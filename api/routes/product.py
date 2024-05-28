from flask import Blueprint, jsonify, request

from api.models.product import Product
from api.repositories.product import ProductRepository

product_blueprint = Blueprint('products',
                             __name__,
                             url_prefix='/api/')

@product_blueprint.route('products',
                        methods=['POST'])
def create_product():
    body = request.get_json()
    response = ProductRepository.new_product(body)
    if response is None:
        return jsonify({'info': 'No data'}), 404
    return response.as_dict(), 200
