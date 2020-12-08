from application import db
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    status=db.Column(db.String(30))

class Add(FlaskForm):
    entry_name = StringField('Task Name')
    status = StringField('Status')
    submit = SubmitField('Add Entry')