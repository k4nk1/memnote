from flask import Blueprint, request
from json import dumps
from models  import db, User, Note
from utils import short_uuid

class UserAPI():
    bp = Blueprint('user', __name__, url_prefix='/u')
    
    @bp.route('', methods=['POST'])
    def add():
        id = short_uuid()
        user = User()
        user.id = id
        db.session.add(user)
        db.session.commit()
        return dumps({'id': id})

    @bp.route('/<id>', methods=['DELETE'])
    def delete(id):
        user = db.session.get(User, id)
        if user is None: return '', 400
        db.session.delete(user)
        db.session.commit()
        return ''
    
    @bp.route('/<id>/n', methods=['GET'])
    def get_mynotes(id):
        user = db.session.get(User, id)
        if user is None: return dumps({'errmsg': 'Not Exist'}), 404
        notes = user.notes
        return dumps({'notes':[{'id': note.id, 'title': note.title} for note in notes]})

class NoteAPI():
    bp = Blueprint('note', __name__, url_prefix='/n')

    @bp.route('/<id>', methods=['GET'])
    def get(id):
        note: Note = db.session.get(Note, id)
        if note is None: return dumps({'errmsg': 'Not Exist'}), 404
        return dumps({'title': note.title, 'content': note.content})

    @bp.route('', methods=['POST'])
    def add():
        user_id = request.json.get('u')
        if user_id is None: return dumps({'errmsg': 'Unauthorized'}), 401
        user = db.session.get(User, user_id)
        if user is None: return dumps({'errmsg': 'Not Exist'}), 404
        note = Note()
        note.id = short_uuid()
        note.author = user
        note.author_id = user_id
        note.title = '新規ノート'
        note.content = ''
        db.session.add(note)
        user.notes.append(note)
        db.session.commit()
        return dumps({'id': note.id})

    @bp.route('/<id>', methods=['PUT'])
    def put(id):
        json: dict = request.json
        note = db.session.get(Note, id)
        if note is None: return dumps({'errmsg': 'Not Exist'}), 404
        if json.get('u') != note.author_id: return dumps({'errmsg': 'Unauthorized'}), 401
        if json.get('t') is not None: note.title = json.get('t')
        if json.get('c') is not None: note.content = json.get('c')
        db.session.commit()
        return ''

    @bp.route('/<id>', methods=['DELETE'])
    def delete(id):
        json: dict = request.json
        note = db.session.get(Note, id)
        if note is None: return dumps({'errmsg': 'Not Exist'}), 404
        if json.get('u') != note.author_id: return dumps({'errmsg': 'Unauthorized'}), 401
        db.session.delete(note)
        db.session.commit()
        return ''

api_bp = Blueprint('api', __name__, url_prefix='/api')
api_bp.register_blueprint(UserAPI.bp)
api_bp.register_blueprint(NoteAPI.bp)