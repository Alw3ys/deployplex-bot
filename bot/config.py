import os

import openai
import tweepy
from dotenv import load_dotenv


class Config:
    _self = None
    _initialized = False

    prompt = """
    You are an AI bot for X (previously Twitter), operated by DeployPlex.
    About DeployPlex: It's the go-to FastAPI platform, providing vector db hosting, monitoring, and more.
    Your traits: A Python, FastAPI and DeployPlex enthusiast, you believe AGI will emerge from Python, perhaps Mojo.
    Your task: Share a daily humorous, sarcastic developer-focused message without using hashtags; MUST be one to two sentences max, be concise.
    When replying to users, leverage their background for humor. Be edgy, but never discriminatory.
    """

    def __new__(cls):
        if cls._self is None:
            cls._self = super(Config, cls).__new__(cls)
        return cls._self

    def __init__(self):
        if self._initialized:
            return
        load_dotenv()

        openai.api_key = os.getenv("OPENAI_API_KEY")

        self.tweepy_client = tweepy.Client(
            consumer_key=os.getenv("CONSUMER_KEY"),
            consumer_secret=os.getenv("CONSUMER_SECRET"),
            access_token=os.getenv("ACCESS_TOKEN"),
            access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
        )

        self._initialized = True
