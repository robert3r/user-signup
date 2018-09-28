from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/welcome", methods=['GET'])
def welcome():
    user = request.form['username']
    return render_template('welcome.html', username = user)

@app.route("/", methods=['POST'])
def validate_password():

    space = [' ']
    special = ['.','@']

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if len(username) < 3 or len(username) > 20 or username == "" or any(char in space for char in username):
        username_error = 'That is not a valid username'
        username = ''
    if len(password) < 3 or len(password) > 20 or password == "":
        password_error = 'That is not a valid password'
        password = '' 
        username = username
        email = email
    if verify != password or verify == "":
        verify_error = 'Passwords do not match'
        username = username
        password = ''
        verify = ''
        email = email
    if  email != "":
        if len(email) < 3 or len(email) > 20 or not any(char in special for char in email):
            email_error = 'That is not a valid email'
            username = username
            password = ''
            verify = ''
            email = ''    


    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username = username)
    else:
        return render_template('index.html',username = username, email = email, username_error = username_error, password_error = password_error, verify_error = verify_error, email_error = email_error)
  
@app.route("/")
def display_index():
    return render_template('index.html')

app.run()
