from flask import Flask,request,redirect,render_template,session
import db

app=Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        render_template('login.html')
    else:
        user=request.form['user']
        pw=request.form['pass']

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='GET':
        render_template('register.html')
    else:
        name=request.form['name']
        user=request.form['user']
        pw=request.form['pass']
        color=request.form['color']

@app.route('/logout')
def logout():
    #if logged in, log out
    #redirect to login
    redirect('/login')

@app.route('/about')
def about():
    render_template('about.html')

@app.route('/home')
def home():
    ##check if logged in
    render_template('home.html')
    ##else, redirect to login and store home with sessions
    
@app.route('/setting',methods=['GET','POST'])
def settings():
    ##check if logged in
    if request.method=='GET':
        render_template('settings.html')
    else:
        ##get new info and update
        pass
    ##if not logged in, redirect to login and store settings with sessions

if __name__ == '__main__':
    app.debug=True
    app.run()
