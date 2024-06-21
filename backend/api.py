from flask import Blueprint

class UserAPI():
    bp = Blueprint('user', __name__, url_prefix='/u')
    
    @bp.route('/', methods=['POST'])
    def add():
        pass

    @bp.route('/<id>', methods=['DELETE'])
    def delete(id):
        pass

    @bp.route('/<id>/n', methods=['GET'])
    def get_notes(id):
        pass

    @bp.route('/<id>/n', methods=['POST'])
    def add_note(id):
        pass


class NoteAPI():
    bp = Blueprint('note', __name__, url_prefix='/n')

    @bp.route('/<id>', methods=['GET'])
    def get(id):
        pass

    @bp.route('/<id>', methods=['PUT'])
    def put(id):
        pass

    @bp.route('/<id>', methods=['DELETE'])
    def delete(id):
        pass

api_bp = Blueprint('api', __name__, url_prefix='/api')
api_bp.register_blueprint(UserAPI.bp)
api_bp.register_blueprint(NoteAPI.bp)