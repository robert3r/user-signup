from flask import Flask, request, redirect, render_template, url_for
import cgi
import re

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route('/welcome', methods=['GET'])
def welcome():
    user = request.args.get('username')
    return render_template('welcome.html', username = user)

@app.route('/', methods=['POST'])
def validate_password():

    space = [' ']

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
    """ if len(password) < 3 or len(password) > 20 or password == "":
        password_error = 'That is not a valid password'
        password = '' 
        username = username
        email = email """
    if password == "" or not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
        password_error = 'Type 8 char including at least one number, special char, capital and lower letter.'
        password = '' 
        username = username
        email = email     
    if verify != password or verify == "":
        verify_error = 'Passwords do not match'
        username = username
        password = ''
        verify = ''
        email = email 
          
    """ if  email != "":
        if len(email) < 3 or len(email) > 20 or not any(char in special for char in email) """
    if email != "" and len(email) < 6 or len(email) > 20:
        if not re.match('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', email)!= None:
            email_error = 'That is not a valid email'
            username = username
            password = ''
            verify = ''
            email = ''    


    if not username_error and not password_error and not verify_error and not email_error:
        # return render_template('welcome.html', title = "Welcome", username = username)
        return redirect( 'welcome?username={}'.format(username) )
    else:
        return render_template('register.html',title="Signup", username = username, email = email, username_error = username_error, password_error = password_error, verify_error = verify_error, email_error = email_error)
  
@app.route('/')
def display_index():
    return render_template('register.html', title = "Signup")

app.run()
