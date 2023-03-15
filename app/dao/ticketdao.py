from sqlalchemy import Column, Integer, String
from app.config.config import Base

class Ticket(Base):
    __tablename__ = 'ticket_app_table'
    event_id = Column(Integer, primary_key=True)
    event_name = Column(String(250))
    total_tickets = Column(Integer)
    ticket_price = Column(Integer)
