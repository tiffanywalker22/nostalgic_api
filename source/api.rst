API Documentation
=================

Overview
--------

This API provides access to the data in the `bedrooms` table of the PostgreSQL database. It allows users to retrieve information about bedrooms through a RESTful endpoint.

Dependencies
------------

- `Flask`: A lightweight WSGI web application framework for Python.
- `psycopg2`: A PostgreSQL adapter for Python.
- `logging`: Python's built-in logging module for logging messages.

Endpoints
---------

### `/bedrooms`

**Method:** `GET`

**Description:**
Retrieves a list of all bedrooms from the `bedrooms` table in the PostgreSQL database.

**Response:**
- **Status Code:** `200 OK`
- **Content-Type:** `application/json`
- **Body:** A JSON array of bedroom objects, where each object contains:
- `bedroom_id`: An integer representing the unique ID of the bedroom.
- `title`: The title of the bedroom.
- `description`: A text description of the bedroom.
- `img_src`: The URL or path to an image of the bedroom.