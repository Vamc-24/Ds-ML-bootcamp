from flask import Flask, render_template,request

app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome, it is my flask web page! My name is vamsi. pursuing AIDS "

@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
       name=request.form['name']
       email=request.form['email']
       phone=request.form['phone']
       return f'Hello {name} \n Your email is {email} \n Your phone num is : {phone}'
    return render_template("form.html")
    

if __name__=="__main__":
    app.run(debug=True)



