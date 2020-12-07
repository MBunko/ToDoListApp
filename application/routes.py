from application import app, db
from application.models import Todo

@app.route('/add')
def add():
    new_task = Todo(name="New task", status="Not started")
    db.session.add(new_task)
    db.session.commit()
    return "Added new task to database"

@app.route('/read')
@app.route('/')
def read():
    all_tasks = Todo.query.all()
    tasks_string = ""
    for task in all_tasks:
        tasks_string += "<br>"+ str(task.id) + ". " + task.name+ "- " +task.status
    return tasks_string

@app.route('/update/<int:number>/<name>')
def update(name, number):
    task = Todo.query.filter_by(id=number).first()
    if task is not None:
        task.name = name
        db.session.commit()
        return task.name
    else:
        return "entry does not exist"

@app.route('/delete/<int:number>')
def delete(number):
    task = Todo.query.filter_by(id=number).first()
    if task is not None:
        db.session.delete(task)
        db.session.commit()
        return task.name
    else:
        return "Entry does not exist"

@app.route('/count')
def count():
    number = Todo.query.count()
    n2=str(number)
    return n2

@app.route('/status/<int:number>/<name>')
def status(number, name):
    task = Todo.query.filter_by(id=number).first()
    if task is not None:
        task.status = name
        db.session.commit()
        return task.status
    else:
        return "Entry does not exist"