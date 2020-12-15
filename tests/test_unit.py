import unittest
from flask import url_for

from application import app, db
from application.models import Todo

class Testbase(unittest.TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI= getenv('DATABASE_URI'),
            SECRET_KEY= getenv('SECRET_KEY'),
            DEBUG=True
        )
        return app

    def setUp(self):
        db.create_all()
        test_task=Todo(name="test flask app")
        db.session.add(test_task)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(Testbase):
    def test_read_get(self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for('update', id=1))
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete', number=1), follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_complete_get(self):
        response = self.client.get(url_for('complete', id=1), follow_redirects=True)
        self.assertEqual(response.status_code,200)

class TestRead(Testbase):
    def test_read_tasks(self):
        response= self.client.get(url_for("read"))
        self.assertIn(b"test flask app", response.data)

class TestCreate(Testbase):
    def test_add_task(self):
        response = self.client.post(url_for("read"),
            data=dict(entry_name="Create a new task", status="incomplete"),
            follow_redirects=True
        )
        self.assertIn(b"Create a new task", response.data)
    
class TestUpdate(Testbase):
    def test_update_task(self):
        response = self.client.post(url_for("update", id=1),
            data=dict(entry_name="Update a task", status="incomplete"),
            follow_redirects=True
        )
        self.assertIn(b"Update a task", response.data)

class TestDelete(Testbase):
    def test_update_task(self):
        response = self.client.get(url_for("delete", number=1),
            follow_redirects=True
        )
        self.assertNotIn(b"test flask app", response.data)
    
