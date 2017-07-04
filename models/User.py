from sqlalchemy import Column, Integer, String, Sequence
from models.Meta import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', )>" % (
            self.name, self.fullname)



