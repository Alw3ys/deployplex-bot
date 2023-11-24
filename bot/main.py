import openai
from dosei import Dosei
from fastapi import FastAPI, Response
from bot.config import Config

config = Config()
app = FastAPI()
dosei = Dosei()


def write_a_joke():
    response_result = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": config.prompt}],
    )
    config.tweepy_client.create_tweet(
        text=response_result.choices[0].message["content"]
    )


@app.post("/")
def post_a_joke() -> Response:
    write_a_joke()
    return Response()


@dosei.cron_job("0 9,13,17 * * *")
def tweet():
    write_a_joke()
