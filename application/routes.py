from application import app, db
from application.models import Todo
from application.models import Add
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

@app.route('/add')
def add():
    new_task = Todo(name="New task", status="Not started")
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("read"))

@app.route('/read', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def read():
    all_tasks = Todo.query.all()
    tasks_string = ""

    form=Add()
    if request.method == 'POST':
        entry_name = form.entry_name.data
        status = form.status.data

        if len(entry_name) == 0 or len(status) == 0:
            error = "Please supply both task name and status"
        else:
            new_task = Todo(name=entry_name, status=status)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("read"))

    return render_template('add.html', form=form) + render_template("index.html", title="Read", all_tasks=all_tasks)

@app.route('/update/<int:id>', methods= ["GET", "POST"])
def update(id):
    form=Add()
    task = Todo.query.filter_by(id=id).first()
    if request.method =="POST":
        task.name = form.entry_name.data
        task.status=form.status.data
        db.session.commit()
        return redirect(url_for("read"))
    return render_template("update.html", form=form, title="Update", task=task)

@app.route('/delete/<int:number>')
def delete(number):
    task = Todo.query.filter_by(id=number).first()
    if task is not None:
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for("read"))
    else:
        return "Entry does not exist"

@app.route('/count')
def count():
    number = Todo.query.count()
    n2=str(number)
    return n2

@app.route ('/complete<int:id>', methods = ["GET", "POST"])
def complete(id):
    form=Add()
    task = Todo.query.filter_by(id=id).first()
    task.status="complete"
    db.session.commit()
    return redirect(url_for("read"))



@app.route('/status/<int:number>/<name>')
def status(number, name):
    task = Todo.query.filter_by(id=number).first()
    if task is not None:
        task.status = name
        db.session.commit()
        return task.status
    else:
        return "Entry does not exist"