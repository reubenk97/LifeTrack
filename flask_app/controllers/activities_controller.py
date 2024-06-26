from flask_app import app
from flask import render_template, session, redirect, request, flash
from flask_app.models.activity_model import Activity
from flask_app.models.category_model import Category
import os

# Life Tracker Page
@app.route('/lifetrack')
def life_tracker():
    if 'user_id' not in session:
        return redirect('/')
    maps_key = os.environ.get("LIFETRACK_GOOGLEMAPS_API_KEY")
    categories_list = Category.get_all()
    return render_template('/activities_new.html', maps_key = maps_key, categories_list = categories_list)

# View Activity Page
@app.route('/activities')
def activity_page():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id':session['user_id']
    }
    activities_list = Activity.get_all(data)
    return render_template('/activities_page.html', activities_list = activities_list)

# Process creating a new Activity
@app.route('/activities/add', methods=['post'])
def add_activity():
    if 'user_id' not in session:
        return redirect('/')
    print("Attempting to add Activity.")
    if not Activity.validate(request.form):
        return redirect('/lifetrack')
    data = {
        **request.form,
        'user_id':session['user_id']
    }
    Activity.create(data)
    return redirect('/lifetrack')