from fastapi import FastAPI,HTTPException
from database import db
from model import NewEvent,UpdateEvent


app=FastAPI()

@app.get('/')
def main():
    return "Server running"



#store event details
@app.post('/newevent', description='Posting a new event', status_code=201)
def new_event(data: NewEvent):
    collection = db['event']
    
    existing_event = collection.find_one({"uuid": data.uuid})
    
    if existing_event:
        raise HTTPException(status_code=409, detail="Event with this ID already exists")

    try:
            collection.insert_one({
                'event_name': data.event_name,
                'location': data.location,
                'time': data.time,
                'description': data.description,
                'uuid': data.uuid
            })
            return {"message": "Event created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error inserting event: " + str(e))

#read event details
@app.get('/events/{id}', description='Get the event details')
async def get_event(id: int):
    collection = db['event']
    result = collection.find_one({"uuid": id}, {'_id': 0})
    if not result:
        raise HTTPException(status_code=404, detail="Event not found")
    return result



#edit event details (update)
@app.patch('/events/{id}', description="Update an event")
def update_event(id: int, data: UpdateEvent):
    collection = db['event']

    existing_event = collection.find_one({"uuid": id})
    
    if not existing_event:
        raise HTTPException(status_code=404, detail="Event not found")
    updated_data = data.dict()
    if updated_data:
        result = collection.update_one({'uuid': id}, {'$set': updated_data})
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Event not found")
        return {"message": "Event updated successfully"}
    raise HTTPException(status_code=400, detail="No data provided for update")



#delete event details
@app.delete('/events/{id}', description="Delete an event")
def delete_event(id: int):
    collection = db['event']
    result = collection.delete_one({'uuid': id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"message": "Event deleted successfully"}