import pytest
import json
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
    if response.status_code != 200:
            raise AssertionError()

def test_about_page(client):
    """
    GIVEN a Flask Application
    WHEN the '/about' is requested
    THEN check if the response is valid
    """
    response = client.get("/about")
    if response.status_code != 200:
            raise AssertionError()

def test_docs_page(client):
    """
    GIVEN a Flask Application
    WHEN the 'docs' is requested
    THEN check if the response is valid
    """
    response = client.get("/docs")
    if response.status_code != 200:
            raise AssertionError()

def test_all_characters_api(client):
    """
    GIVEN a Flask Application
    WHEN the '/characters' is requested
    THEN check if the response is valid
    AND check if the amount of data returns equal the amount of data in the file
    """
    response = client.get("/characters")
    data = json.loads(response.data)
    if len(data) != 19 or response.status_code != 200:
            raise AssertionError()

def test_all_locations_api(client):
    """
    GIVEN a Flask Application
    WHEN the '/locations' is requested
    THEN check if the response is valid
    AND check if the amount of data returns equal the amount of data in the file
    """
    response = client.get("/locations")
    data = json.loads(response.data)
    if response.status_code != 200 or len(data) != 4:
            raise AssertionError()

def test_all_bendings_api(client):
        """
        GIVEN a Flask Application
        WHEN the '/bendings' is requested
        THEN check if the response is valid
        """
        response = client.get("/bendings")
        data = json.loads(response.data)
        if response.status_code != 200 and len(data) == 4:
                raise AssertionError()

def test_character_api(client):
        """
         GIVEN a Flask Application
         WHEN the '/characters' is requested
         AND a name is provided
         THEN check if the response is valid
         AND check if the response has only one character
        """
        name = "Katara"
        response = client.get("/characters/"+name)
        data = [json.loads(response.data)]
        if response.status_code != 200 and len(data) != 1:
                raise AssertionError()

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
        if response.status_code != 200:
                 raise AssertionError()

def test_characters_filter_api_error(client):
        """
        GIVEN a Flask Application
        WHEN the '/characters' is requested
        AND a param is provided
        AND a bad value is provided
        THEN check if the response is not valid
        """
        filters = {"benders":"Hello",  "gender":"Hello", "ethnicity":"Hello", "nationality":"Hello", "affiliations":"Hello"}
        for filter in filters:
                URL = "/characters/" + filter + "/" + filters.get(filter)
                response = client.get(URL)
                if response.status_code != 404:
                         raise AssertionError()

def test_location_api(client):
        name = "Ember%20Island"
        response = client.get("/locations/"+name)
        data = [json.loads(response.data)]
        if response.status_code != 200 and len(data) != 1:
                 raise AssertionError()

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
        if response.status_code != 200:
                 raise AssertionError()

def test_locations_filters_api_error(client):
    """
    GIVEN a Flask Application
    WHEN the '/locations' is requested
    AND a param is provided
    AND a bad value is provided
    THEN check if the response is not valid
    """
    URL = "/locations/nation/hello"
    response = client.get(URL)
    if response.status_code != 404:
            raise AssertionError()

def test_bending_api(client):
    """
    GIVEN a Flask Application
    WHEN the '/bendings' is requested
    AND a name is provided
    THEN check if the response is valid
    """
    name = "Earthbending"
    response = client.get("/bendings/"+name)
    data = [json.loads(response.data)]
    if response.status_code != 200 and len(data) != 1:
             raise AssertionError()