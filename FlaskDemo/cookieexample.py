from flask import Flask, render_template, request, make_response, session, redirect, url_for

#constructor
app= Flask(__name__)

app.secret_key = 'xxxxxxxfgdgdgfhfghfdgfgfdggdgdgdgdgg'


@app.route('/')
def index():
    return render_template('index.html')

#setcookie
@app.route('/setcookie' , methods=['GET', 'POST'] )
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('readcookie.html'))
        # hold the data in the cookie variable userid --> request.form['nm']
        resp.set_cookie('userid', user)
        return resp


@app.route('/getcookie' , methods=['GET', 'POST'] )
def getcookie():
    name = request.cookies.get('userid')
    return "<h1>%s</h1>" % name

@app.route('/login' , methods=['GET', 'POST'] )
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index2'))
    return '''

       <form action = "" method = "post">
          <p><input type = text name = username/></p>
          <p><input type = submit value = Login /></p>
       </form>

       '''

@app.route('/logout' , methods=['GET', 'POST'] )
def logout():
    session.pop('username', None)
    return redirect(url_for('index2'))


if __name__=='__main__':
    app.run(debug=True)