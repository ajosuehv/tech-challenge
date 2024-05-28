import factory
from factory.faker import faker
import uuid
from api.models.product import Product

class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Product
    name = faker.Faker().nic_handle()
    price = 10.0
    cost = 5.0
    sku = faker.Faker().uuid4()
    