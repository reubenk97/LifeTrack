from flask_app import app
from flask import render_template, session, redirect, request, flash

# View Activity Page
@app.route('/activities')
def activity_page():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('/activities_page.html')
