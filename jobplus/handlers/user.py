from flask import Blueprint, render_template, flash, redirect, url_for
from jobplus.models import User
from jobplus.forms import UserProfileForm
from flask_login import current_user, login_required

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/<int:user_id>')
def profile(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user/profile.html', user=user)

@login_required
@user.route('/profile', methods=['GET', 'POST'])
def update_profile():
    form = UserProfileForm(obj=current_user)
    if form.validate_on_submit():
        form.update_profile(current_user)
        flash('个人信息更新成功', 'success')
        return redirect(url_for('front.index'))
    return render_template('user/update_profile.html', form=form)