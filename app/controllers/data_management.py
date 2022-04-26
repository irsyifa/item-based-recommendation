from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import current_user, login_required
from app.libraries.data import dump_data
from app.models import Rating
from app.libraries.recommender import get_recommendation

dataManager = Blueprint('datamanagement', __name__)
@dataManager.route("submit", methods=["POST"])
@login_required
def submit():
    if current_user.is_authenticated:
        user_id = current_user.get_id() 
        produk = request.form.get("produk")
        rate = request.form.get("rate")
        data = Rating(
            userId = user_id,
            itemId = produk, 
            rating =rate
        )
        data.save()
        return redirect(url_for('usermanagement.index'))
    else:
        return redirect(url_for('usermanagement.index'))

@dataManager.route("dump", methods=["POST"])
def dump():
    data = dump_data()
    for i in data:
        rate = Rating(
            userId=str(i["userId"]),
            itemId=i["itemId"],
            rating=i["rating"]
        )
        rate.save()
    
    return render_template("index.html")


@dataManager.route("recommendation", methods=["GET"])
@login_required
def recommendation():
    if current_user.is_authenticated:
        user_id = current_user.get_id() 
        ratings = Rating.objects.all()
        ratings = [i.to_mongo() for i in ratings]
        try:
            last_viewed, recs, col_recs= get_recommendation(user_id, ratings)
        except:
            last_viewed = []
            recs = []
            col_recs = []

        return render_template('index.html', last_viewed=last_viewed, recs=recs, colrecs=col_recs)