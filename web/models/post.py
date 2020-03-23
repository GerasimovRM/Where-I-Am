import sqlalchemy as sa
from sqlalchemy.orm import relation
import datetime

from .db_session import SqlAlchemyBase


class Post(SqlAlchemyBase):
    __tablename__ = 'post'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'), unique=True, nullable=False)
    title = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String, nullable=True)
    post_date = sa.Column(sa.DateTime, default=datetime.datetime.now)

    user = relation('User', back_populates='posts')
    attachments = relation('Attachment', back_populates='post')