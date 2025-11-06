import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.anyio
async def test_create_and_get_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # create
        payload = {"name": "Amar", "email": "amar@example.com", "age": 35}
        r = await ac.post("/api/v1/users/", json=payload)
        assert r.status_code == 201
        data = r.json()
        user_id = data["id"]

        # get by id
        r2 = await ac.get(f"/api/v1/users/{user_id}")
        assert r2.status_code == 200
        assert r2.json()["email"] == "amar@example.com"

        # list
        r3 = await ac.get("/api/v1/users?limit=10")
        assert r3.status_code == 200
        assert any(u["id"] == user_id for u in r3.json())

@pytest.mark.anyio
async def test_get_user_not_found():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.get("/api/v1/users/99999")
        assert r.status_code == 404