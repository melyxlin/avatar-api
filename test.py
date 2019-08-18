import pytest
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
