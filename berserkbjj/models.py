from datetime import datetime
from . import db
from sqlalchemy.dialects.postgresql import ARRAY

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    image = db.Column(db.String(60), nullable=False)
    producttype = db.Column(db.String(60), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500), nullable=False)

    orders = db.relationship("Order", back_populates="products")

    def __repr__(self):
        str = "Id: {}, Name: {}, Image: {}, Product Type: {}, Cost: {}, Description: {}\n"
        return str.format(self.id, self.name, self.image, self.producttype, self.cost, self.description)

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    shippingaddress = db.Column(db.String(128))
    
    totalcost = db.Column(db.Float)
    date = db.Column(db.DateTime)

    products = db.relationship("Product", back_populates="orders")
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    def __repr__(self):
        str = "id: {}, Status: {}, Firstname: {}, Surname: {}, Email: {}, Phone: {}, Shipping Address: {},Total Cost: {}, Date: {}\n"
        return str.format(self.id, self.status, self.firstname, self.surname, self.email, self.phone, self.shippingaddress, self.totalcost, self.date)
