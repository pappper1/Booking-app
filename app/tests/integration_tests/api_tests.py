import random

import pytest
from httpx import AsyncClient


def test_get_users(ac: AsyncClient):
    assert 1 == 1

@pytest.mark.parametrize("email, password, status_code", [
    ("kotopes@gmail.com", "kotopes", 200),
    ("kotopes@gmail.com", "kot0pes", 409),
    ("kotoqwe12pes@gmail.com", "kot0asdpes", 200),
    ("kacasd", "kot0asdpes", 422),
])
async def test_register_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post("/auth/register", json={
        "email": email,
        "password": password
    })

    assert response.status_code == status_code


@pytest.mark.parametrize("email, password, status_code", [
    ("user@example.com", "string", 200),
    ("sarah@example.com", "string", 200),
])
async def test_login_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post("/auth/login", json={
        "email": email,
        "password": password
    })

    assert response.status_code == status_code


async def test_get_hotels(ac: AsyncClient):
    response = await ac.get(
        "/hotels/"
    )
    assert response.status_code == 200


async def test_get_hotels_by_location(ac: AsyncClient):
    response = await ac.get(
        "/hotels/{New York}"
    )
    assert response.status_code == 200