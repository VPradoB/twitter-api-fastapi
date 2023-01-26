from typing import List
from uuid import UUID

from fastapi import FastAPI
from fastapi import status

from models.tweet import Tweet
from models.user import UserLogin, User

app = FastAPI()


# Authorization ep
@app.post(path="/signin", response_model=User, status_code=status.HTTP_200_OK, tags=['Authorization'])
def signin(user: UserLogin):
    return {"user": user}


@app.post(path="/signup", response_model=User, status_code=status.HTTP_201_CREATED, tags=['Authorization'])
def signup():
    pass


# user endpoints
@app.get(path="/users", response_model=List[User], status_code=status.HTTP_200_OK, tags=['User'])
def index_user():
    pass


@app.get(path="/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK, tags=['User'])
def show_user(user_id: UUID):
    pass


@app.delete(path="/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK, tags=['User'])
def delete_user(user_id: UUID):
    pass


@app.put(path="/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK, tags=['User'])
def index_user(user_id: UUID):
    pass


# Tweet endpoints
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    tags=['Tweet'],
    summary="Get all tweets"
)
def home():
    return {"twitter API": "working..."}


@app.get(path="/tweets", response_model=List[Tweet], status_code=status.HTTP_200_OK, tags=['Tweet'])
def index_tweet():
    pass


@app.get(path="/tweets/{tweet_id}", response_model=Tweet, status_code=status.HTTP_200_OK, tags=['Tweet'])
def show_tweet(tweet_id: UUID):
    pass


@app.post(
    path="/tweets",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    tags=['Tweet'],
    summary="Store a new tweet"
)
def home():
    return {"twitter API": "working..."}


@app.put(path="/tweets/{tweet_id}", response_model=Tweet, status_code=status.HTTP_200_OK, tags=['Tweet'])
def index_tweet(tweet_id: UUID):
    pass


@app.delete(path="/tweets/{tweet_id}", response_model=Tweet, status_code=status.HTTP_200_OK, tags=['Tweet'])
def delete_tweet(tweet_id: UUID):
    pass
