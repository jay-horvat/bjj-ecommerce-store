from flask import Blueprint, render_template, request
from .models import Product, Order
from datetime import datetime
from .forms import CheckoutForm
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products = products)

@bp.route('/product/<int:productid>/')
def returnproduct(productid):
    products = Product.query.filter(Product.id == productid)
    return render_template('product.html', products = products)

@bp.route('/checkout', methods=['POST','GET'])
def checkout():
    form = CheckoutForm()
    
    if form.validate_on_submit():
            
            order = Order(
                status=False,
                firstname=form.firstname.data,
                surname=form.surname.data,
                email=form.email.data,
                phone=form.phone.data,
                shippingaddress=form.shippingaddress.data,
                totalcost=0,
                date=datetime.now(),
                product_id = request.values.get('product_id')
            )
            #order.products.append(product)
            db.session.add(order)
            db.session.commit()

    return render_template('checkout.html', form=form)

