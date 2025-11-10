import os
from flask import Flask, g, render_template
import flask_sijax

# Define path to Sijax static files
path = os.path.join(os.path.dirname(__file__), 'static/js/sijax/')

app = Flask(__name__)

app.config['SIJAX_STATIC_PATH'] = path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'

# Initialize Sijax
flask_sijax.Sijax(app)


@app.route('/')
def index():
    return 'Index'


@flask_sijax.route(app, '/hello')
def hello():
    def say_hi(obj_response):
        obj_response.alert('Hi there!')

    if g.sijax.is_sijax_request:
        # Sijax request detected - handle it
        g.sijax.register_callback('say_hi', say_hi)
        return g.sijax.process_request()

    # Regular (non-Sijax) request
    return render_template('sijaxexample.html')


if __name__ == '__main__':
    app.run(debug=True)
