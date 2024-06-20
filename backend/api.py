from flask import Blueprint

api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route('/u/<id>/m', methods=['GET'])
def mynotes(id: str):
    pass

@api_bp.route('/n/n', methods=['POST'])
def new():
    pass

@api_bp.route('/n/<id>', methods=['GET'])
def get(id: str):
    pass

@api_bp.route('/n/<id>', methods=['PUT'])
def put(id: str):
    pass

@api_bp.route('/n/<id>', methods=['DELETE'])
def delete(id: str):
    pass