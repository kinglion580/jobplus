from flask import Blueprint, render_template, flash
from jobplus.forms import RegisterForm

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
    return render_template('register.html', form=form)
