import praw
from dotenv import load_dotenv
import os
import query_handler

load_dotenv()

def main():
    # Initialize values from dotenv to connect using Reddit API
    USER_AGENT = os.getenv("USER_AGENT")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    CLIENT_ID = os.getenv("CLIENT_ID")
    REDDIT_NAME = os.getenv("REDDIT_NAME")
    PASSWORD = os.getenv("PASSWORD")

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

    # Create a stream of comments for a subreddit
    for comment in praw.models.util.stream_generator(r.inbox.mentions, skip_existing=True):
        reply = comment_parser(comment)

# Parses a given comment to ensure that it's correctly formatted
# Simple comparison format: /u/username player1 player2
def comment_parser(comment):
    try:
        comment_tokens = comment.body.split(' ')
        start_index = comment_tokens.index("/u/" + os.getenv("REDDIT_NAME"))
        player1 = comment_tokens[start_index+1] + " " + comment_tokens[start_index+2]
        player2 = comment_tokens[start_index+3] + " " + comment_tokens[start_index+4]

        return "placeholder"
    except Exception as e:
        print(e)
        return "Sorry, I couldn't get that for you!"

if __name__ == "__main__":
    main()
