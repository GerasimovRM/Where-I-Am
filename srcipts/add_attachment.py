from models import db_session
from models.attachment import Attachment

if __name__ == '__main__':
    db_session.global_init('../web/db/wia_db.db')

post = Attachment(
    post_id=1,
    description='test description',
    location='my place')

session = db_session.create_session()
session.add(post)
session.commit()