import openai
from fastapi import FastAPI, Response, Depends
from bot.config import Config
from deployplex.integrations.fastapi import cron_job_auth

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
def read_root(auth: None = Depends(cron_job_auth)) -> Response:
    return Response()
