from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import Students, Grades, Classes, Professor, Login, app, db


#Home Page
@app.route('/')
def index():
    # student = Students.query.filter_by(first_name="Jose").first()
    # print(student.first_name)
    # login = Login('josesantos@ucmerced.edu', 1234, 'student',student)
    # db.session.add(login)
    # db.session.commit()

    # people = Professor.query.all()
    # for i in people:
    #     print(i)
    return render_template('index.html')

# prof Page
@app.route('/prof')
def index2():
    #query
    query = db.session.query(Professor.id,Professor.first_name,Professor.last_name, Classes.start_time,Classes.end_time,Classes.days,Classes.enrolled).\
        join(Classes).\
        filter(Professor.id == Classes.prof_id).\
            group_by(Classes.class_name)

    query = prof_to_dict(query)

    # pass the data to the template
    return render_template('Professor.html', data=query)


# Student View Courses
@app.route('/student/<id>', methods=['GET'])
def student_schedule(id):

    # Query Student's in Grades to find Classes
    grades = Grades.query.filter_by(student_id=id)

    # Query the Classes 
    courses = []
    for grade in grades:
        courses.append(Classes.query.filter_by(id=grade.class_id).first())
    data = courses_to_dict(courses)
    # Return query as dictionary
    return render_template('student.html', data=data)

    # student = Students(4, "Li", "Cheng")
    # db.session.add(student)
    # db.session.commit()
    # student = Students.query.filter_by(first_name="John").first()
    # course = Classes.query.filter_by(class_name="Math 101").first()
    # grade = Grades(4,student,course,77)
    # db.session.add(grade)
    # db.session.commit()


# Convert the grades from objects to dictionary (for JSON)
def prof_to_dict(list):
    output = []
    for profData in list:
        c = {}
        c["id"] = profData.id
        c["profName"] = profData.first_name + " " + profData.last_name
        c["time"] = profData.days + " "+ profData.start_time + " "+profData.end_time
        c["enrolled"] = profData.enrolled
        
        output.append(c)
    return output


# Convert the grades from objects to dictionary (for JSON)
def courses_to_dict(list):
    output = []
    for course in list:
        c = {}
        c["course"] = course.class_name
        c["prof"] = course.prof.first_name + " " + course.prof.last_name
        c["time"] = course.days + " " + course.start_time + " " + course.end_time
        c["enrollment"] = course.enrolled
        output.append(c)
    return output

# Driver Code
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)