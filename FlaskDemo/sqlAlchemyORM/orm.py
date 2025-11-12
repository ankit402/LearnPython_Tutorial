from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "some_secret_key"

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # ✅ simplified column name
    name = db.Column("name", db.String(100),nullable=False)
    age = db.Column("age", db.Integer,nullable=False)
    gender = db.Column("gender", db.String(100),nullable=False)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

#Students.query.all()
@app.route("/")
def show_all():
    return render_template('show_all.html', students=Student.query.all())


@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        # ✅ Input validation
        if not name or not age or not gender:
            flash("Please enter all the fields.", "error")
        else:
            try:
                age = int(age)
                new_student = Student(name, age, gender)
                db.session.add(new_student)
                db.session.commit()
                flash("Record added successfully!", "success")
                return redirect(url_for("show_all"))
            except ValueError:
                flash("Age must be a number.", "error")
    return render_template("new.html")

@app.route('/delete/<int:id>', methods=["GET", "POST"])
def delete_student(id):
    student = Student.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()
        flash(f"Student {student.name} deleted successfully!", "success")
    else:
        flash("Student not found.", "error")
    return redirect(url_for('show_all'))

@app.route('/edit/<int:id>', methods=["GET", "POST"])
def edit_student(id):
    student = Student.query.get(id)
    if not student:
        flash("Student not found.", "error")
        return redirect(url_for('show_all'))

    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        if not name or not age or not gender:
            flash("Please fill all fields.", "error")
        else:
            try:
                student.name = name
                student.age = int(age)
                student.gender = gender
                db.session.commit()
                flash("Student updated successfully!", "success")
                return redirect(url_for('show_all'))
            except ValueError:
                flash("Age must be a number.", "error")
    return render_template("edit.html", student=student)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug = True)