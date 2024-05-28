from flask import Blueprint, jsonify

healthcheck_blueprint = Blueprint('healthcheck_blueprint', __name__)


@healthcheck_blueprint.route('/health-check', methods=['GET'])
def health_check():
    return jsonify({"message": "Process running!"})
