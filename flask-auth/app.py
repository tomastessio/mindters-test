from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

def authenticate(username, password):
    user = User.query.filter_by(username=username, password=password).first()
    return user is not None


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not authenticate(auth.username, auth.password):
            return Response(
                'Could not verify your access, please try again', 401,
                {'WWW-Authenticate': 'Basic realm="Login required!"'})
        return f(*args, **kwargs)
    return decorated

@app.route('/')
@requires_auth
def index():
    return "Welcome to the protected route!"


@app.route('/user_info', methods=['GET'])
@requires_auth
def get_user_info():
    with app.app_context():
        user_id = request.args.get('user_id')

        if not user_id:
            return Response('User ID is missing', 400)

        user = None
        user = User.query.get(user_id)

        if not user:
            return Response('User not found', 404)

        user_info = {
            'id': user.id,
            'username': user.username,
        }

        return jsonify(user_info)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run()