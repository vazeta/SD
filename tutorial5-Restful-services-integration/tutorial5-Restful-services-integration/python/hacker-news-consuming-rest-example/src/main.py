from fastapi import FastAPI
from MyHackerNewsController import router 

app = FastAPI()

# Register the controller's router
app.include_router(router)

# Uvicorn wrapper
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
