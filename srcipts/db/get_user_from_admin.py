from models import db_session
from models.user import User
from models.admin import Admin


if __name__ == '__main__':
    db_session.global_init('sqlite:///../../db/wia_db.db')


session = db_session.create_session()
admin = session.query(Admin).first()
#user = session.query(User).filter(User.id.in_(admin)).first()
#print(user)
session.commit()
