import os

import pytest

from dotenv import load_dotenv
from api.app import create_app
from api.database import db
from api.models.product import Product
from api.models.inventory import Inventory



load_dotenv('../env/db.dotenv')

# --------
# Fixtures
# --------

@pytest.fixture(scope='module')
def new_product():
    product = Product('Product Name',1000.0,1500.0)
    return product

@pytest.fixture(scope='module')
def new_inventory():
    inventory = Inventory(1)
    return inventory


@pytest.fixture(scope='module')
def test_client():
    # Set the Testing configuration prior to creating the Flask application
    # os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!

