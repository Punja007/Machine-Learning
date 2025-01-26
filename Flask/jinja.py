from flask import Flask,render_template,request

app = Flask(__name__)  #It creates an instance of WSGI application

@app.route("/")
def welcome():
    return "<html><H1>Hello welcome to the html flask integration.</H1></html>"

@app.route("/index")
def home():
    return render_template('index.html')


@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method =='POST':
        name = request.form['name'] 
        return f'hello {name}!'
    return render_template('form.html')

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "passed"
    else:
        res = "failed"

    return render_template('results.html', result=res,marks=score)


@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score >= 50:
        res = "passed"
    else:
        res = "failed"

    result = {'scr':score,'res':res}
    return render_template('results2.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)