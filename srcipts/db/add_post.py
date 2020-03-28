from models import db_session
from models.post import Post

if __name__ == '__main__':
    db_session.global_init('sqlite:///../../db/wia_db.db')

post = Post(
    user_id=1,
    title='test title',
    description='test description')

session = db_session.create_session()
session.add(post)
session.commit()