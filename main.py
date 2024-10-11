from fastapi import FastAPI 

app = FastAPI()

@app.get("/items/{item_id}")

async def read_item(item_id:int):
  return {"item_id":item_id}
  ##fastapi takes care of serializing python dic into json objct


@app.get("/users/me")

async def read_user_me():
  return {"user_id":"the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: int):
  return {"user_id":user_id}  