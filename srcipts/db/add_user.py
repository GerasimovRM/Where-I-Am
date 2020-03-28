from models import db_session
from models.user import User


if __name__ == '__main__':
    db_session.global_init('sqlite:///../../db/wia_db.db')


user1 = User(
        nickname='fedor777',
        first_name='Федя',
        last_name='Крюков',
        email='feodor3@gmail.com',
        unhashed_password='my_unhashable_password')

user2 = User(
        nickname='Roman',
        first_name='Roman',
        last_name='Science',
        email='roma@mmsp.ru',
        unhashed_password='megA_password')

session = db_session.create_session()
session.add(user1)
session.add(user2)
session.commit()
