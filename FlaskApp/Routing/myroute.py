# Routing/myroute.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from DBContext.dbclass import db, User, Group, UserGroup, Role
from werkzeug.security import generate_password_hash ,check_password_hash

# Create a blueprint
myroute_bp = Blueprint('myroute', __name__)

@myroute_bp.route('/')
def main():
    return render_template('Login.html')

@myroute_bp.route('/home')
def home():
    if 'username' in session:
        users = User.query.all()
        groups = Group.query.all()
        return render_template('home.html', username=session['username'],groups=groups, users=users)
    else:
        flash("Please login first!", "warning")
        return redirect(url_for('myroute.main'))



@myroute_bp.route('/Login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Query user from the database
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            # Store user info in session
            session['username'] = user.username
            flash("Login Successful!", "success")
            return redirect(url_for('myroute.home'))  # redirect to home route
        else:
            flash("Invalid username or password!", "danger")
            return redirect(url_for('myroute.login'))

    # GET request renders the login page
    return render_template('Login.html')

@myroute_bp.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
        flash("Logout Successful!", "success")
        return redirect(url_for('myroute.login'))

@myroute_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        age = request.form['age']
        gender = request.form['gender']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
    #userdata = User(username, hashed_password, age='', gender='', phone='', email='')

        # Check if username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("User already exists in the database!", "warning")
            return redirect(url_for('myroute.register'))
        # Hash the password before saving
        hashed_password = generate_password_hash(password)
        # Add new user to DB
        new_user = User(username=username, password=hashed_password, age = age, gender=gender, phone=phone, email=email,address=address)
        db.session.add(new_user)
        db.session.commit()
        flash("User registered successfully!", "success")
        # Redirect to home page after registration
        return redirect(url_for('myroute.home'))
    # GET method: show registration page
    return render_template('RegisterUser.html', username=session.get('username'))


@myroute_bp.route('/show_all')
def show_all():
    # Fetch all users from the database
    groups = Group.query.all()
    users = User.query.all()
    # Fetch all groups from the database
    # Render the template and pass the fetched data and the session username
    return render_template('home.html', groups=groups, users=users,  username=session.get('username'))


@myroute_bp.route('/changepassword/<username>', methods=['GET', 'POST'])
def changepassword(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        flash("User not found!", "danger")
        return redirect(url_for('myroute.home'))
    if request.method == 'POST':
        current_password = generate_password_hash(request.form['current_password'])
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        # Check current password (assuming plain-text stored, replace with hash verify if hashed)
        if check_password_hash(user.password, (current_password)):
            flash("Incorrect current password!", "danger")
            return redirect(url_for('myroute.changepassword', username=username))
        # Ensure new and confirm match
        if new_password != confirm_password:
            flash("New passwords do not match!", "warning")
            return redirect(url_for('myroute.changepassword', username=username))
        # Update password securely
        user.password = generate_password_hash(new_password)
        db.session.commit()
        flash("Password updated successfully!", "success")
        return redirect(url_for('myroute.home'))
    # GET request — render the form
    return render_template('changepassword.html', username=username)


@myroute_bp.route('/edituser/<int:id>', methods=['GET', 'POST'])
def edituser(id):
    userdata = User.query.filter_by(id=id).first()
    if not userdata:
        flash("User not found!", "danger")
        return redirect(url_for('myroute.home'))
    if request.method == 'POST':
        userdata.age = request.form['age']
        userdata.gender = request.form['gender']
        userdata.phone = request.form['phone']
        userdata.email = request.form['email']
        db.session.commit()
        flash("User edited successfully!", "success")
        return redirect(url_for('myroute.home'))
    else:
        flash("User updation failed!", "error")
        return render_template('edituser.html', userdata=userdata)

@myroute_bp.route('/deleteuser/<int:id>', methods=['GET', 'POST'])
def deleteuser(id):
    userdata = User.query.filter_by(id=id).first()
    if userdata:
        db.session.delete(userdata)
        db.session.commit()
        flash("User Deleted successfully!", "success")
        return redirect(url_for('myroute.home'))
    else:
        flash("User Deletion Failed!", "Error")
        return redirect(url_for('myroute.home'))


@myroute_bp.route('/AddGroup/<string:username>', methods=['GET', 'POST'])
def AddGroup(username):

    if request.method == 'POST':
        groupname = request.form['groupname'].strip()
        groupdescription = request.form['groupdescription'].strip()

        # 1. Validation for empty name
        if not groupname:
            flash("Group name cannot be empty!", "danger")
            return redirect(request.url)

        # 2. Check duplicate group
        existing = Group.query.filter_by(groupname=groupname).first()
        if existing:
            flash("Group name already exists!", "warning")
            return redirect(request.url)

        try:
            # 3. Add the group safely
            new_group = Group(groupname, groupdescription)
            db.session.add(new_group)
            db.session.commit()

            flash("Group added successfully!", "success")
            return redirect(url_for('myroute.home'))

        except Exception as e:
            db.session.rollback()
            flash(f"Database error: {str(e)}", "danger")
            return redirect(request.url)

    # GET request → show page
    return render_template('AddGroup.html', username=username)

@myroute_bp.route('/GroupManagement', methods=['GET', 'POST'])
def GroupManagement():
    groups = Group.query.all()
    return render_template('AddGroup.html', groups=groups)

@myroute_bp.route('/editgroup/<int:id>', methods=['GET', 'POST'])
def editgroup(id):
    groupdata = Group.query.filter_by(id=id).first()
    if not groupdata:
        flash("Group not found!", "danger")
    else:
        groupdata.groupname = request.form['groupname']
        groupdata.groupdescription = request.form['groupdescription']
        db.session.commit()
        flash("Group edited successfully!", "success")
        return redirect(url_for('myroute.home'))

@myroute_bp.route('/deletegroup/<int:id>', methods=['GET', 'POST'])
def deletegroup(id):
    groupdata = Group.query.filter_by(id=id).first()
    if not groupdata:
        flash("Group not found!", "danger")
        return redirect(url_for('myroute.home'))
    else:
        db.session.delete(groupdata)
        db.session.commit()
        flash("Group deleted successfully!", "success")
        return redirect(url_for('myroute.home'))
