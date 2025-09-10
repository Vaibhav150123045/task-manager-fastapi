from fastapi import FastAPI
from routes import user_authentication

app = FastAPI(title="My FastAPI App", version="1.0.0")

# Include routers
app.include_router(user_authentication.router,
                   prefix="/user_authentication", tags=["Authentication"])
# app.include_router(users.router, prefix="/users", tags=["Users"])
# app.include_router(items.router, prefix="/items", tags=["Items"])


@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI App"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
