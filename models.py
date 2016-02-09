from sqlalchemy import Column, Integer, String, Text, DateTime, Date, Boolean
from database import Base

class Event(Base):
    __tablename__ = 'events'
    id              = Column(Integer, primary_key=True)
    event_id        = Column(Integer)
    name            = Column(String(255))
    start_time      = Column(DateTime)
    date            = Column(Date)
    location        = Column(String(120))
    is_date_only    = Column(Boolean)
    description     = Column(Text)
    picture_url     = Column(String(120))

    def __init__(self, event_id=None, name=None, start_time=None, date=None,
        location=None, is_date_only=False, description=None, picture_url=None):
        self.event_id       = event_id
        self.name           = name
        self.start_time     = start_time
        self.date           = date
        self.location       = location
        self.is_date_only   = is_date_only
        self.description    = description
        self.picture_url    = picture_url

    def __repr__(self):
        return "<Event %r>" % self.name
