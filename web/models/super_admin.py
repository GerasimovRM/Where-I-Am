import sqlalchemy as sa
from sqlalchemy.orm import relation

from .db_session import SqlAlchemyBase


class SuperAdmin(SqlAlchemyBase):
    __tablename__ = 'super_admin'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    admin_id = sa.Column(sa.Integer, sa.ForeignKey('admin.id'), unique=True, nullable=False)

    admin = relation('Admin', back_populates='super_admin')