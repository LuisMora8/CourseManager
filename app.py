from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Flask and SQLDatabase configuaration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://grades.sqlite"
db = SQLAlchemy(app)


# Database Models

class Students(db.Model):
    # Static variable to create unique key
    numkey = 0

    student_numkey = db.Column(db.Integer)
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

    grade_numkey = db.Column(db.Integer)
    student_numkey = db.Column(db.Integer)
    class_numkey = db.Column(db.Integer)
    grade = db.Column(db.Double)

    def __init__(self, student_key, class_key, grade) -> None:
        super().__init__()
        Grades.numkey += 1
        self.grade_numkey = Grades.numkey
        self.student_numkey = student_key
        self.class_numkey = class_key
        self.grade = grade

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Driver Code
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)