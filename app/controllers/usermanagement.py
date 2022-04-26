from flask import Blueprint, flash, request, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Rating
from app.libraries.data import active_data
from app.libraries.recommender import get_recommendation
from bootstrap.extensions import login as lg

user = Blueprint('usermanagement', __name__)
@user.route("login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('usermanagement.index'))

    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.objects(username=username).first()
        if user == None or user.check_password(password) == False:
            flash("Invalid username or password")
            return redirect(url_for('usermanagement.login'))
 
        remember_me = request.form.get('customCheck')
        if remember_me == "on":
            remember_me = True
        else:
            remember_me = False
        login_user(user, remember=remember_me)
        return redirect(url_for('usermanagement.index'))
    else:
        return render_template('login.html')

@user.route('logout', methods=["POST"])
def logout():
    logout_user()
    return redirect(url_for('usermanagement.login'))

@user.route('register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("usermanagement.index"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        repeat_password = request.form.get('repeat_pwd')
        if password == repeat_password and username:
            try:
                user = User(username=username)
                user.set_password(password)
                user.save()
                flash("Success")
                return redirect(url_for('usermanagement.login'))
            except:
                flash("error")
                return render_template('register.html')
        else:
            flash("error")
            return render_template('register.html')
    else:
        flash("error")
        return render_template('register.html')

@user.route('index', methods=["GET"])
@login_required
def index():
    if current_user.is_authenticated:
        user_id = current_user.get_id()
        if user_id:    
            user = User.objects(id=user_id).first()
            ratings = Rating.objects.all()
            ratings = [i.to_mongo() for i in ratings]
            available = active_data(user_id, ratings)    
            try:
                last_viewed, recs, col_recs= get_recommendation(user_id, ratings)
            except:
                last_viewed = []
                recs = []
                col_recs = []

            return render_template('index.html', username=user.username, 
                available=available, last_viewed=last_viewed, recs=recs, colrecs=col_recs)

    # return render_template('login.html')

@user.route('/', methods=["GET"])
def home():
    return redirect(url_for("usermanagement.index"))

@lg.unauthorized_handler
def unauthorized():
    return render_template("login.html")
