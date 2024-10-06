# EventsAPI

An event management API built with [FastAPI](https://fastapi.tiangolo.com) 🔥 and MongoDB.
I chose FastAPI for building EventsAPI primarily because of its speed and performance. FastAPI is one of the fastest web frameworks available, as it’s built on standard Python type hints, leveraging asyncio for high-performance asynchronous code execution.

> Made for SRMKZILLA club submission
## Check out the another task [ENV MANAGER](https://github.com/harsshhan/Env-Manager)

## Tech Stack

- **Backend**: FastAPI, a modern, fast (high-performance) web framework.
- **Database**: MongoDB for efficient document storage.
- **API Documentation**: Self-documented with OpenAPI and Swagger at `/docs`.

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- MongoDB (locally or hosted, e.g., MongoDB Atlas)
- [Pipenv](https://pipenv.pypa.io/en/latest/) or `pip` for installing dependencies

### Setup

1. Clone the repository:

```bash
git clone https://github.com/harsshhan/EventsAPI.git
cd EventsAPI
```

2. Setup Virtual Environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Create a .env file with the following content:

```bash
DB_URL=mongodb+srv://<your-username>:<your-password>@<your-cluster-url>/<your-database>?retryWrites=true&w=majority
DB_NAME=your-database-name
```
Make sure to replace the placeholders to with your MongoDB credentials



### Running the app

1. Run the App

```bash
uvicorn main:app --reload
```

## API Endpoints

`POST /events`
Create a new event. Requires a JSON body:

`GET /events/{id}`
Retrieve an event by its ID.

`PATCH /events/{id}`
Update an existing event by its ID. Requires a JSON body with updated details.

`DELETE /events/{id}`
Delete an event by its ID.

## [Documentation]()

The API is documented using OpenAPI. Access the Swagger UI for exploration:

- Swagger UI: `/docs`


## Docker

You can run the application using Docker. Make sure you have Docker and Docker Compose installed.

To build and run the containers, use:

```bash
docker compose up --build
```

## License

This project is licensed under the MPL 2.0 License.
