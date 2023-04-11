from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Flask and SQLDatabase configuaration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///students.sqlite"
db = SQLAlchemy(app)

# Database Models
class Login(db.Model):
    __tablename__ = 'login'

    username = db.Column(db.String, unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String, unique=True, nullable=False)
    role = db.Column(db.String, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    student = db.relationship('Students', backref=db.backref('user'))

    def __init__(self, username, password, role, student) :
        super().__init__()
        self.username = username
        self.password = password
        self.role = role
        self.student = student

class Students(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

    def __init__(self, id, first, last):
        super().__init__()
        self.id = id
        self.first_name = first
        self.last_name = last

class Grades(db.Model):
    __tablename__ = 'grades'

    numkey = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    student = db.relationship('Students', backref=db.backref('students'))
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))
    course = db.relationship('Classes', backref=db.backref('classes'))
    grade = db.Column(db.Float)

    def __init__(self, numkey, student, course, grade) :
        super().__init__()
        self.numkey = numkey
        self.student = student
        self.course = course
        self.grade = grade

class Classes(db.Model):
    __tablename__ = 'classes'

    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String)
    prof_id = db.Column(db.Integer, db.ForeignKey('professor.id'))
    prof = db.relationship('Professor', backref=db.backref('professor'))
    start_time = db.Column(db.String)
    end_time = db.Column(db.String)
    days = db.Column(db.String)
    enrolled = db.Column(db.Integer)

    def __init__(self, id, prof, name, start, end, days, enrolled):
        super().__init__()
        self.id = id
        self.prof = prof
        self.class_name = name
        self.start_time = start
        self.end_time = end
        self.days = days
        self.enrolled = enrolled

class Professor(db.Model):
    __tablename__ = 'professor'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

    def __init__(self, id, first, last) :
        super().__init__()
        self.id = id
        self.first_name = first
        self.last_name = last