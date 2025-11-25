from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo


app = Flask(__name__)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb+srv://mauryaashishravi_db_user:G58jsEiXCu44nfuw@cluster1.v3qad6e.mongodb.net/"
mongo = PyMongo(app)
# Route for Homepage
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')
@app.route('/terms')
def terms():
    return render_template('terms.html')

# 🛠️ Only Keep This Contact Route (REMOVE the duplicate one above)
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        # Insert into MongoDB
        mongo.db.contacts.insert_one({"name": name, "email": email, "phone": phone, "message": message})

        # Redirect to Thank You page
        return redirect(url_for("thankyou"))

    return render_template("contact.html")

@app.route('/thankyou')
def thankyou():
    return render_template('thank_you.html')


if __name__ == '__main__':
    app.run(debug=True)
    
    