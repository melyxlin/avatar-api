import pytest
import json
from flask import Flask
from project import *

@pytest.fixture
def client():
    client = app.test_client()
    return client

def test_home_page(client):
    """
    GIVEN a Flask Application
    WHEN the '/' is requested
    THEN check if the response is valid
    """
    response = client.get("/")
    assert response.status_code == 200

def test_about_page(client):
    """
    GIVEN a Flask Application
    WHEN the '/about' is requested
    THEN check if the response is valid
    """
    response = client.get("/about")
    assert response.status_code == 200

def test_docs_page(client):
    """
    GIVEN a Flask Application
    WHEN the 'docs' is requested
    THEN check if the response is valid
    """
    response = client.get("/docs")
    assert response.status_code == 200

def test_all_characters_api(client):
    """
    GIVEN a Flask Application
    WHEN the '/characters' is requested
    THEN check if the response is valid
    AND check if the amount of data returns equal the amount of data in the file
    """
    response = client.get("/characters")
    data = json.loads(response.data)
    assert len(data) == 19 and response.status_code == 200

def test_all_locations_api(client):
    """
    GIVEN a Flask Application
    WHEN the '/locations' is requested
    THEN check if the response is valid
    AND check if the amount of data returns equal the amount of data in the file
    """
    response = client.get("/locations")
    data = json.loads(response.data)
    assert response.status_code == 200 and len(data) == 4

def test_all_bendings_api(client):
        """
        GIVEN a Flask Application
        WHEN the '/bendings' is requested
        THEN check if the response is valid
        """
        response = client.get("/bendings")
        data = json.loads(response.data)
        assert response.status_code ==200

def test_characters_filters_api(client):
    """
    GIVEN a Flask Application
    WHEN the '/characters' is requested
    AND a param is provided
    AND a value is provided
    THEN check if the response is valid
    """
    filters = {"benders":"Waterbending",  "gender":"Male", "ethnicity":"Earth%20Kingdom", "nationality":"Fire%20Nation", "affiliations":"Team%20Avatar"}
    for filter in filters:
        URL = "/characters/" + filter + "/" + filters.get(filter)
        response = client.get(URL)
        assert response.status_code == 200

def test_locations_filters_api(client):
    """
    GIVEN a Flask Application
    WHEN the '/locations' is requested
    AND a param is provided
    AND a value is provided
    THEN check if the response is valid
    """
    filters = {"nation":"Earth%20Kingdom"}
    for filter in filters:
        URL = "/locations/" + filter + "/" + filters.get(filter)
        response = client.get(URL)
        assert response.status_code == 200