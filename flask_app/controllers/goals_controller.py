from flask_app import app
from flask import render_template, session, redirect, request, flash
from flask_app.models.user_model import User
from flask_app.models.goal_model import Goal

@app.route('/goals/add', methods=['post'])
def ajax_add_goal():
    if 'user_id' not in session:
        return redirect('/')
    print(request.form)
    errors = Goal.validate(request.form)
    if len(errors) > 0:
        return {'message':'validations failed', 'errors':errors}
    goal_data = {
        **request.form,
        'user_id': session['user_id']
    }
    id = Goal.create(goal_data)
    logged_user = User.get_by_id({'id':session['user_id']})

    res = {
        **goal_data,
        'id':id,
        'username':f'{logged_user.username}'
    }
    
    return res

@app.route('/goals/<int:id>/edit', methods=['post'])
def ajax_edit_goal(id):
    if 'user_id' not in session:
        return redirect('/')
    errors = Goal.validate(request.form)
    if len(errors) > 0:
        return {'message':'validations failed', 'errors':errors}
    goal_data = {
        **request.form,
        'user_id': session['user_id']
    }
    Goal.update(goal_data)
    logged_user = User.get_by_id({'id':session['user_id']})

    res = {
        **goal_data,
        'id':id,
        'username':f'{logged_user.username}'
    }
    
    return res

@app.route('/goals/<int:id>/delete')
def delete_goal(id):
    if 'user_id' not in session:
        return redirect('/')
    Goal.remove({'id':id})
    return redirect('/goals')