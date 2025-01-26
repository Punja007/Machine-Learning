from flask import Flask,render_template,request

app = Flask(__name__)  #It creates an instance of WSGI application

@app.route("/")
def welcome():
    return "<html><H1>Hello welcome to the html flask integration.</H1></html>"

@app.route("/index")
def home():
    return render_template('index.html')

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method =='POST':
        name = request.form['naame']
        return f'hello {name} welcome!'
    return render_template('form.html')


#as i have used action attribute in html page as submit the form route is pretty much useless
#action attribute of html form is basically the path where we want to send the form after clicking submit button
@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method =='POST':
        name = request.form['naame']
        return f'hello {name}!'
    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)