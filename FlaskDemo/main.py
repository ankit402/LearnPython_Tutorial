from flask import Flask, render_template, request, redirect, url_for

# initialize constructor
app = Flask(__name__)

#define route
@app.route("/")
def home():
    return "Welcome to Home Page"

from flask import Flask

app = Flask(__name__)

@app.route("/openurl")
def openurl():
    return "https://www.tutorialspoint.com/flask/flask_routing.htm"

# You can also add another route manually
app.add_url_rule("/", "home", openurl)

@app.route("/index")
def index():
    return "This is my index page for the app"

@app.route('/welcome/<name>')
def welcome(name):
    return 'Welcome to welcome Page %s' % name

@app.route("/About")
def About():
    return "Welcome to About Page"

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

#ulr_for
@app.route('/admin')
def admin():
    return "Welcome to Admin Page"

@app.route('/not admin')
def not_admin():
    return "Welcome to Not Admin Page"

'''
    The url_for() function is very useful for dynamically
    building a URL for a specific function. The function accepts
    the name of a function as first argument, and one or more keyword arguments, 
    each corresponding to the variable part of URL.
    The following script demonstrates use of url_for() function.
'''

@app.route('/user/<username>')
def user(username):
    if username == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('not_admin'))

if __name__ == "__main__":
    app.run(debug=True)