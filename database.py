from   sqlalchemy                 import create_engine
from   sqlalchemy.orm             import scoped_session, sessionmaker
from   sqlalchemy.ext.declarative import declarative_base
import sys , os
sys.path.append(os.getcwd().replace('/api','',1))
import config
import pytest

engine = create_engine(config.__SQLALCHEMY_DATABASE_URI)

db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
Base       = declarative_base()
Base.query = db_session.query_property()

#@pytest.fixture
def init_db():
    Base.metadata.create_all(bind=engine)

