from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Flask and SQLDatabase configuaration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://grades.sqlite"
db = SQLAlchemy(app)


# Database Grades mode
# LAB7 EXAMPLE
class Grades(db.Model):
    name = db.Column(db.String, unique=True, primary_key=True, nullable=False)
    grade = db.Column(db.String)

    def __init__(self, name, grade) -> None:
        super().__init__()
        self.name = name
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