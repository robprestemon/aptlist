from sqlalchemy import Column, DateTime, Integer, String, Sequence
from sqlalchemy.orm import relationship
from models.Meta import Base
from models.Group import users_has_groups
import datetime


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('users_id_seq'), primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    groups = relationship('Group', secondary=users_has_groups, back_populates='users')
    created = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<User(name='%s', email='%s', created='%s', group='%s')>" % (
            self.name, self.email, self.created, self.groups)

