from flask_login import UserMixin
import sqlalchemy as sa
from sqlalchemy.orm import relation
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

from .db_session import SqlAlchemyBase, create_session


friends_relation = sa.Table('friends', SqlAlchemyBase.metadata,
                            sa.Column('user_id_1', sa.Integer, sa.ForeignKey('user.id'), primary_key=True),
                            sa.Column('user_id_2', sa.Integer, sa.ForeignKey('user.id'), primary_key=True))


class User(SqlAlchemyBase, SerializerMixin):
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

    # Дружественность в одну сторону! Вот такие вот друзья в наше время..
    friends = relation('User', secondary=friends_relation,
                          primaryjoin=friends_relation.c.user_id_1==id,
                          secondaryjoin=friends_relation.c.user_id_2==id,
                          backref="back_friends")

    @property
    def unhashed_password(self):
        raise AttributeError('Cannot view unhashed password!')

    @unhashed_password.setter
    def unhashed_password(self, unhashed_password):
        self.password = generate_password_hash(unhashed_password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    # to_dict из SerializerMixin не работает, так как ругается на рекурсию, связанную со связью user <MTM>
    def to_dict(self, **kwargs):
        answer = {}
        friends = list(map(lambda u: u.id, self.friends))
        back_friends = list(map(lambda u: u.id, self.back_friends))
        user = super().to_dict(only=['id', 'nickname', 'last_name', 'first_name', 'middle_name'], **kwargs)
        answer.update(user)
        answer['friends'] = friends
        answer['back_friends'] = back_friends
        return answer

    def __repr__(self):
        return '\n'.join(map(str, [self.id,
                                   self.nickname,
                                   self.first_name,
                                   self.middle_name,
                                   self.last_name,
                                   self.email,
                                   self.registration_date,
                                   self.posts]))
