from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def user_signup():
    return render_template('index.html')

@app.route('/user-signup', methods=['POST'])
def validate_form():

    username=request.form['username']
    username_error=""
    if username == "":
        username_error = 'Please enter a username'
    if " " in username:
        username_error = 'Username cannot contain a space'
    if len(username) < 3 or len(username)  > 20:
        username_error = 'Username length must be between 3 and 20 characters'
        username = ""
    
    password=request.form['password']
    password_error=""
    if password == "":
        password_error ='Please enter a password'
        password = ""

    if len(password) < 3 or len(password) > 20:
        password_error = 'Password length must be between 3 and 20 characters'
        username = ""

    verify_password=request.form['verify_password']
    verify_error=""
    if verify_password == "":
        verify_error = 'Please verify the password. Re-enter password'
        verify_password = ""
    if verify_password != password:
        verify_error = 'Passwords do not match.  Please verify password'
        verify_password = ""

    email=request.form['email']
    email_error=""
    if email != "":
        if email.count('.') > 1 or email.count('@') > 1:
            email_error = 'The email is not valid'

        if '@' not in email  or '.' not in email:
            email_error = 'The email is not valid'

        if " " in email:
            email_error = 'The email is not valid'
    
    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template(
            'index.html', username_error=username_error,
            password_error=password_error,
            verify_error=verify_error,
            email_error=email_error)



app.run()