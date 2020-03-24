import sqlalchemy as sa
from sqlalchemy.orm import relation
from .db_session import SqlAlchemyBase


class Admin(SqlAlchemyBase):
    __tablename__ = 'admin'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'), unique=True, nullable=False)

    user = relation('User', back_populates='admin')
    super_admin = relation('SuperAdmin', back_populates='admin')