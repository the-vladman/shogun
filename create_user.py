import os
from flask.ext.sqlalchemy import SQLAlchemy
from api.app import app,db
from users import User

passwd=app.config['PASSWORD']
username=app.config['USER']

if __name__ == '__main__':
    app.config.from_object('config.TestConfig')
    #if not os.path.exists('db.sqlite'):
    with app.app_context():
        db.create_all()
    user = User(username=username,config=app.config)
    user.hash_password(passwd)
    db.session.add(user)
    db.session.commit()
