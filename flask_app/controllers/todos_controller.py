from flask_app import app
from flask import render_template, session, redirect, request, flash
from flask_app.models.todo_model import Todo
from flask_app.models.user_model import User

# Reminder/Goals Page
@app.route('/todos')
def todo_page():
    if 'user_id' not in session:
        return redirect('/')
    todos_list = Todo.get_all({'id':session['user_id']})
    return render_template('/todos_page.html', todos_list = todos_list)

@app.route('/todos/add', methods=['post'])
def add_todo():
    if 'user_id' not in session:
        return redirect('/')
    print(request.form)
    errors = Todo.validate(request.form)
    if len(errors) > 0:
        return {'message':'validations failed', 'errors':errors}
    todo_data = {
        **request.form,
        'user_id': session['user_id']
    }
    id = Todo.create(todo_data)
    logged_user = User.get_by_id({'id':session['user_id']})

    res = {
        **todo_data,
        'id':id,
        'username':f'{logged_user.username}'
    }
    
    return res