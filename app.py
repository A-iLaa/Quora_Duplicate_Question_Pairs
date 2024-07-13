from flask import Flask,render_template,url_for,redirect
from form import PredictForm
import helper
import joblib

model = joblib.load("model.joblib")

app=Flask(__name__)

app.config["SECRET_KEY"]="secret_key"

@app.route("/")
@app.route("/home")
def home():
   return render_template("home.html",title="Quora Duplicate Question Pair Predictor")


@app.route("/predict",methods=["GET","POST"])
def predict():
    form = PredictForm()
    q1=form.q1.data
    q2=form.q2.data
    if form.validate_on_submit():
        new_data=helper.query_point_creator(q1,q2)
        result = model.predict(new_data)[0]
        if result == 0:
            return render_template("not_duplicate.html")
        else :
            return render_template("duplicate.html")
    return render_template("predict.html",title="Predict Page",form=form)
        
if __name__=="__main__":
    app.run(debug=True)