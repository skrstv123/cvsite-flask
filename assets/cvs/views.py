from assets import db
from assets.cvs.forms import MainForm
from assets.models import Portfolio
from assets.cvs.picture import add_profile_pic
from assets.cvs.cv import add_cv
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required

cv = Blueprint('cv', __name__)

@cv.route("/mainform", methods=["GET", "POST"])
@login_required
def mainform():
    if not current_user.is_authenticated:
        return redirect(url_for("users.login"))
    form = MainForm()
    row = Portfolio.query.filter_by(username=current_user.username).first()
    # print("pic name:",row.profile_pic)

    if form.validate_on_submit():
        if form.profile_pic.data:
            row.profile_pic = add_profile_pic(
                form.profile_pic.data, 
                current_user.username
                )

        if row.profile_pic.strip()=="":
            row.profile_pic = "ico.jpg"

        if form.resume.data:
            row.resume = add_cv(
                form.resume.data, 
                current_user.username
            )
            print(row.resume)
        
        row.name= str(form.name.data ).strip()
        row.header = str(form.header.data).strip()
        # row.profile_pic = form.profile_pic.data.filename if form.profile_pic.data else "ico.jpg"
        row.username = current_user.username

        row.level1=str(form.level1.data).strip()
        row.institute1 = form.institute1.data
        row.grade1 = form.grade1.data
        row.level2=str(form.level2.data).strip()
        row.institute2 = form.institute2.data
        row.grade2 = form.grade2.data
        row.level3=str(form.level3.data).strip()
        row.institute3 = form.institute3.data
        row.grade3 = form.grade3.data

        row.skills = str(form.skills.data).strip()

        row.pro_title1 = str(form.pro_title1.data).strip()
        row.pro_desc1 = form.pro_desc1.data
        row.pro_link1 = form.pro_link1.data
        row.pro_title2 = str(form.pro_title2.data).strip()
        row.pro_desc2 = form.pro_desc2.data
        row.pro_link2 = form.pro_link2.data
        row.pro_title3 = str(form.pro_title3.data).strip()
        row.pro_desc3 = form.pro_desc3.data
        row.pro_link3 = form.pro_link3.data
        row.pro_title4 = str(form.pro_title4.data).strip()
        row.pro_desc4 = form.pro_desc4.data
        row.pro_link4 = form.pro_link4.data

        row.catg1 = str(form.catg1.data).strip()
        row.title1=form.title1.data
        row.desc1=form.desc1.data
        row.catg2 = str(form.catg2.data).strip()
        row.title2=form.title2.data
        row.desc2=form.desc2.data

        row.fb = form.fb.data
        row.twt = form.twt.data
        row.ig = form.ig.data
        row.lkn = form.lkn.data

        db.session.commit()
        # print(row.username)
        
        flash("data submitted successfully! check your profile at /"+str(current_user.username))

    elif request.method=='GET':
        form.name.data = row.name
        form.header.data = row.header 

        form.level1.data = row.level1
        form.institute1.data  = row.institute1
        form.grade1.data = row.grade1 
        form.level2.data = row.level2
        form.institute2.data = row.institute2 
        form.grade2.data = row.grade2
        form.level3.data = row.level3
        form.institute3.data = row.institute3
        form.grade3.data = row.grade3

        form.skills.data = row.skills

        form.pro_title1.data = row.pro_title1 
        form.pro_desc1.data = row.pro_desc1
        form.pro_link1.data=row.pro_link1 
        form.pro_title2.data=row.pro_title2
        form.pro_desc2.data=row.pro_desc2 
        form.pro_link2.data=row.pro_link2
        form.pro_title3.data=row.pro_title3
        form.pro_desc3.data=row.pro_desc3
        form.pro_link3.data=row.pro_link3
        form.pro_title4.data=row.pro_title4
        form.pro_desc4.data=row.pro_desc4 
        form.pro_link4.data=row.pro_link4 

        form.catg1.data=row.catg1
        form.title1.data=row.title1
        form.desc1.data=row.desc1
        form.catg2.data=row.catg2
        form.title2.data=row.title2
        form.desc2.data=row.desc2

        form.fb.data=row.fb
        form.twt.data=row.twt
        form.ig.data=row.ig
        form.lkn.data=row.lkn

    return render_template("main_form.html", form=form)

@cv.route("/help")
@login_required
def help():
    if not current_user.is_authenticated:
        return redirect(url_for("users.login"))
    return render_template("help.html")

@cv.route("/<username>")
def showcv(username):
    data = Portfolio.query.filter_by(username=username).all()
    if len(data)==0:
        return render_template("error_pages/404.html"),404 
    
    data = data[0]
    profile_pic = url_for('static', filename='DP/' + data.profile_pic)
    skills = [x for x in data.skills.strip().split(',') if len(x.strip())>0]
    return render_template("cv.html",profile_pic=profile_pic, skills=skills, username=username, data=data)