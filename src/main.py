from fastapi import FastAPI
from .routes import users, posts, auth
 
app = FastAPI()

print("main.py")

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(auth.router)

@app.get("/", tags=["Root"])
def read_root():
    return {
        "message" : "hello worlddddd!"
        }
