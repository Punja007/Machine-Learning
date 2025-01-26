from flask import Flask,url_for,redirect,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('proj.html')


@app.route("/submit",methods=['GET','POST'])
def submit():
    final_score=0
    if request.method=='POST':
        sci = float(request.form['science'])
        maths = float(request.form['maths'])
        eng = float(request.form['english'])

        final_score=(sci+maths+eng)/3

    return redirect(url_for('success',score=final_score))


@app.route('/result/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "passed"
    else:
        res = "failed"

    result = {'scr':score,'res':res}
    return render_template('results2.html', result=result)

    


if __name__ == "__main__":
    app.run(debug=True)
