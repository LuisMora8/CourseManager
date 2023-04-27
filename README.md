# Course Management System

This is a web application built using Flask, Flask-SQLAlchemy, Flask-Admin, JavaScript, HTML, and CSS that serves as a course management system for students, professors, and administrators. The application allows students to view their courses and add/remove classes, professors to view the courses they will teach and change students' grades, and administrators to edit/delete/create records from the database.

## Requirements
To run this application, you will need to have the following installed on your machine:

Python 3
Flask
Flask-SQLAlchemy
Flask-Admin

## Installation
1. Clone the repository:
<pre><code>git clone https://github.com/LuisMora8/CourseManager
</code></pre>
2. Navigate to the project directory:
<pre><code>cd course-management-system
</code></pre>
3. Create and activate a virtual environment:
<pre><code>python3 -m venv course-management-venv
source course-management-venv/bin/activate
</code></pre>
4. Install the dependencies:
<pre><code>pip install -r requirements.txt
</code></pre>
5. Run the application:
<pre><code>flask run
</code></pre>
6. Open your browser and go to http://localhost:5000/ to view the application.

## Usage
### Student
Go to the login page and enter your username and password.
Once logged in, you will be redirected to the home page where you can view your courses and add/remove classes.
###  Professor
Go to the login page and enter your username and password.
Once logged in, you will be redirected to the home page where you can view the courses you will teach and change students' grades.
### Administrator
Go to the login page and enter your username and password.
Once logged in, you will be redirected to the admin page where you can edit/delete/create records from the database.

## Tech Stack
Flask for the back-end framework
Flask-SQLAlchemy for the database ORM
Flask-Admin for the admin interface
JavaScript for dynamic web page features
AJAX to create an API with the database
HTML and CSS for the static webpage features.
