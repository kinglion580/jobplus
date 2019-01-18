from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, Length
from jobplus.models import db, User


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
