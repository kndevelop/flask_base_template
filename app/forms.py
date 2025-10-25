from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class UserForm(FlaskForm):
    name = StringField(
        "名前",
        validators=[
            DataRequired(message="名前は必須です"),
            Length(max=16, message="名前は16文字以内で入力してください")
        ]
    )
    age = IntegerField(
        "年齢",
        validators=[
            DataRequired(message="年齢は必須です"),
            NumberRange(min=0, max=999, message="年齢は0〜999の範囲で入力してください")
        ]
    )
    submit = SubmitField("追加")