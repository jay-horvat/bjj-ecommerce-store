from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
app=Flask(__name__)

def create_app():
    app.debug=True
    app.secret_key='BerserkSecret321'

    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///berserkbjj.sqlite'

    db.init_app(app)

    bootstrap = Bootstrap(app)
    
    from . import views
    app.register_blueprint(views.bp)
   
    return app
