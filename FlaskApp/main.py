from flask import Flask, render_template, redirect, url_for
from Routing.myroute import myroute_bp  # import the blueprint
from DBContext.dbclass import mydb_bp, db, User  # import blueprint AND db instance

#constructor init the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "AAAAAAAAAAAAAAAAAAAAAAAAABBBBBBB"

# Initialize DB with app
db.init_app(app)
# Register the blueprint
app.register_blueprint(myroute_bp) #routing bp
app.register_blueprint(mydb_bp) #routing db

with app.app_context():
    db.create_all()

    # # Check if the table is empty
    # if User.query.count() == 0:
    #     default_users = [
    #         User(username="admin", password="admin123"),
    #         User(username="user1", password="password1"),
    #         User(username="user2", password="password2")
    #     ]
    #     db.session.bulk_save_objects(default_users)
    #     db.session.commit()
    #     print("Default users added to the database.")

if __name__ == '__main__':

    app.run(debug=True)




