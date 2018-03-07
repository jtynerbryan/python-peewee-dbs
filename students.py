from peewee import *

db = SqliteDatabase('students.db')

class BaseModel(Model):
    """A base model that will use our Sqlite3 database"""
    class Meta:
        database = db

class Student(BaseModel):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)

students = [
    {'username': 'jesse tyner-bryan',
     'points': 10000
    },
    {'username': 'john tyner',
     'points': 12948
    },
    {'username': 'blah blah guy',
     'points': 12948
    }
]

def add_students(students):
    for student in students:
        try:
            Student.create(username=student['username'], points=student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()

def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student

if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students(students)
    print(f'Our top student right now is {top_student().username}')
