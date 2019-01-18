from flask import Blueprint, render_template, flash, redirect, url_for
from jobplus.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user
from jobplus.models import db, User

front = Blueprint('front', __name__)


@front.route('/')
def index():
    return render_template('index.html')


@front.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功，请登录', 'success')
        return redirect(url_for('.login'))
    return render_template('register.html', form=form)


@front.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user, form.remember_me.data)
        flash('登录成功', 'success')
        return redirect(url_for('.index'))
    return render_template('login.html', form=form)


@front.route('/logout')
def logout():
    logout_user()
    flash('您已经退出登录', 'success')
    return redirect(url_for('.index'))


@front.route('/companyregister', methods=['GET', 'POST'])
def companyregister():
    form = RegisterForm()
    form.username.label = u'企业名称'
    if form.validate_on_submit():
        company_user = form.create_user()
        company_user.role = User.ROLE_COMPANY
        db.session.add(company_user)
        db.session.commit()
        flash('注册成功，请登录', 'success')
        return redirect(url_for('.login'))
    return render_template('companyregister.html', form=form)