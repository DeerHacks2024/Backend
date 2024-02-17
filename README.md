# DeerHacks 2024 API Documentation 🦌🔒

Welcome to the DeerHacks 2024 API documentation! This API provides endpoints to interact with event data including retrieval, insertion, updating, and deletion of events and attendees.

## Base URL

The base URL for accessing the API locally is:

```
http://localhost:5000/
```

## Endpoints

### Retrieve All Events

Retrieve all events stored in the database.

- **URL:** `/retrieve`
- **Method:** `GET`
- **Response:** JSON object containing all event data.

### Retrieve Events by Category

Retrieve events by specifying a category.

- **URL:** `/retrieve/<category>`
- **Method:** `GET`
- **Params:** `category` - The category of events to retrieve.
- **Response:** JSON object containing events in the specified category.

### Insert Event

Insert a new event into the database.

- **URL:** `/insert`
- **Method:** `POST`
- **Request Body:** JSON object representing the event to be inserted.
- **Response:** JSON object confirming the successful insertion of the event.

### Add Attendee to Event

Add an attendee to a specific event.

- **URL:** `/add-attendee`
- **Method:** `POST`
- **Request Body:** JSON object containing the `_id` of the event and the name of the attendee.
- **Response:** JSON object confirming the successful addition of the attendee to the event.

### Update Event

Update an existing event in the database.

- **URL:** `/update`
- **Method:** `POST`
- **Request Body:** JSON object representing the updated event data including the `_id` of the event to update.
- **Response:** JSON object confirming the successful update of the event.

### Delete Event

Delete an event from the database.

- **URL:** `/delete`
- **Method:** `DELETE`
- **Request Body:** JSON object containing the `_id` of the event to delete.
- **Response:** JSON object confirming the successful deletion of the event.

### Delete Event by ID

Delete an event from the database by specifying its ID.

- **URL:** `/delete/<id>`
- **Method:** `DELETE`
- **Params:** `id` - The ID of the event to delete.
- **Response:** JSON object confirming the successful deletion of the event.

## Error Handling

The API returns appropriate error messages and status codes for invalid requests or operations that fail.

- **400 Bad Request:** Invalid request format.
- **404 Not Found:** Event not found.

## Running the Server

To run the server locally, execute the following command:

```bash
python app.py
```

## Requirements

Ensure you have the dependencies installed 

You can install them via pip:

```bash
pip install -r requirements.txt
```