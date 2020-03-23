import sqlalchemy as sa
from sqlalchemy.orm import relation

from .db_session import SqlAlchemyBase


class Attachment(SqlAlchemyBase):
    __tablename__ = 'attachment'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    post_id = sa.Column(sa.Integer, sa.ForeignKey('post.id'), nullable=False)
    photo = sa.Column(sa.BLOB, nullable=True)
    description = sa.Column(sa.String, nullable=True)
    location = sa.Column(sa.String, nullable=True)

    post = relation('Post', back_populates='attachments')