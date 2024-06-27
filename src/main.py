from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import users, posts, auth
 
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users.router)
app.include_router(posts.router)
app.include_router(auth.router)

@app.get("/", tags=["Root"])
def read_root():
    return {
        "message" : "home page!"
        }
