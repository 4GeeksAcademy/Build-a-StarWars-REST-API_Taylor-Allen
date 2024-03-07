from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

favorite_people = db.Table(
    "favorite_people",
    db.Column("user_id", db.ForeignKey("user.id")),
    db.Column("person_id", db.ForeignKey("people.id")),
)

favorite_planets = db.Table(
    "favorite_planets",
    db.Column("user_id", db.ForeignKey("user.id")),
    db.Column("planet_id", db.ForeignKey("planet.id")),
)

favorite_vehicles = db.Table(
    "favorite_vehicles",
    db.Column("user_id", db.ForeignKey("user.id")),
    db.Column("vehicle_id", db.ForeignKey("vehicle.id")),
)

class User(db.Model):
    __tablename__ = "user"    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorite_people = db.relationship('People', secondary=favorite_people)
    favorite_planets = db.relationship('Planet', secondary=favorite_planets)
    favorite_vehicles = db.relationship('Vehicle', secondary=favorite_vehicles)


    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "favorite_people": [x.serialize() for x in self.favorite_people],
            "favorite_planets": [x.serialize() for x in self.favorite_planets],
            "favorite_vehicles": [x.serialize() for x in self.favorite_vehicles]
            # do not serialize the password, its a security breach
        }

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=True)
    length = db.Column(db.String(250), nullable=True)


    def __repr__(self):
        return '<Vehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "length": self.length
        }

class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=True)
    climate = db.Column(db.String(250), nullable=True)
    terrain = db.Column(db.String(250), nullable=True)
    diameter = db.Column(db.String(250), nullable=True)


    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "diameter": self.diameter
        }

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=True)
    hair_color = db.Column(db.String(250), nullable=True)
    eye_color = db.Column(db.String(250), nullable=True)


    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color
        }

