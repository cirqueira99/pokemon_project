from typing import List

from fastapi.testclient import TestClient
from sqlalchemy import create_engine, true
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from server.main import app
from server.schemas.trainer_schema import TrainerResponse
from server.sqlalchemy.config.database import get_db, Base


SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/db-postgres'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def test_create_trainer():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    new_tainer = {
        "name": "Henrique Test",
        "insignias": ["teste01", "teste02"],
        "leader_gym": True,
        "qt_pokemons": 5,
        "password": "teste123"
    }

    new_trainer_copy = new_tainer.copy()
    new_trainer_copy['id'] = 1

    response = client.post('/api/trainer/create', json=new_tainer)

    assert response.status_code == 200
    assert response.json() == new_trainer_copy


def test_get_trainer_all():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    new_tainer1 = {
        "name": "Henrique Test",
        "insignias": ["teste01", "teste02"],
        "leader_gym": True,
        "qt_pokemons": 10,
        "password": "teste123"
    }
    new_tainer2 = {
        "name": "Pedro Test",
        "insignias": ["teste01", "teste02"],
        "leader_gym": True,
        "qt_pokemons": 10,
        "password": "teste123"
    }

    client.post('/api/trainer/create', json=new_tainer1)
    client.post('/api/trainer/create', json=new_tainer2)

    response = client.get('/api/trainer/list')

    response_planed = [
        {"name": "Henrique Test", "insignias": ["teste01", "teste02"], "leader_gym": True, "qt_pokemons": 10, "password": "teste123", "id": 1},
        {"name": "Pedro Test", "insignias": ["teste01", "teste02"], "leader_gym": True, "qt_pokemons": 10, "password": "teste123", "id": 2}
    ]

    assert response.status_code == 200
    assert response.json() == response_planed
