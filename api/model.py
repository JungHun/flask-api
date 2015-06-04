import sys , os
import pytest
sys.path.append(os.getcwd().replace('/api','',1))
from   database       import Base
from   sqlalchemy     import Column, Integer, String

#@pytest.fixture
class Host(Base):
    __tablename__ = 'host_info'

    access_no     = Column(Integer  , primary_key=True)
    send_number   = Column(Integer  , unique=True)
    action_verb   = Column(String(1), unique=True)

    def __init__(self, send_number=None, action_verb=None):
        self.send_number   = send_number
        self.action_verb   = action_verb

    def __repr__(self):
        return '<send_number %r>' % (self.send_number)
