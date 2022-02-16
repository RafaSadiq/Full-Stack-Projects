from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'customer.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), unique=False)
    lname = db.Column(db.String(50), unique=False)
    
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
class CustomerSchema(ma.Schema):
    class Meta:
        fields = ('fname', 'lname')
        
customer_schema=CustomerSchema()
customers_schema=CustomerSchema(many=True)


@app.route('/people')
def home():
    return render_template('index.html')

@app.route('/customer', methods=["POST"])
def add_customer():
    fname = request.json['fname']
    lname = request.json['lname']
    
    new_customer = Customer(fname, lname)
    db.session.add(new_customer)
    db.session.commit()
    customer = Customer.query.get(new_customer.id)
    return customer_schema.jsonify(customer)

@app.route('/customers', methods=["GET"])
def get_peoples():
    all_customers = Customer.query.all()
    results = customers_schema.dump(all_customers)
    return jsonify(results)

@app.route('/', methods=["GET"])
def get_customers():
    all_customers = Customer.query.all()
    results = customers_schema.dump(all_customers)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
    
    

