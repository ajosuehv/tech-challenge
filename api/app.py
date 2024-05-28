from flask import Flask
from api.routes.healthcheck import healthcheck_blueprint
from api.routes.product import product_blueprint
from api.routes.inventory import inventory_blueprint
from api.routes.order import order_blueprint
from flask_migrate import Migrate
from api.database import db


from api.config import Config


def create_app():    
    app = Flask(__name__)        
    app.config.from_mapping(
        SECRET_KEY = "cZrUKitc5Ifczw4Jml0aNIESUwFTG0nxEIII6HurvsrgwQtXLV1CZa02z8kw5rub"
    )     
    
    app.config.from_object(Config)    
    
    # Database and Migrations
    db.init_app(app)

    from api.models.inventory import Inventory
    from api.models.order import Order
    from api.models.order_item import OrderItem
    from api.models.product import Product

    migrate = Migrate(app, db)

    app.register_blueprint(healthcheck_blueprint)
    app.register_blueprint(product_blueprint)
    app.register_blueprint(inventory_blueprint)
    app.register_blueprint(order_blueprint)

    return app