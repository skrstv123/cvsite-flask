from flask import render_template,request,Blueprint, redirect, url_for
from assets.models import Portfolio
core = Blueprint('core',__name__)

@core.route('/')
def index():
    # return render_template('index.html')
    return redirect(url_for("users.register"))

# @core.route('/checkdb')
# def cdb():
#     return '<br>'.join(str(vars( Portfolio.query.all()[0])).split(','))
