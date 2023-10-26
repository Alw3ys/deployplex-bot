import openai
from fastapi import FastAPI, Response
from bot.config import Config

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
