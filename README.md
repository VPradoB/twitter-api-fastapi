# Twitter Clone 
A Twitter clone built with Domain-Driven Design (DDD) and Clean Architecture principles, using FastAPI and SQLite as the database.

## Future Features
- User registration and login
- Creating and managing tweets
- Following and unfollowing users
- Viewing tweets from followed users in a timeline

## Tech Stack
- FastAPI for the web framework
- SQLite as the database
- DDD and Clean Architecture for software design

## Prerequisites
- Python 3.6+
- pipenv for package management

## Getting Started
1. Clone the repository
`git clone https://github.com/VPradoB/twitter-api-fastapi.git`

2. Navigate to the project directory `cd twitter-api-fastapi`

3. Install dependencies `pipenv install`

4. Set environment variables `cp .env.example .env`

5. Run the application `pipenv run uvicorn app.main:app --reload`
The application should now be running at http://localhost:8000.

## Contributing
Contributions are welcome! Please open a pull request or an issue if you would like to contribute.
