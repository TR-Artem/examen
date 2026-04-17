from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.routers import auth, tasks, admin

app = FastAPI(
    title="Task Tracker API",
    version="1.0.0"
)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    print("✅ База данных создана")

app.include_router(auth.router)
app.include_router(tasks.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"message": "Task Tracker API is running"}