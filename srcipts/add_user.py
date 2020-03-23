from web.models import db_session
from web.models.user import User

if __name__ == '__main__':
    db_session.global_init('../web/db/wia_db.db')

user1 = User(
        nickname='test2',
        first_name='test2',
        last_name='test2',
        email='test2@test2.test2',
        unhashed_password='test2')

user2 = User(
        nickname='test',
        first_name='test',
        last_name='test',
        email='test@test.test',
        unhashed_password='test')

session = db_session.create_session()
session.add(user1)
session.add(user2)
session.commit()