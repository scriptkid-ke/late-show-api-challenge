from server.app import db

class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(100), nullable=False)

    appearances = db.relationship('Appearance', backref='guest', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Guest {self.name}>'