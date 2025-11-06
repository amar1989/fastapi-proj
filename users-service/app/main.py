from fastapi import FastAPI
from app.api.v1.routes_user import router as users_router

#app = FastAPI()

app = FastAPI(title="Users API")
app.include_router(users_router)

@app.get("/health")
def health():
    return {"ok": True}
