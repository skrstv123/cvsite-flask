from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

class MainForm(FlaskForm):

    name = StringField('NAME',validators=[DataRequired()])
    header = TextAreaField('SHORT BIO', validators = [DataRequired()])
    profile_pic = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])

    # education 
    level1 = StringField('education level',)
    institute1 = StringField('Institite name',)
    grade1 = StringField('describe your grades',)

    level2 = StringField('education level',)
    institute2 = StringField('Institite name',)
    grade2 = StringField('describe your grades',)

    level3 = StringField('education level',)
    institute3 = StringField('Institite name',)
    grade3 = StringField('describe your grades',)

    # skills 
    skills = StringField('skills',)

    # projects 
    pro_title1 = StringField('PROJECT TITLE',)
    pro_desc1 = TextAreaField('describe', )
    pro_link1 = StringField('demo link',)

    pro_title2 = StringField('PROJECT TITLE',)
    pro_desc2 = TextAreaField('describe', )
    pro_link2 = StringField('demo link',)

    pro_title3 = StringField('PROJECT TITLE',)
    pro_desc3 = TextAreaField('describe', )
    pro_link3 = StringField('demo link',)

    pro_title4 = StringField('PROJECT TITLE',)
    pro_desc4 = TextAreaField('describe', )
    pro_link4 = StringField('demo link',)

    # work exp
    catg1 = StringField('JOB CATEGORY',)
    title1 = StringField('JOB TITLE',)
    desc1 = TextAreaField('describe', )

    catg2 = StringField('JOB CATEGORY',)
    title2 = StringField('JOB TITLE',)
    desc2 = TextAreaField('describe', )

    resume = FileField('Upload single-page resume', validators=[FileAllowed(['pdf', 'jpg'])])

    # social media links
    fb = StringField('facebook profile link:',)
    twt = StringField('twitter profile link:',)
    ig = StringField('instagram profile link:',)
    lkn = StringField('linkedin profile link:',)

    Submit = SubmitField("submit")
