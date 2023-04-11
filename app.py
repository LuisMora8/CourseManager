from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
from models import Students, Grades, Classes, Professor, Login, app, db


#Home Page
@app.route('/')
def index():
    return render_template('index.html')

# prof Page
@app.route('/prof')
def index2():
    #query
    query = db.session.query(Classes.class_name,Professor.id,Professor.first_name,Professor.last_name, Classes.start_time,Classes.end_time,Classes.days,Classes.enrolled).\
        join(Classes).\
        filter(Professor.id == Classes.prof_id).\
            group_by(Classes.class_name)
    

    query = prof_to_dict(query)

    # pass the data to the template
    return render_template('Professor.html', data=query)


@app.route('/<name>/<grade>',methods = ['GET'])
def updateData(name,grade):
    dict = {'StuGrade':grade}
    # print(dict["StuGrade"])
    # print(name)
    # print(grade)
    name = name.split(" ")
    print(name[0])
    # query = db.session.query( Students.first_name,Students.last_name,Grades.grade).\
    #     join(Grades).\
    #     filter(Students.id == Grades.student_id,Students.first_name == name[0],Students.last_name == name[1])
    # print(query.grades_grade)
    # for i in query:
    #     print(i)
    # query.grade = dict["StuGrade"]
    
    # db.session.commit()

    student = Students.query.filter_by(first_name=name[0], last_name=name[1]).first()
    result = Grades.query.filter_by(student_id=student.id).first()

    result.grade=grade
    db.session.commit()
    # print(query.grade)
    # query = grades_to_dict(result)

    # for i in query:
    #     print(i)
    # print(query.grade)
    # return render_template('showClassGrades.html',data=query,className= 3)
    return 0

#class grades
@app.route('/classGrades/<id>',methods = ['GET'])
def showClass(id):
    print(id)

    #query
    query = db.session.query( Students.first_name,Students.last_name,Grades.grade).\
        join(Grades).\
        filter(Students.id == Grades.student_id)
        # filter(Classes.prof_id == id)
            # group_by(Classes.class_name)
    
    query = grades_to_dict(query)

    courseName = str(Classes.class_name)
    for i in query:
        print(i)
    return render_template('showClassGrades.html',data=query,className= id)

    if(request.method == "GET"):
        print("hello there")
        # return redirect('showClassGrades')
        return render_template('showClassGrades.html')


# Student View Courses
@app.route('/student/<id>', methods=['GET'])
def student_schedule(id):

    # Query Student's in Grades to find Classes
    grades = Grades.query.filter_by(student_id=id)

    if(request.method == 'GET'):
        # Query the Student's Classes 
        courses = []
        for grade in grades:
            courses.append(Classes.query.filter_by(id=grade.class_id).first())
        data = courses_to_dict(courses)
        
        # Return query as dictionary
        return render_template('student.html', data=data)

    elif(request.method == 'POST'):
        # Query all the classes
        courses = [[]]
        for grade in grades:
            courses.append(Classes.query.all())
        data = courses_to_dict(courses)

    # student = Students(4, "Li", "Cheng")
    # db.session.add(student)
    # db.session.commit()
    # student = Students.query.filter_by(first_name="John").first()
    # course = Classes.query.filter_by(class_name="Math 101").first()
    # grade = Grades(4,student,course,77)
    # db.session.add(grade)
    # db.session.commit()

# Convert the student grades from objects to dictionary (for JSON)
def grades_to_dict(list):
    output = []
    for gradesData in list:
        c = {}
        c["studentName"] = gradesData.first_name + " " + gradesData.last_name
        c["grades"] = gradesData.grade
        
        output.append(c)
    return output

# Convert the professor classes from objects to dictionary (for JSON)
def prof_to_dict(list):
    output = []
    for profData in list:
        c = {}
        c["id"] = profData.id
        c["className"] = profData.class_name
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