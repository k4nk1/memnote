from flask import Flask, render_template
from flask_cors import CORS
from api import api_bp
import models

app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
app.config.from_pyfile('app.cfg')
CORS(app)

app.register_blueprint(api_bp)
models.init(app)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run()