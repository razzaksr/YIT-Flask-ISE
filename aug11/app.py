from flask import Flask, jsonify, render_template, request
from data import accounts
app = Flask(__name__)

# @app.route("/",methods=['GET'])
# def calculator():
#     return render_template('index.html')
# @app.route("/findbmi", methods=['POST'])
# def finding():
#     height = float(request.form['height'])
#     weight = float(request.form['weight'])
#     height=height/100
#     # print(height,weight)
#     bmi = weight/(height*height)
#     # print(bmi)
#     return render_template('index.html',result=bmi)

@app.route("/findbmi",methods=['GET','POST'])
def calculator():
    if request.method == "GET":
        return render_template('index.html')
    else:
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        height=height/100
        bmi = weight/(height*height)
        return render_template('index.html',result=bmi)

@app.route("/view",methods=['GET'])
def view():
    return render_template('view.html',customers = accounts)

@app.route("/greet", methods=['GET'])
def greetings():
    return jsonify({"message":"welcome all of you to learn flask jinja"})

if __name__ == "__main__":
    app.run('localhost',7777)