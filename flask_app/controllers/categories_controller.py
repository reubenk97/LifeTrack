from flask_app import app
from flask import render_template, session, redirect, request, flash
from flask_app.models.activity_model import Activity
from flask_app.models.category_model import Category

@app.route('/categories')
def category_page():
    if 'user_id' not in session:
        return redirect('/')
    categories_list = Category.get_all()
    return render_template('categories_page.html', categories_list = categories_list)

@app.route('/categories/add', methods=['post'])
def ajax_add_category():
    if 'user_id' not in session:
        return redirect('/')
    errors = Category.validate(request.form)
    if len(errors) > 0:
        return {'message':'validations failed', 'errors':errors}
    category_data = {
        **request.form,
        'user_id':session['user_id']
    }
    id = Category.create(request.form)
    res = {
        **category_data,
        'id':id
    }
    return res