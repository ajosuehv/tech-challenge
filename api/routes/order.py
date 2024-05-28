from flask import Blueprint, jsonify, request
from api.repositories.order import OrderRepository

order_blueprint = Blueprint('order_blueprint', __name__,
                             url_prefix='/api/')


@order_blueprint.route('/orders', methods=['post'])
def create_order():
    body = request.get_json()
    response = OrderRepository.set_order(body)
    
    return response.as_dict()