from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_heroku import Heroku
# from flask_bcrypt import Bcrypt

app = Flask(__name__)
# CORS(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = ''
# heroku = Heroku(app)
# db = SQLAlchemy(app)

# class User(db.Model):
#     __tablename__ ="users"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120), nullable=False)
#     password = db.Column(db.String(), nullable=False)
#     user_type = db.Column(db.String(30), nullable=False)
#     requests = db.relationship('Requests', backref='users', lazy=True)
#     tasks = db.relationship('Tasks', backref='users', lazy=True)

#     def __init__(self, name, password, user_type):
#         self.name = name
#         self.password = password
#         self.user_type = user_type

#     def __repr__(self):
#         return '<Title %r>' % self.name


# class Request(db.Model):
#     __tablename__ = "requests"

#     id = db.Column(db.Integer, primary_key=True)
#     activity = db.Column(db.String(100), nullable=False)
#     time = db.Column(db.String(40), nullable=True)

#     users_id = db.Column(db.Integer, db.ForeignKey(User.id))

#     def __init__(self, activity, time, users_id):
#         self.activity = activity
#         self.time = time
#         self.users_id = users_id

# class Task(db.Model):
#     __tablename__ = "tasks"

#     id = db.Column(db.Integer, primary_key=True)
#     task = db.Column(db.String(100), nullable=False)
#     comment = db.Column(db.String(100), nullable=True)
#     image_url = db.Column(db.String(150), nullable=True)

#     users_id = db.Column(db.Integer, db.ForeignKey(User.id))

#     def __init__(task, comment, image_url, users_id):
#         self.task = task
#         self.comment = comment
#         self.image_url = image_url
#         self.users_id = users_id


@app.route("/")
def home():
    return "<h1>Hi Galen</h1>"


# @app.route('/users/input', methods=['POST'])
# def user_input():
#     if request.content_type == 'application/json':
#         post_data = request.get_json()

#         name = post_data.get('name')
#         password = post_data.get('password')
#         user_type = post_data.get('user_type')
        
#         reg = User(name, password, user_type)
#         db.session.add(reg)
#         db.session.commit()
#         return jsonify("User Posted")
#     return jsonify("Something went wrong")

# @app.route('/users', methods=['GET'])
# def return_all_users():
#     all_users = db.session.query(User.id, User.name, User.password, User.user_type).all()
#     return jsonify(all_users)

# @app.route("/users/verification", methods=["POST"])
# def user_verification():
#     if request.content_type == "application/json":
#         post_data = request.get_json()
#         user_password = post_data.get("password")
#         check_username = db.session.query(User.name).filter(User.name == post_data.get("name")).first()
#         if check_username is None:
#             return jsonify("User NOT Verified")
#         valid_password = db.session.query(User.password).filter(User.password == post_data.get("password")).first()
#         if valid_password is None:
#             return jsonify("Password NOT Verified")
#         if user_password != valid_password:
#             return jsonify("Password NOT Verified")
#         return jsonify("User Verified")
#     return jsonify("Error verifying user")







# ###################################################
# ## originally from Andrew's book list python app ##
# ###################################################
# @app.route('/book/input', methods=['POST'])
# def books_input():
#     if request.content_type == 'application/json':
#         post_data = request.get_json()
#         # if the request (someone pings the url) is a json application, then send data to database
#         title = post_data.get('title')
#         author = post_data.get('author')
#         reg = Book(title, author)
#         db.session.add(reg)
#             # will taking the title and author and add to the db
#         db.session.commit()
#         return jsonify("Data Posted")
#     return jsonify("Something went wrong")
#         # his happens if the if statement above is false

# @app.route('/books', methods=['GET'])
# def return_books():
#     all_books = db.session.query(Book.id, Book.title, Book.author).all()
#     return jsonify(all_books)

# @app.route('/book/<id>', methods=['GET'])
# def return_single_book(id):
#     one_book = db.session.query(Book.id, Book.title, Book.author).filter(Book.id == id).first()
#     # storing the query in a variable
#     return jsonify(one_book)
#     # this is the SQL code (abbreviated) that is actually running
#         # SELECT books.title, etc
#         # FROM book
#         # WHERE books.id = 1

# @app.route('/delete/<id>', methods=["DELETE"])
# # // this will pass id in as the arguement below. This is a changeable piece of code (like a slug)
# def book_delete(id):
#     if request.content_type == 'application/json':
#         record = db.session.query(Book).get(id)
#         db.session.delete(record)
#         db.session.commit()
#         return jsonify("Completed Delete action")
#     return jsonify("Delete Failed")

# @app.route('/update_book/<id>', methods=["PUT"])
# def book_update(id):
#     if request.content_type =='application/json':
#         put_data = request.get_json()
#         title = put_data.get('title')
#         author = put_data.get('author')
#         record = db.session.query(Book).get(id)
#         record.title = title
#         record.author = author
#         db.session.commit()
#         return jsonify("Completed Update")
#     return jsonify("Update Failed")


if __name__ == "__main__":
    app.debut = True
    app.run()
