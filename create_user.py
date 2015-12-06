from api.auth.users import User,db
from api.bare_app import app

def create_user():
    app.config.from_object('config.TestConfig')
    passwd=app.config['PASSWORD']
    username=app.config['USER']
    with app.app_context():
        db.create_all()
    user = User(username=username,config=app.config)
    user.hash_password(passwd)
    db.session.add(user)
    db.session.commit()
    return user


if __name__ == '__main__':
    user = create_user()
    print user.generate_auth_token()
