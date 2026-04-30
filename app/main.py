from fastapi import FastAPI
from app.routes import user_routes, fight_routes, performance_routes

app = FastAPI()

app.include_router(user_routes.router)
app.include_router(fight_routes.router)
app.include_router(performance_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Boxing Performance Evaluation Platform!"}