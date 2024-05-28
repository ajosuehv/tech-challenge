from flask import Blueprint, jsonify, request
from api.repositories.inventory import InventoryRepository
inventory_blueprint = Blueprint('inventory_blueprint', __name__,
                                url_prefix='/api/')


@inventory_blueprint.route('/inventories/product/<int:product_id>', methods=['PATCH'])
def update_inventory(product_id):
    body = request.get_json()
    inventory = InventoryRepository.add_inventory(product_id,body)
    return inventory.as_dict()
