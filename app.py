from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import Students, Grades, Classes, Professor, Login, app, db

# # Flask and SQLDatabase configuaration
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///students.sqlite"
# db = SQLAlchemy(app)


# Home Page
#@app.route('/')
#def index():
#    return render_template('student.html')

@app.route('/')
def student_schedule():
    db.session.drop()
    # prof =  Professor('Ammon', 'Hepworth');
    # db.session.add(prof);
    # db.session.commit();
    return render_template('student.html')
    

# Driver Code
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)