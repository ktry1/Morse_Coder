from werkzeug.utils import redirect
from wtforms import SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired

from classes import Decoder, Butler
from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.widgets import TextArea
decoder=Decoder()
butler=Butler()
app = Flask(__name__)
Bootstrap(app)




@app.route("/", methods=["POST","GET"])
def home():
    if request.method=="POST":
        choice=request.form.get("choice")
        text=request.form.get("input")
        answer=butler.direct(text,choice,decoder.cipher, decoder.decipher)
        return render_template("output.html",answer=answer)

    return render_template("index.html")








app.run()