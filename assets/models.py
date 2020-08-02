from assets import app, login_manager, db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

# function which generates current_user variable
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), unique=True,  index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    portfolio = db.relationship('Portfolio', backref='owner', lazy=True, uselist = False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def match_password(self, password):
        return check_password_hash(self.password_hash, password)

class Portfolio(db.Model):
    users = db.relationship(User)
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128), default="Your Name")
    header = db.Column(db.Text, )
    profile_pic = db.Column(db.String(64), nullable=False, default='ico.jpg')
    username = db.Column(db.String(64), db.ForeignKey('users.username'), nullable=False)

    # education 
    level1 = db.Column(db.Text, )
    institute1 = db.Column(db.Text, )
    grade1 = db.Column(db.Text, )

    level2 = db.Column(db.Text,)
    institute2 = db.Column(db.Text, )
    grade2 = db.Column(db.Text, )

    level3 = db.Column(db.Text,)
    institute3 = db.Column(db.Text, )
    grade3 = db.Column(db.Text,)

    # skills 
    skills = db.Column(db.String(128), )
    
    # projects 

    pro_title1 = db.Column(db.String(32),)
    pro_desc1 = db.Column(db.String(64),)
    pro_link1 = db.Column(db.String(512),)

    pro_title2 = db.Column(db.String(32),)
    pro_desc2 = db.Column(db.String(64),)
    pro_link2 = db.Column(db.String(512),)

    pro_title3 = db.Column(db.String(32),)
    pro_desc3 = db.Column(db.String(64),)
    pro_link3 = db.Column(db.String(512),)

    pro_title4 = db.Column(db.String(32),)
    pro_desc4 = db.Column(db.String(64),)
    pro_link4 = db.Column(db.String(512),)

    # work exp
    catg1 = db.Column(db.String(32),)
    title1 = db.Column(db.String(64),)
    desc1 = db.Column(db.String(128),)

    catg2 = db.Column(db.String(32),)
    title2 = db.Column(db.String(64),)
    desc2 = db.Column(db.String(128),)

    resume = db.Column(db.String(512),default="")

    # social media links
    fb = db.Column(db.String(512),)
    twt = db.Column(db.String(512),)
    ig = db.Column(db.String(512),)
    lkn = db.Column(db.String(512),)

    def __init__(self, *args):
        self.name, self.header, self.profile_pic, self.username, self.level1, self.institute1, self.grade1, self.level2, self.institute2, self.grade2, self.level3, self.institute3, self.grade3, self.skills, self.pro_title1, self.pro_desc1, self.pro_link1, self.pro_title2, self.pro_desc2, self.pro_link2, self.pro_title3, self.pro_desc3, self.pro_link3, self.pro_title4, self.pro_desc4, self.pro_link4, self.catg1, self.title1, self.desc1, self.catg2, self.title2, self.desc2,self.resume, self.fb, self.twt, self.ig, self.lkn = args   
        