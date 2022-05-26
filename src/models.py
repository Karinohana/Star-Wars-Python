from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email
            # do not serialize the password, its a security breach
        }

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    def __repr__(self):
        return f"<Account {self.id}>"
    def serialize(self):
        return {
            'id': self.id,
            'total': self.total
        }


class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.String(80), unique=False, nullable=False)
    terrain = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    image1 = db.Column(db.String(200), nullable=False)
    image2 = db.Column(db.String(200), nullable=False)
    brief = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(400), nullable=False)
    tbd = db.Column(db.String(200), nullable=True)
    tbd2 = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "image1": self.image1,
            "image2": self.image2,
            "brief": self.brief,
            "description": self.description,
            # do not serialize the password, its a security breach
        }