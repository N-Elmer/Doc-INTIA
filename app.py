import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = os.path.join(project_dir, "bd/database.db")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Customer(db.Model):
    name = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Name: {}>".format(self.name)

class Insurance(db.Model):
    policy = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Policy: {}>".format(self.policy)


@app.route("/", methods=["GET", "POST"])
def home():
    customers = None
    if request.form:
        try:
            customer = Customer(name=request.form.get("name"))
            db.session.add(customer)
            db.session.commit()
        except Exception as e:
            print("Failed to add customer")
            print(e)
    customers = Customer.query.all()
    return render_template("home.html", customers=customers)


@app.route("/update", methods=["POST"])
def update():
    try:
        newname = request.form.get("newname")
        oldname = request.form.get("oldname")
        customer = Customer.query.filter_by(name=oldname).first()
        customer.name = newname
        db.session.commit()
    except Exception as e:
        print("Couldn't update customer name")
        print(e)
    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete():
    name = request.form.get("name")
    customer = Customer.query.filter_by(name=name).first()
    db.session.delete(customer)
    db.session.commit()
    return redirect("/")

@app.route("/insurance", methods=["GET", "POST"])
def insurance():
    insurances = None
    if request.form:
        try:
            insurance = Insurance(policy=request.form.get("policy"))
            db.session.add(insurance)
            db.session.commit()
        except Exception as e:
            print("Failed to add insurance")
            print(e)
    insurances = Insurance.query.all()
    return render_template("home.html", insurances=insurances)

@app.route("/update_insurance", methods=["POST"])
def update_insurance():
    try:
        newpolicy = request.form.get("newpolicy")
        oldpolicy = request.form.get("oldpolicy")
        insurance = Insurance.query.filter_by(policy=oldpolicy).first()
        insurance.policy = newpolicy
        db.session.commit()
    except Exception as e:
        print("Couldn't update insurance policy")
        print(e)
    return redirect("/")

@app.route("/delete_insurance", methods=["POST"])
def delete_insurance():
    policy = request.form.get("policy")
    insurance = Insurance.query.filter_by(policy=policy).first()
    db.session.delete(insurance)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
