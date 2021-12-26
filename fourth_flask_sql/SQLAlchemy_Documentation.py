# from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy()
#
#
# class ItemModel(db.Model):
#     """ Telling SQLAlchemy which table we want to use"""
#     __tablename__ = "items"
#
#     """ What columns we want the table to contain
#     primary key means that this is unique
#     """
#     id = db.Column(db.Integer, primary_key=True)
#
#     name = db.Column(db.String(80))  # For setting characters limit to 80
#     price = db.Column(db.Float(precision=2))  # For setting decimal places
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     @classmethod
#     def find_by_name(cls, name):
#         """ Using SQLAlchemy query filter to return the first result that matches name"""
#         # return cls.query.filter_by(name=name).first()
#
#         """ Using two filter: name and id"""
#         return cls.query.filter_by(name=name).filter_by(id=1)
#
#     """ Insert/Update item in DataBase"""
#     def save_to_db(self):
#         db.session.add(self)
#         db.session.commit()
#
#     """ Delete item from DataBase"""
#     def delete_from_db(self):
#         db.session.delete(self)
#         db.session.commit()
#
#
# class ItemList(Resource):
#     def get(self):
#         return {'item': ItemModel.query.all()}  # Returns all of the objects in the database
#
# # SQLAlchemy is slightly slower :))
