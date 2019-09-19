import praw
from dotenv import load_dotenv
import os
load_dotenv()


if __name__ == "__main__":
    # Initialize values from dotenv to connect using Reddit API
    USER_AGENT = os.getenv("USER_AGENT")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    CLIENT_ID = os.getenv("CLIENT_ID")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")

    # Get Reddit Instance
    r = None
    try:
        r = praw.Reddit(user_agent=USER_AGENT,
                        client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        username=USERNAME,
                        password=PASSWORD)
    except Exception as e:
        print(e)
