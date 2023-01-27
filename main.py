import json
from datetime import datetime
from typing import List
from uuid import UUID

from fastapi import FastAPI, Body, HTTPException
from fastapi import status

from models.tweet import Tweet, TweetCreate, TweetInDB
from models.user import UserLogin, User, UserRegister

app = FastAPI()


# Authorization ep
@app.post(path="/signin", response_model=User, status_code=status.HTTP_200_OK, tags=['Authorization'])
def signin(user: UserLogin):
    with open('users.json', 'r', encoding='utf-8-sig') as f:
        users = json.load(f)
        for u in users:
            if u['email'] == user.email and u['password'] == user.password:
                return u
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")


@app.post(path="/signup", response_model=User, status_code=status.HTTP_201_CREATED, tags=['Authorization'])
def signup(user: UserRegister = Body(...)):
    """
     Sign up a new user
     This endpoint is used to create a new user

    :param user: UserRegister

    :return:
        user (User)
    """
    with open('users.json', 'r+', encoding='utf-8-sig') as f:
        users = json.load(f)
        user_dict = user.dict()
        user_dict['id'] = str(user_dict['id'])
        user_dict['birthdate'] = str(user_dict['birthdate'])
        users.append(user_dict)

        f.seek(0)
        json.dump(users, f, indent=4)
        f.truncate()
        return user_dict


# user endpoints
@app.get(path="/users", response_model=List[User], status_code=status.HTTP_200_OK, tags=['User'])
def index_user():
    """
    Get all users

    :return:
        List[User]
    """
    with open('users.json', 'r', encoding='utf-8-sig') as f:
        users = json.load(f)
        return users


@app.get(path="/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK, tags=['User'])
def show_user(user_id: UUID):
    """
    Show one user by id

    :param user_id:

    :return:
        User
    """
    with open('users.json', 'r', encoding='utf-8-sig') as f:
        users = json.load(f)
        for user in users:
            if user['id'] == str(user_id):
                return user


@app.delete(path="/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK, tags=['User'])
def delete_user(user_id: UUID):
    """
    Delete one user by id

    :param user_id:

    :return:
        User
    """
    with open('users.json', 'r+', encoding='utf-8-sig') as f:
        users = json.load(f)
        for user in users:
            if user['id'] == str(user_id):
                users.remove(user)
                f.seek(0)
                json.dump(users, f, indent=4)
                f.truncate()
                return user


@app.put(path="/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK, tags=['User'])
def update_user(user_id: UUID, user: UserRegister = Body(...)):
    """
    Update one user by id

    :param user:
    :param user_id:

    :return:
        User
    """
    with open('users.json', 'r+', encoding='utf-8-sig') as f:
        users = json.load(f)
        for u in users:
            if u['id'] == str(user_id):
                u['first_name'] = user.first_name
                u['last_name'] = user.last_name
                u['birthdate'] = str(user.birthdate)
                f.seek(0)
                json.dump(users, f, indent=4)
                f.truncate()
                return u


# Tweet endpoints
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    tags=['Tweet'],
    summary="Get all tweets"
)
def home():
    with open('tweets.json', 'r', encoding='utf-8-sig') as f:
        tweets = json.load(f)
        return tweets


@app.get(path="/tweets/{tweet_id}", response_model=Tweet, status_code=status.HTTP_200_OK, tags=['Tweet'])
def show_tweet(tweet_id: UUID):
    with open('tweets.json', 'r', encoding='utf-8-sig') as f:
        tweets = json.load(f)
        for tweet in tweets:
            if tweet['id'] == str(tweet_id):
                return tweet


@app.post(
    path="/tweets",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    tags=['Tweet'],
    summary="Store a new tweet"
)
def store_tweets(tweet: TweetCreate = Body(...)):
    with open('tweets.json', 'r+', encoding='utf-8-sig') as f:
        with open('users.json', 'r', encoding='utf-8-sig') as f2:
            tweets: List[TweetInDB] = json.load(f)
            users: List[User] = json.load(f2)

            new_tweet = tweet.dict()
            new_tweet['id'] = str(new_tweet['id'])
            new_tweet['user_id'] = str(new_tweet['user_id'])
            new_tweet['created_at'] = str(datetime.now())
            new_tweet['updated_at'] = str(datetime.now())

            if new_tweet['user_id'] not in [user['id'] for user in users]:
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="User id does not exist")

            if new_tweet['id'] in [tweet['id'] for tweet in tweets]:
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Tweet id already exist")

            tweets.append(new_tweet)
            f.seek(0)
            json.dump(tweets, f, indent=4)
            f.truncate()

            return new_tweet


@app.put(path="/tweets/{tweet_id}", response_model=Tweet, status_code=status.HTTP_200_OK, tags=['Tweet'])
def update_tweet(tweet_id: UUID):
    """
    :param tweet_id:
    :return:
        Tweet
    """
    with(open('tweets.json', 'r+', encoding='utf-8-sig')) as f:
        tweets = json.load(f)
        for tweet in tweets:
            if tweet['id'] == str(tweet_id):
                tweet['content'] = 'Updated content'
                tweet['updated_at'] = str(datetime.now())
                f.seek(0)
                json.dump(tweets, f, indent=4)
                f.truncate()
                return tweet


@app.delete(path="/tweets/{tweet_id}", response_model=Tweet, status_code=status.HTTP_200_OK, tags=['Tweet'])
def delete_tweet(tweet_id: UUID):
    """
    :param tweet_id:
    :return:
        Tweet
    """
    with(open('tweets.json', 'r+', encoding='utf-8-sig')) as f:
        tweets = json.load(f)
        for tweet in tweets:
            if tweet['id'] == str(tweet_id):
                tweets.remove(tweet)
                f.seek(0)
                json.dump(tweets, f, indent=4)
                f.truncate()
                return tweet
