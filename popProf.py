from app import db
from models import Students, Grades, Classes, Professor, Login, app, db
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

people = Professor.query.all()
for i in people:
    print(i)