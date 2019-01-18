from flask import Blueprint, render_template
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
    return render_template('register.html', form=form)

