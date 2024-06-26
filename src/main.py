from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from .db import engine, Base
from .routes import users, posts, auth
 
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(auth.router)

@app.get("/", tags=["Root"])
def read_root():
    return {
        "message" : "home page!"
        }
