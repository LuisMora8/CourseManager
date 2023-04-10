from flask import Flask, render_template, request
# from Flask-SQLAlchemy import SQLalchemy
import SQLAlchemy
# Flask and SQLDatabase configuaration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///students.sqlite"
db = SQLAlchemy(app)


# Database Models
class Login(db.Model):
    username = db.Column(db.String, unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String, unique=True, nullable=False)
    role = db.Column(db.String, nullable=False)

    def __init__(self, username, password, role) -> None:
        super().__init__()
        self.username = username
        self.password = password
        self.role = role

class Students(db.Model):
    # Static variable to create unique key
    numkey = 0

    student_numkey = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

    def __init__(self, first, last) -> None:
        super().__init__()
        Students.numkey += 1
        self.student_numkey = Students.numkey
        self.first_name = first
        self.last_name = last

class Grades(db.Model):
    # Static variable to create unique key
    numkey = 0

    grade_numkey = db.Column(db.Integer, primary_key=True)
    student_numkey = db.Column(db.Integer)
    class_numkey = db.Column(db.Integer)
    grade = db.Column(db.Float)

    def __init__(self, student_key, class_key, grade) -> None:
        super().__init__()
        Grades.numkey += 1
        self.grade_numkey = Grades.numkey
        self.student_numkey = student_key
        self.class_numkey = class_key
        self.grade = grade

class Classes(db.Model):
    # Static variable to create unique key
    numkey = 0

    class_numkey = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String)
    prof_numkey = db.Column(db.Integer)
    start_time = db.Column(db.String)
    end_time = db.Column(db.String)
    days = db.Column(db.String)
    enrolled = db.Column(db.Integer)

    def __init__(self, name, prof_key, start, end, days, enrolled) -> None:
        super().__init__()
        Classes.numkey += 1
        self.class_numkey = Classes.numkey
        self.class_name = name
        self.prof_numkey = prof_key
        self.start_time = start
        self.end_time = end
        self.days = days
        self.enrolled = enrolled

class Professor(db.Model):
    # Static variable to create unique key
    numkey = 0

    prof_numkey = db.Column(db.Integer, primary_key=True)
    prof_name = db.Column(db.Integer)
    class_numkey = db.Column(db.Integer)

    def __init__(self, name, class_key) -> None:
        super().__init__()
        Professor.numkey += 1
        self.prof_numkey = Professor.numkey
        self.prof_name = name
        self.class_numkey = class_key


# Home Page
@app.route('/')
def index():
    return render_template('student.html')

# prof Page
@app.route('/prof')
def index():
    # query the database and retrieve the data
    data = Professor.query.all()

    # pass the data to the template
    return render_template('Professor.html', data=data)
    # return render_template('Professor.html')


# Driver Code
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)