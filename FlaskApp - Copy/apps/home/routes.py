# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from Demos.win32ts_logoff_disconnected import username
from apps import db, login_manager
from apps.authentication.models import Users
from apps.home import blueprint
from flask import render_template, request ,flash ,url_for, redirect
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound


@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')

@blueprint.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    if request.method == "POST":

        current_user.firname = request.form.get("firstname")
        current_user.lastname  = request.form.get("lastname")
        current_user.phone     = request.form.get("phone")
        current_user.address1   = request.form.get("address")
        current_user.address2  = request.form.get("address2")
        current_user.gender    = request.form.get("gender")
        current_user.dob       = request.form.get("dob")
        current_user.information     = request.form.get("about")

        db.session.commit()
        flash("Profile updated successfully!", "success")
        return redirect(url_for('home_blueprint.profile'))
    flash("Profile updated failed!", "error")
    return render_template("home/profile.html")





@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):
    try:
        segment = request.path.split('/')[-1]
        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
