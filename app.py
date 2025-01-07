from flask import Flask,flash, render_template, request,url_for,redirect,Response,session,send_file,send_from_directory

app=Flask(__name__)
@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")
   

if  __name__=='__main__':
    app.run(debug=True)