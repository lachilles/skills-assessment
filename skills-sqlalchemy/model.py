"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Model(db.Model):
    """Car model."""

    __tablename__ = "models"
    model_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    year = db.Column(db.Integer, nullable=True)
    brand_name = db.Column(db.String(64), db.ForeignKey('models.brand_name'))
    name = db.Column(db.String(64), nullable=True)

    brand_name = db.relationship("Brand")

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Model model_id=%s brand_name=%s>" % (self.model_id, self.brand_name)


class Brand(db.Model):
    """Car brand."""

    __tablename__ = "brands"
    brand_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), db.ForeignKey('brands.name'))
    founded = db.Column(db.Integer, nullable=True)
    headquarters = db.Column(db.String(64), nullable=True)
    discontinued = db.Column(db.Integer, nullable=True)

    name = db.relationship("Model")

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Model brand_id=%s name=%s>" % (self.brand_id, self.name)


# End Part 1


##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///cars'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
