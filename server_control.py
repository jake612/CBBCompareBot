import praw
from dotenv import load_dotenv
import os
load_dotenv()


if __name__ == "__main__":
    # Initialize values from dotenv to connect using Reddit API
    USER_AGENT = os.getenv("USER_AGENT")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    CLIENT_ID = os.getenv("CLIENT_ID")
    REDDIT_NAME = os.getenv("REDDIT_NAME")
    PASSWORD = os.getenv("PASSWORD")

    print(USER_AGENT + ", " + REDDIT_NAME + ", " + PASSWORD)

    # Get Reddit Instance
    r = None
    try:
        r = praw.Reddit(user_agent=USER_AGENT,
                        client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        username=REDDIT_NAME,
                        password=PASSWORD)
    except Exception as e:
        print(e)

    user = r.redditor("spez")

    karma_by_subreddit = {}
    for thing in user.submissions.top("all"):
        subreddit=thing.subreddit.display_name
        karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0) + thing.score)

    print(karma_by_subreddit)
