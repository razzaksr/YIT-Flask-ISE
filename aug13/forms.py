from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class OutPatientForm(FlaskForm):
    # name = field(label)
    patient = StringField("Patient Name",validators=[
        DataRequired(message="Patient name is mandate"),
        Regexp(r"^[A-Za-z ]{3,50}$", message="Invalid patient name")
    ])
    address = TextAreaField("Patient Address",validators=[
        DataRequired("Address is mandate"),
        Regexp(r"^(?=.*[-.#])(?=.+[0-9])[A-Za-z0-9-.#, ]{10,100}$", message="invalid address")
    ])
    contact = StringField("Contact number",validators=[
        DataRequired(message="Contact number is mandate"),
        Regexp(r"^[0-9]{10}$", message="invalid contact number")
    ])
    gender = RadioField("Gender",choices=[
        ("male","Male"),
        ("female","FeMale"),
        ("other","Other"),
    ], validators=[
        DataRequired(message="gender is madate")
    ])
    symptoms = SelectMultipleField("Tell us What do you feel",choices=[
        ("cough","Cough"),
        ("cold","Cold"),
        ("backpain","Back Pain"),
        ("headache","Headache")
    ], validators=[
        DataRequired(message="Any one symptoms has to select")
    ])
    age = StringField("age", validators=[
        DataRequired(message="Age is mandate"),
        Regexp(r"^[0-9]{1,2}$",message="Invalid Age")
    ])
    policy = BooleanField("Did you availed any health insurance?")
    submit = SubmitField("Admit")