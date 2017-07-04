from sqlalchemy import Table, ForeignKey, Column, DateTime, Integer, String, Sequence
from sqlalchemy.orm import relationship
from models.Meta import Base
import datetime

users_has_groups = Table('users_has_groups', Base.metadata,
                    Column('user_id', Integer, ForeignKey('users.id')),
                    Column('group_id', Integer, ForeignKey('groups.id'))
                    )


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, Sequence('groups_id_seq'), primary_key=True)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    users = relationship('User', secondary=users_has_groups, back_populates='groups')
