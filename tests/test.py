import pytest
import json
from flask import Flask
from project import *

@pytest.fixture
def client():
    client = app.test_client()
    return client

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200

def test_about_page(client):
    response = client.get("/about")
    assert response.status_code == 200

def test_docs_page(client):
    response = client.get("/docs")
    assert response.status_code == 200

def test_all_characters_api(client):
    response = client.get("/characters")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 19

def test_all_locations_api(client):
    response = client.get("/locations")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 4
