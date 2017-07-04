from sqlalchemy import Column, Integer, String, Sequence
from models import Meta, User


class Group(Meta):
    __tablename__ = 'groups'
    id = Column(Integer, Sequence('group_id_seq'), primary_key=True)