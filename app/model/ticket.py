from pydantic import BaseModel

class Ticket(BaseModel):
    event_name:str
    total_tickets:int
    ticket_price:int
