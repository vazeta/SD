from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from app.routes import router
from app.models import Counter

app = FastAPI()

# Set up session middleware (a secret key is required)
app.add_middleware(SessionMiddleware, secret_key="!secret")

# Create a global application-scoped counter and store it in the app state.
app.state.application_counter = Counter()

# Include our routes (all endpoints are in app/routes.py)
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True)
