from web.models import db_session
from web.models.user import User, friends_table

if __name__ == '__main__':
    db_session.global_init('../web/db/wia_db.db')

session = db_session.create_session()
state = friends_table.insert().values(user_id_1=1, user_id_2=2)
session.execute(state)
session.commit()
