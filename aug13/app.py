from flask import *
from forms import OutPatientForm

app = Flask(__name__)
# csrf token
app.config["SECRET_KEY"] = "iscflaskyit"

# in memory
patients = []

@app.route("/view")
def viewAll(): return render_template("patients.html", data = patients)

@app.route("/", methods=["GET", "POST"])
def admit():
    op = OutPatientForm()
    if op.validate_on_submit():
        person = {
            op.patient.name : op.patient.data,
            op.address.name : op.address.data,
            op.contact.name : op.contact.data,
            op.symptoms.name : op.symptoms.data,
            op.gender.name : op.gender.data,
            op.age.name : op.age.data,
            op.policy.name : op.policy.data
        }
        patients.append(person)
        return redirect("/view")
    return render_template('main.html', form = op)

if __name__ == "__main__": app.run('localhost',7766)