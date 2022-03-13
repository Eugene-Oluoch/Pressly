#imports
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField,SubmitField
from wtforms.validators import DataRequired, Length


#Post Creation Form
class PostForm(FlaskForm):
    title = StringField("title", validators=[DataRequired(),Length(min=2)],render_kw={"placeholder": "Title"})
    content = TextAreaField("Content", validators=[DataRequired(), Length(min=10)],render_kw={"placeholder": "What is the blog about"})
    picture = FileField('image', validators=[FileAllowed(['jpg','png','jpeg'])])
    submit = SubmitField("Publish")
    
#Form to Update Already existing Forms
class UpdatePost(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Title', validators=[DataRequired()])
    submit = SubmitField('Update')