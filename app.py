from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import Students, Grades, Classes, Professor, Login, app, db

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from wtforms.widgets import TextArea

# Admin Subclasses
class ChildView(ModelView):
    column_display_pk = True
    column_hide_backrefs = False
    #column_list = ('id', 'name', 'parent')

class LoginView(ModelView):
    column_display_pk = True
    column_hide_backrefs = False
    list_columns = ('username', 'password', 'role', 'student_id')
    form_columns = ('username', 'password', 'role', 'student')

class StudentView(ModelView):
    column_display_pk = True
    column_hide_backrefs = False
    list_columns = ('id', 'first_name', 'last_name')
    form_columns = ('id', 'first_name', 'last_name')

class ProfessorView(ModelView):
    column_display_pk = True
    column_hide_backrefs = False
    list_columns = ('id', 'first_name', 'last_name')
    form_columns = ('id', 'first_name', 'last_name')

class GradesView(ModelView):
    column_display_pk = True
    column_hide_backrefs = False
    list_columns = ('numkey', 'student_id', 'student','class_id', 'course', 'grade')
    form_columns = ('numkey', 'student','course', 'grade')

class ClassesView(ModelView):
    column_display_pk = True
    column_hide_backrefs = False
    list_columns = ('id', 'class_name', 'prof_id','prof', 'start_time', 'end_time', 'days', 'enrolled')
    form_columns = ('id', 'prof','class_name', 'start_time', 'end_time', 'days', 'enrolled')

# Home Page
@app.route('/')
def index():
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

# Convert the query from objects to dictionary (for JSON)
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

# Convert the query from objects to dictionary (for JSON)
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

# Student View Load Courses
@app.route('/student/<id>', methods=['GET'])
def student_schedule(id):
    courses = []

    # Query Student's in Grades to find Classes
    grades = Grades.query.filter_by(student_id=id)

    if(request.method == 'GET'):
        # Query the Student's Classes 
        for grade in grades:
            courses.append(Classes.query.filter_by(id=grade.class_id).first())
        data = courses_to_dict(courses)
        # Return query as dictionary
        return render_template('student.html', data=data)

# Return Current Schedule
@app.route('/student/<id>/your-courses', methods=['GET'])
def view_schedule(id):
    # Query Student's in Grades to find Classes
    grades = Grades.query.filter_by(student_id=id)

    # Query the Student's Classes 
    courses = []
    for grade in grades:
        courses.append(Classes.query.filter_by(id=grade.class_id).first())
    data = courses_to_dict(courses)
    # Return query as dictionary
    return data

# Return Classes Available to Register
@app.route('/student/<id>/add-courses', methods=['GET'])
def view_all_courses(id):
    # Query Student's in Grades to find Classes
    grades = Grades.query.filter_by(student_id=id)

    # Query the Student's Classes 
    student_courses = []
    for grade in grades:
        student_courses.append(Classes.query.filter_by(id=grade.class_id).first())
    # Query All Classes
    all_courses = Classes.query.all()

    # Return dictionary of classes
    data = registration_courses_to_dict(student_courses, all_courses)
    return data

# Add and Remove Classes
@app.route('/student/<id>/add-courses/<classname>', methods=['POST', 'DELETE'])
def register(id, classname):
    # Query Student's in Grades to find Classes
    grades = Grades.query.filter_by(student_id=id)

    # Query the Student's Classes 
    student_courses = []
    for grade in grades:
        student_courses.append(Classes.query.filter_by(id=grade.class_id).first())

    data = dict(request.json)
    course = Classes.query.filter_by(class_name=data["course_name"].replace("%20", " ")).first()
    # Create Grade to add Class to Schedule
    if(request.method == 'POST'):
        # Query Grades To Get Last Numkey
        query = Grades.query.all()
        new_grade_numkey = query[-1].numkey + 1
        student = Students.query.filter_by(id=id).first()
        # Add grade
        new_grade = Grades(new_grade_numkey, student, course, 0)
        print(new_grade.student.first_name)
        db.session.add(new_grade)
        # Query Class and increase enrollment
        course.enrolled = course.enrolled + 1
        db.session.commit()
    
    # Post New Grade for Student
    elif(request.method == 'DELETE'):
        # Query the selected class/grade and delete
        old_grade = Grades.query.filter_by(student_id=id).first()
        db.session.delete(old_grade)
        # Decrease enrollment
        course.enrolled = course.enrolled - 1
        db.session.commit()
    
     # Query All Classes
    all_courses = Classes.query.all()
    # Return dictionary of classes
    data = registration_courses_to_dict(student_courses, all_courses)
    return data
    
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

# Convert the grades from objects to dictionary (for JSON)
def registration_courses_to_dict(student_classes, all_courses):
    output = []
    for course in all_courses:
        c = {}
        c["course"] = course.class_name
        c["prof"] = course.prof.first_name + " " + course.prof.last_name
        c["time"] = course.days + " " + course.start_time + " " + course.end_time
        c["enrollment"] = course.enrolled
        if(course in student_classes):
            c["enrolled"] = True
        else:
            c["enrolled"] = False
        output.append(c)
    return output

# Driver Code
if __name__ == '__main__':

# Admin
    with app.app_context():
        #Login.__table__.drop(db.engine)
        db.create_all()
        admin = Admin(app)
        admin.add_view(LoginView(Login, db.session))
        admin.add_view(StudentView(Students, db.session))
        admin.add_view(ProfessorView(Professor, db.session))
        admin.add_view(ClassesView(Classes, db.session))
        admin.add_view(GradesView(Grades, db.session))
    app.run(debug=True)