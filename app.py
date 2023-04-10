from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import Students, Grades, Classes, Professor, Login, app, db


#Home Page
@app.route('/')
def index():
   return render_template('index.html')

# Student View Courses
@app.route('/<student>')
def student_schedule():
    # student = Students(4, "Li", "Cheng")
    # db.session.add(student)
    # db.session.commit()
    # student = Students.query.filter_by(first_name="John").first()
    # course = Classes.query.filter_by(class_name="Math 101").first()
    # grade = Grades(4,student,course,77)
    # db.session.add(grade)
    # db.session.commit()
    return render_template('student.html')
    

# Driver Code
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)