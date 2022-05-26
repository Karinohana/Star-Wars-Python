"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
from models import People
from models import Planets
from models import Account
from argon2 import PasswordHasher
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager

ph= PasswordHasher()

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "very-long-secret-nobody-know"  # Change this "super secret" with something else!
jwt = JWTManager(app)

app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

@app.route('/register', methods=['POST'])
def register():
    payload = request.get_json()
    user = User(
        email=payload['email'],
        password=ph.hash(payload['password']),
        is_active=True
    )
    db.session.add(user)
    db.session.commit()
    return "user registered", 200

@app.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    user = User.query.filter(User.email == payload['email']).first()
    if user is None:
        return 'failed-auth', 401
    try:
        ph.verify(user.password, payload['password'])
    except:
        return 'failed-auth', 401
    token = create_access_token(identity=user.id)
    return jsonify({ 'token': token })

@app.route('/accounts', methods=['GET'])
@jwt_required()
def accounts():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    accounts = Account.query.filter(Account.user_id==user_id).all()
    account_info = {
        "accounts": [x.serialize() for x in accounts],
        "user": user.serialize()
    }
    return jsonify(account_info)

@app.route('/people/<int:id>', methods=['GET'])
def handle_people_id(id):
    people = People.query.filter(People.id)
    response = {
        "person": People.serialize(people[id-1])
    }

    

    return jsonify(response), 200

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/user/favorites', methods=['GET'])
def handle_user_favorites():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/people', methods=['GET'])
def handle_people():
    table = People.query.all()
    data = list(map(lambda x: x.serialize(),table))

    return jsonify(data), 200



@app.route('/planets', methods=['GET'])
def handle_planets():
    table = Planets.query.all()
    data = list(map(lambda x: x.serialize(),table))

    return jsonify(data), 200

@app.route('/planets', methods=['POST'])
def handle_post_planet():
    payload = request.get_json()
    info = Planets(name = payload["name"],climate = payload["climate"], terrain = payload["terrain"])
    db.session.add(info)
    db.session.commit()

    return "success", 200


@app.route('/planets/<int:planet_id>', methods=['GET'])
def handle_planets_id():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def handle_favs_planet():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def handle_favs_people():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/people', methods=['POST'])
def handle_post_people():
    payload = request.get_json()
    info = People(name = payload["name"],image1 = payload["image1"], image2 = payload["image2"], brief = payload["brief"], description = payload["description"],tbd = payload["tbd"], tbd2 = payload["tbd2"])
    db.session.add(info)
    db.session.commit()


    return jsonify("success"), 200

@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def handle_delete_planet():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/favorite/people/<int:people_id> ', methods=['DELETE'])
def handle_delete_people():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
