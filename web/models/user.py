from flask_login import UserMixin
import sqlalchemy as sa
from sqlalchemy.orm import relation, mapper
from werkzeug.security import generate_password_hash
import datetime

from .db_session import SqlAlchemyBase




friends_table = sa.Table('friends', SqlAlchemyBase.metadata,
                         sa.Column('user_id_1', sa.Integer, sa.ForeignKey('user.id'), primary_key=True),
                         sa.Column('user_id_2', sa.Integer, sa.ForeignKey('user.id'), primary_key=True))


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'user'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nickname = sa.Column(sa.String, unique=True, nullable=False)
    first_name = sa.Column(sa.String, nullable=False)
    last_name = sa.Column(sa.String, nullable=False)
    middle_name = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, unique=True, nullable=False)
    password = sa.Column(sa.String, nullable=False)
    registration_date = sa.Column(sa.DateTime, default=datetime.datetime.now)

    admin = relation('Admin', back_populates='user')
    posts = relation('Post', back_populates='user')


    friend_ids = relation("User",
                          secondary=friends_table)


    @property
    def unhashed_password(self):
        raise AttributeError('Cannot view unhashed password!')

    @unhashed_password.setter
    def unhashed_password(self, unhashed_password):
        self.password = generate_password_hash(unhashed_password)
