from flask_app import app
from flask import render_template, session, redirect, request, flash
from flask_app.models.todo_model import Todo
from flask_app.models.user_model import User
from flask_app.models.goal_model import Goal

# Reminder/Goals Page
@app.route('/todos')
def todo_page():
    if 'user_id' not in session:
        return redirect('/')
    todos_list = Todo.get_all({'id':session['user_id'], 'completed':0})
    completed_list = Todo.get_all({'id':session['user_id'], 'completed':1})
    return render_template('/todos_page.html', todos_list = todos_list, completed_list = completed_list)

@app.route('/goals')
def goals_page():
    if 'user_id' not in session:
        return redirect('/')
    goals_list = Goal.get_all({'id':session['user_id']})
    return render_template('/goals_page.html', goals_list = goals_list)

@app.route('/todos/add', methods=['post'])
def ajax_add_todo():
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

@app.route('/todos/<int:id>/edit', methods=['post'])
def ajax_edit_todo(id):
    if 'user_id' not in session:
        return redirect('/')
    errors = Todo.validate(request.form)
    if len(errors) > 0:
        return {'message':'validations failed', 'errors':errors}
    todo_data = {
        **request.form,
        'user_id': session['user_id']
    }
    Todo.update(todo_data)
    logged_user = User.get_by_id({'id':session['user_id']})

    res = {
        **todo_data,
        'id':id,
        'username':f'{logged_user.username}'
    }
    
    return res

@app.route('/todos/<int:id>/delete')
def delete_todo(id):
    if 'user_id' not in session:
        return redirect('/')
    Todo.remove({'id':id})
    return redirect('/todos')

@app.route('/todos/<int:id>/complete', methods=['post'])
def complete_todo(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id':id
    }
    Todo.complete(data)
    return data