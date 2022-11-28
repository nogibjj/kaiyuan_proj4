from fastapi import FastAPI, HTTPException
import uvicorn
from fruitlib.ranfruit import fruit_generator
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Song(BaseModel):

    name: str
    artist: str
    description: str

store_songlist = []

@app.get("/")
async def root():
    return {"message": "Hello Project 4 This is a song list. Add/Read/Delete/Update your songs"}

#create
@app.post('/add/')
async def create_song(song: Song):
    store_songlist.append(song)
    return song

#read
@app.get('/getall/', response_model=List[Song])
async def get_all_songs():
    return store_songlist

#delete
@app.delete('/delete/{name}')
async def delete_song(name: str):
    for i,x in enumerate(store_songlist):
        if x.name == name:
            obj = store_songlist[i]
            store_songlist.pop(i)
            return obj

    raise HTTPException(status_code=404, detail="Song Not Found")

#update
@app.put('/update/{name}')
async def update_todo(name: str, song: Song):
    for i,x in enumerate(store_songlist):
        if x.name == name:
            store_songlist[i] = song
            return store_songlist[i]

    raise HTTPException(status_code=404, detail="Song Not Found")

'''
@app.get("/fruits/{fruit}")
async def myfruit(fruit: str):
    """Adds a fruit to random fruit"""

    chosen_random_fruit = fruit_generator(fruit)
    return {"random_fruit": chosen_random_fruit}
    '''

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')