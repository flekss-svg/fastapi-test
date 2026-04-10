from fastapi import FastAPI
import uvicorn

app=FastAPI()
users=[{"id":1,"name":"Diman"}]
@app.get("/users")
def get_users():
    return users
if __name__=="__main__":
    uvicorn.run("main:app",host='0.0.0.0')