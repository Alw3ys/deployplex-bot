import openai
from dosei import Dosei
from fastapi import FastAPI, Response
from bot.config import Config

config = Config()
app = FastAPI()
dosei = Dosei()


@app.post("/")
def post_root() -> Response:
    return Response()


@dosei.cron_job("0 9,13,17 * * *")
def tweet():
    response_result = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": config.prompt}],
    )
    config.tweepy_client.create_tweet(
        text=response_result.choices[0].message["content"]
    )
