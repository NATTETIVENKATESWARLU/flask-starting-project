from flask import Flask,render_template

app=Flask(__name__)


#basic string 
@app.route('/')
def hii():
    return "<h1>hello wold<h1>"


#web pages adding
@app.route('/index')
def html():
    return render_template('index.html')




if __name__=='__main__':
    app.run(debug=True)