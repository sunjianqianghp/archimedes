from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__, template_folder='D:\\projects\\archimedes\\src\\templates')

@app.route("/")
def choose_year():
    print('============================')
    return render_template("choose_year.html")

@app.route("/search", methods = ['POST', 'GET'])
def search():
    if request.method == "POST":
        yr = request.form['yr']
        return redirect(url_for('year_of_you', yr=yr))

    
@app.route("/<yr>", methods = ["POST","GET"])
def year_of_you(yr):
    if yr in ['2020', '2021', '2022', '2023']:
        return render_template("u{}.html".format(yr))
    else:
        return render_template("others.html" )



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

