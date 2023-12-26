from fastapi import FastAPI

from src.routers import analyse_router
from src.routers import data_router

app = FastAPI()
import os

workspace_path = os.getcwd()  # This gets the current working directory
print("Workspace path:", workspace_path)
# Include routers from different features
# app.include_router(analyse_router, prefix="/analyse", tags=["analyse"])
app.include_router(data_router)
app.include_route
# Add more routers for other features...

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)