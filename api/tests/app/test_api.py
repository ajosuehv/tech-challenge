"""
This file (test_books.py) contains the functional tests for the `books` blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the `books` blueprint.
"""
import os
import re
import pytest

from api.app import create_app
from api.database import db
from uuid import UUID

def test_healthcheck():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get('/health-check')
        json_resp = response.get_json()
        assert response.status_code == 200
        assert json_resp["message"] == 'Process running!'

def test_create_product():
    flask_app = create_app()
    data = {
            "name":"Producto 6",
            "price":21.00,
            "cost":4
            }
    with flask_app.test_client() as test_client:
        response = test_client.post('/api/products',json=data)
        print(response)
        json_resp = response.json
        
        assert response.status_code == 200
        assert json_resp["name"] == data["name"]
        assert json_resp["cost"] == data["cost"]
        assert json_resp["price"] == data["price"]
        assert UUID(json_resp["sku"], version=4)
        
def test_update_product_stock():
    flask_app = create_app()
    data = {
            "name":"Producto X",
            "price":21.00,
            "cost":4
            }
    with flask_app.test_client() as test_client:
        response = test_client.post('/api/products',json=data)
        json_resp = response.json
        
        assert response.status_code == 200
        assert json_resp["name"] == data["name"]
        assert json_resp["cost"] == data["cost"]
        assert json_resp["price"] == data["price"]
        assert UUID(json_resp["sku"], version=4)


