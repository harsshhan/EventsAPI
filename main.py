from fastapi import FastAPI
from database import db
from model import NewEvent,UpdateEvent

app=FastAPI()

@app.get('/')
def main():
    return "Server running"


#store event details
@app.post('/newevent',description='Posting a new event')
def new_event(data:NewEvent):
    collection=db['event']
    try:
        collection.insert_one({'event_name':data.event_name,'location':data.location,'time':data.time,'description':data.description,'uuid':data.uuid})
    except:
        return "Error inserting"
    return 'Successful'

#read event details
@app.get('/events/{id}',description='Get the list of event details')
async def get_event(id:int):
    collection=db['event']
    result=collection.find_one({"uuid":id},{'_id':0})
    return result



#edit event details (update)
@app.put('/events/{id}',description="Update an event")
def update_event(id:int,data:UpdateEvent):
    collection=db['event']
    updated_data={}
    for k,v in data.dict().items():
        if v is not None:
            updated_data[k]=v
    if updated_data:
        collection.update_one({'uuid':id},{'$set':updated_data})
        return "update successfull"



#delete event details
@app.put('/delete/{id}')
def delete_event(id:int):
    collection=db['event']
    collection.delete_one({'uuid':id})
    return "Successfull"



#