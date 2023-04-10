from app import db, Professor
prof1 = Professor(prof_numkey = 1,prof_name = "Angelo kyrilov", class_numkey = 2)
prof2 = Professor(prof_numkey = 2,prof_name = "Santosh Chandrasekhar", class_numkey = 3)

# student1 = User(name='Erick Vargas', grade= 45.3)
# student2 = User(name='Abel Getachew', grade=12.2)
db.session.add(prof1)
db.session.add(prof2)
db.session.commit()