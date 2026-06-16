import os
import sys
import praw

reddit = praw.Reddit(
    client_id=os.environ.get("reddit_id"),
    client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
    user_agent=os.environ.get("REDDIT_USER_AGENT", "LocalEsportsAggregator/1.0"),
    username=os.environ.get("REDDIT_USERNAME"),
    password=os.environ.get("REDDIT_PASSWORD")
)

target_subreddits = ["gaming", "esports","PS5","Playstation","Dropshipping"]

def fetch_and_aggregate():
    for sub_name in target_subreddits:
        try:
            subreddit = reddit.subreddit(sub_name)
            for submission in subreddit.hot(limit=10):
                if not submission.is_self:
                    continue
                print(f"Subreddit: {sub_name}")
                print(f"Title: {submission.title}")
                print(f"Content: {submission.selftext[:300]}")
                print("-" * 50)
        except Exception as e:
            print(f"Error accessing {sub_name}: {e}", file=sys.stderr)

if __name__ == "__main__":
    fetch_and_aggregate()