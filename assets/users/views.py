from assets import db
from assets.users.forms import (RegistrationForm, LoginForm, 
                                PassForm, DeleteForm)
from assets.models import Portfolio, User
from flask import (render_template, url_for,
                   flash, redirect, 
                   request, Blueprint)

from flask_login import (login_user, current_user,
                         logout_user, login_required)

from werkzeug.security import generate_password_hash

users = Blueprint('users', __name__)

@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("cv.mainform"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.match_password(form.password.data) :
    
            login_user(user)
            flash('Logged in successfully.')
            
            return redirect(url_for("cv.mainform"))
        else:
            flash("login failed, credentials do not match")
    return render_template('login.html', form=form)

@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("cv.mainform"))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        user_data = Portfolio("", "", "",str(form.username.data).strip(), "", "", "", "", "", "", "", "", "", "",  "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "","")
        db.session.add_all([user, user_data])
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)

@users.route("/change_password", methods=['GET', 'POST'])
@login_required
def change_password():
    if not current_user.is_authenticated:
        return redirect(url_for("users.login"))
    form = PassForm()
    if form.validate_on_submit():
        current_user.password_hash = generate_password_hash(form.password.data)
        db.session.commit()
        flash("Password changed successfully!")
    return render_template("change_pass.html", form=form)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('core.index'))

@users.route("/delete_account", methods=['GET', 'POST'])
@login_required
def delete_account():
    form = DeleteForm()
    if form.validate_on_submit():
        pfolio = Portfolio.query.filter_by(username = current_user.username).first()
        user = User.query.filter_by(username = current_user.username).first()
        db.session.delete(pfolio)
        db.session.delete(user)
        db.session.commit()
        logout_user()
        flash("account deleted suucessfully!")
        return redirect(url_for('users.register'))

    return render_template("delete_account.html", form=form)