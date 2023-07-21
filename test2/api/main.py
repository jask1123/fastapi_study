from fastapi import FastAPI

from api.routers import task, done, user, token

app = FastAPI()

app.include_router(task.router, tags=["Task"])
app.include_router(done.router, tags=["Done"])
app.include_router(user.router, tags=["User"])
app.include_router(token.router, tags=["Token"])
