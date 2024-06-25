from flask import Blueprint, request
from json import dumps
from models  import db, User, Note
from utils import short_uuid

class UserAPI():
    bp = Blueprint('user', __name__, url_prefix='/u')
    
    @bp.route('/', methods=['POST'])
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

class NoteAPI():
    bp = Blueprint('note', __name__, url_prefix='/n')

    @bp.route('/', methods=['GET'])
    def get_by_author():
        notes = db.session.query(Note).filter_by(author=request.args.get('u')).all()
        return dumps({'notes':[{'id': note.id, 'title': note.title} for note in notes]})

    @bp.route('/<id>', methods=['GET'])
    def get(id):
        note: Note = db.session.get(Note, id)
        if note is None: return dumps({'errmsg': 'Not Exist'}), 404
        return dumps({'title': note.title, 'content': note.content})

    @bp.route('/', methods=['POST'])
    def add():
        note = Note()
        note.id = short_uuid()
        note.author = request.json['u']
        note.title = '新規ノート'
        note.content = ''
        db.session.add(note)
        db.session.commit()
        return dumps({'id': note.id})

    @bp.route('/<id>', methods=['PUT'])
    def put(id):
        pass

    @bp.route('/<id>', methods=['DELETE'])
    def delete(id):
        pass

api_bp = Blueprint('api', __name__, url_prefix='/api')
api_bp.register_blueprint(UserAPI.bp)
api_bp.register_blueprint(NoteAPI.bp)