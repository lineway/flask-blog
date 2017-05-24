# coding:utf-8
__author__ = 'Piels'

from flask import Blueprint
from flask import redirect, url_for, flash, render_template
from webapp.forms import LoginForm, RegisterForm
from webapp.models import db, User


main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates/main',
)


@main_blueprint.route('/')
def index():
    return redirect(url_for('blog.home'))


@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash("You have been logged out.", category='success')
        return redirect(url_for('.home'))


@main_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    flash("You have been logged out.", category='success')
    return redirect(url_for('.home'))


@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form  = RegisterForm()

    if form.validate_on_submit():
        new_user = User()
        new_user.username = form.username.data
        new_user.set_password(form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash("Your user has been created, please login.", category='success')
        return redirect(url_for('.login'))
    return render_template('register.html', form=form)
