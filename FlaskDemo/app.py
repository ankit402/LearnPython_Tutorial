from flask import Flask, render_template

# It will create an instance of Flask
app = Flask(__name__)

@app.route("/")
def Welcome():
    page_title = "My Flask App"
    page_content = "an HTML template"
    return render_template('Magcall.html', title=page_title, content=page_content)

@app.route("/index")
def index():
    return "This is my index page for the app"


@app.route("/test")
def test():
    return "This is my index page for the app"
if __name__ == '__main__':
    app.run(debug=True)
