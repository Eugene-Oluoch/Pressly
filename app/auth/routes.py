#imports
from flask import Blueprint, render_template, url_for, flash, redirect
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt
from app.models import User
from app.auth.forms import Register,Login,UpdateForm
from app.auth.utils import save_picture


#Blueprint Intialization
auths = Blueprint('users', __name__)


#Register route
@auths.route('/register', methods=['GET','POST'])
def register():
    form = Register()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user_create = User(name=form.name.data,email=form.email.data,password=password_hash,bio="Tell us about yourself")
        db.session.add(user_create)
        db.session.commit()
        flash(f"Account created for {form.name.data}")
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)


#Login Route
@auths.route('/login', methods=['GET','POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("You have successfully logged in.")
            return redirect(url_for('main.home'))
    return render_template('login.html', form=form)


#User profile Route
@auths.route('/profile',methods=['GET','POST'])
@login_required
def profile():
    user  = User.query.filter_by(email=current_user.email).first()
    form = UpdateForm()
    if form.validate_on_submit():
        if form.profile_pic:
            picture_file = save_picture(form.profile_pic.data)
            current_user.image_file = picture_file
        current_user.name = form.name.data
        current_user.email = form.email.data
        current_user.bio = form.bio.data
        db.session.commit()
        flash('Account updated successfully.')
        return redirect(url_for('users.profile'))
    form.name.data = user.name
    form.email.data = user.email
    form.bio.data = user.bio
    image_file = url_for('static',filename=f'images/{current_user.image_file}')
    return render_template('profile.html', form=form, image=image_file, user=user)


#Logout Route
@auths.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))
    