from flask import Blueprint, flash, redirect, url_for, render_template
from jobplus.forms import CompanyProfileForm
from flask_login import current_user

company = Blueprint('company', __name__, url_prefix='/company')

@company.route('/profile', methods=['GET', 'POST'])
def update_profile():
    form = CompanyProfileForm(obj=current_user)
    if form.validate_on_submit():
        form.update_profile(current_user)
        flash('企业信息更新成功', 'success')
        return redirect(url_for('front.index'))
    return render_template('company/update_profile.html', form=form)