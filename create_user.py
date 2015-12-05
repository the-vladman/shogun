from api.app import app,db
from users import User

if __name__ == '__main__':
    app.config.from_object('config.TestConfig')
    passwd=app.config['PASSWORD']
    username=app.config['USER']
    with app.app_context():
        db.create_all()
    user = User(username=username,config=app.config)
    user.hash_password(passwd)
    db.session.add(user)
    db.session.commit()
    print user.generate_auth_token()
