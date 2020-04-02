"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
import datetime
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import AddUser
from app.models import UserProfile
import psycopg2
from werkzeug.utils import secure_filename 

# from werkzeug.security import check_password_hash


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')
    
@app.route('/profile', methods=['GET','POST'])
def profile():
    
    #instantiation of the form
    user = AddUser()
    
    #making a post request and validating data on submission
    if (request.method == "POST" and user.validate_on_submit()):
        
        #doing things the original way and not being fancy 
        
        #taking data from the form and adding it to the db
        
        firstname = user.firstname.data
        lastname = user.lastname.data
        gender = user.gender.data
        email = user.email.data
        location = user.location.data
        biography = user.biography.data 
        
        
        photo = user.photo.data
        
        #saving the photo to the uploads folder
        
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        newUser = UserProfile(first_name=firstname, last_name=lastname, gender=gender, email=email, location=location, biography=biography, photo="uploads/"+filename)
        
        
        db.session.add(newUser)
        db.session.commit()
        
        
        flash('Your Profile has been Successfully added!')
        return redirect(url_for('profiles'))
        
    return render_template("profile.html",form = user)
        
        #  photo = AddUser.photo.data

        #  filename = secure_filename(photo.filename)
        
        #  photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
        # #saving data to the database
        # user = UserProfile(request.form['firstname'], request.form['lastname'], request.form['gender'],
        #           request.form['email'], request.form['location'], request.form['biography'])
                  
        

#not sure if right but we'll see once i fix that error ... 
#profiles route
@app.route('/profiles')
def profiles():
    
    # users = db.session.query(UserProfile).all
    
    users = UserProfile.query.all()
    return render_template("profiles.html", users=users)
    
    

#"/profile/<userid>" route




# #date function to be used in db
# def getDate():

#     today = datetime.datetime.utcnow()
    
    # return today.strftime("%d %m %Y")

###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
