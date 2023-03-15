from fastapi import FastAPI, Body, Depends
import app.model.ticket as ticket
import app.dao.ticketdao as ticketdao

from app.config.config import Base, engine, SessionLocal
from sqlalchemy.orm import Session 

Base.metadata.create_all(engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

app = FastAPI()

@app.get("/ticket/all")
def getItems(session: Session = Depends(get_session)):
    items = session.query(ticketdao.Ticket).all()
    return items

@app.get("/ticket/{id}")
def getItem(id:int, session: Session = Depends(get_session)):
    item = session.query(ticketdao.Ticket).get(id)
    return item


@app.post("/ticket/add")
def addItem(item:ticket.Ticket, session: Session = Depends(get_session)):
    item = ticketdao.Ticket(event_name = item.event_name,total_tickets = item.total_tickets,ticket_price = item.ticket_price)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@app.put("/ticket/update/{id}")
def updateItem(id:int, item:ticket.Ticket, session: Session = Depends(get_session)):
    itemObject = session.query(ticketdao.Ticket).get(id)
    itemObject.event_name = item.event_name
    itemObject.total_tickets = item.total_tickets
    itemObject.ticket_price = item.ticket_price
    session.commit()
    return itemObject


@app.delete("/ticket/remove/{id}")
def deleteItem(id:int, session: Session = Depends(get_session)):
    itemObject = session.query(ticketdao.Ticket).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    return 'Selected Item was deleted...'
