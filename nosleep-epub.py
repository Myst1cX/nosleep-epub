# useful doc: https://pandoc.org/epub.html

import praw

BOOK_TITLE = "NoSleep EBook"
WRITER_NAME = "nosleep-epub-bot"

reddit = praw.Reddit(
    client_id="<your-reddit-app-client-id>",
    client_secret="<your-reddit-app-client-secret>",
    user_agent="<any-random-string-unique-to-your-app>",
)

subreddit = reddit.subreddit("nosleep")

indexPage = ""
remainingPages = ""
idx = 1

with open("dummy.txt", "w") as fo:
    fo.write("% " + BOOK_TITLE + "\n")
    fo.write("% " + WRITER_NAME + "\n")
    for submission in subreddit.top(time_filter="month"):
        indexPage += str(idx) + ". [" + submission.title + "]" + "(#" + str(idx) + ")\n"
        remainingPages += "<a name=" + str(idx) + "></a>\n\n"
        remainingPages += "## " + submission.title + "\n\n"
        remainingPages += submission.selftext + "\n\n"
        idx += 1

    fo.write(indexPage + "\n")
    fo.write(remainingPages)