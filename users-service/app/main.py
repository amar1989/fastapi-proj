from fastapi import FastAPI
from app.api.v1.routes_user import router as users_router
from app.db.session import Base, engine

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Users API with SQLAlchemy")
app.include_router(users_router, prefix="/api/v1")

@app.get("/health")
def health():
    return {"ok": True}
