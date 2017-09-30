import uuid
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///../resources/messages.db', echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Message(Base):
    __tablename__ = 'message'

    uuid = Column(String, primary_key=True, nullable=False)
    time = Column(DateTime, nullable=False)
    author = Column(String, nullable=False, index=True)
    chatgroup = Column(String, nullable=False, index=True)
    msg = Column(String)
    isGroup = Column(Boolean)
    charslen = Column(Integer, nullable=False)
    wordslen = Column(Integer, nullable=False)

    def __init__(self, time, author, chatgroup, msg, charslen, wordslen, isGroup = True):
        self.uuid = str(uuid.uuid1())
        self.time = time
        self.author = author
        self.chatgroup = chatgroup
        self.msg = msg
        self.charslen = charslen
        self.wordslen = wordslen
        self.isGroup = isGroup


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

def addMessage(msgs):
    session = Session()
    session.add_all(msgs)
    session.commit()