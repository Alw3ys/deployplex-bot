import openai
from fastapi import FastAPI, Response, Depends
from bot.config import Config
from bot.cron_auth import authenticate_request

config = Config()
app = FastAPI()


@app.post("/")
def read_root() -> Response:
    response_result = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": config.prompt}],
    )
    config.tweepy_client.create_tweet(
        text=response_result.choices[0].message["content"]
    )
    return Response()


@app.post("/auth")
def read_root(auth: None = Depends(authenticate_request)) -> Response:
    return Response()
