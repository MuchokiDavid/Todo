# Todo App

This is a simple Todo application built with React frontend and Flask backend, featuring authentication using JWT for resource authorization.

## Technologies Used

- React
- Flask
- Bootstrap
- Tailwind CSS
- REST API
- JWT (JSON Web Tokens)

## Features

- User authentication with JWT
- CRUD operations for managing todos
- Responsive design using Bootstrap and Tailwind CSS
- RESTful API endpoints for interacting with the backend

## Getting Started

### Prerequisites

- Node.js
- Python
- Flask
- Pipenv (optional)

### Installation

1. Clone the repository:

```bash

git clone https://github.com/muchokidavid/todo-app.git
cd todo-app
```

2. Install dependencies for frontend:

```bash
cd frontend
npm install
```

3. Install dependencies for backend:

```bash
cd ../backend
pip install -r requirements.txt
```

## Configuration

1. Set up environment variables:

    - Create a .env file in the backend directory.
    - Define the following variables in the .env file:
        - SECRET_KEY: Secret key for JWT token encryption.
        - DATABASE_URL: Connection URL for your database.

## Usage

1. Start the backend server:

```bash
cd backend
python app.py
```

2. Start the frontend server:

```bash
cd ../frontend
npm start
```

3. Open your web browser and navigate to http://localhost:3000 to access the Todo app.

## API Endpoints

- POST /register: Register a new user.
- POST /login: Login and receive JWT token.
- GET /todos: Retrieve all todos.
- GET /todos/:id: Retrieve a specific todo by ID.
- POST /todos: Create a new todo.
- PUT /todos/:id: Update an existing todo by ID.
- DELETE /todos/:id: Delete a todo by ID.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues if you encounter any bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License.

## Author

- David Muchoki