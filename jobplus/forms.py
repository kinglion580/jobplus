from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, Length
from jobplus.models import db, User, Company


class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Email(message='邮箱格式不对')])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 24, message='密码长度要在 6～24 个字符之间')])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱为注册')

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')


class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    email = StringField('邮箱', validators=[DataRequired(), Email(message='邮箱格式不对')])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 24, message='密码长度要在 6～24 个字符之间')])
    repeat_password = PasswordField('重复密码', validators=[DataRequired(), Length(6, 24, message='密码长度要在 6～24 个字符之间')])
    submit = SubmitField('提交')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已被注册')

    def create_user(self):
        user = User(username=self.username.data, email=self.email.data, password=self.password.data)
        db.session.add(user)
        db.session.commit()
        return user


class UserProfileForm(FlaskForm):
    username = StringField('用户名', [DataRequired()])
    real_name = StringField('姓名')
    email = StringField('邮箱', validators=[DataRequired(), Email(message='邮箱格式不对')])
    phone = StringField('手机号')
    work_years = IntegerField('工作年限')
    submit = SubmitField('提交')

    def validate_phone(self, field):
        if len(field.data) != 11:
            raise ValidationError('请输入有效手机号')

    def update_profile(self, user):
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()


class CompanyProfileForm(FlaskForm):
    username = StringField('企业名称')
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    phone = StringField('手机号')
    location = StringField('地址', validators=[Length(0, 64)])
    site = StringField('公司网站', validators=[Length(0, 64)])
    logo = StringField('Logo')
    description = StringField('一句话描述', validators=[Length(0, 100)])
    about = TextAreaField('公司详情', validators=[Length(0, 1024)])
    submit = SubmitField('提交')

    def validate_phone(self, field):
        phone = field.data
        if phone[:2] not in ('13', '15', '18') and len(phone) != 11:
            raise ValidationError('请输入有效的手机号')

    def update_profile(self, user):
        user.username = self.username.data
        user.email = self.email.data

        if user.detail:
            detail = user.detail
        else:
            detail = Company()
            detail.user_id = user.id
            detail.contact = 'x'
        self.populate_obj(detail)
        db.session.add(user)
        db.session.add(detail)
        db.session.commit()


