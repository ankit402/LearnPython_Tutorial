from flask import Flask , render_template


#constructor to call the flask and init the request
app = Flask(__name__)

#route define
@app.route('/index')

def index():
    return render_template('test.html')
    #jinja2 technique the templates folder should present
    # to hold the html pages inside the folder


@app.route('/')
def main():
    return '<h1> hello this is my main root   </h1>'


if __name__ == '__main__':
    app.run(debug= True)

