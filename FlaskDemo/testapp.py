from flask import Flask , url_for , request , redirect

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return f'<h1>{name}</h1>'

#use for http verbs for serve the request from the url
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=request.form['name']))

if __name__ == '__main__':
    app.run(debug=True)

