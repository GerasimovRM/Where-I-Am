from models import db_session
from models.attachment import Attachment

if __name__ == '__main__':
    db_session.global_init('sqlite:///../../db/wia_db.db')

attachment = Attachment(
    post_id=1,
    description='test description',
    location='my place')

session = db_session.create_session()
session.add(attachment)
session.commit()