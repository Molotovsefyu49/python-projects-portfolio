import requests
from email_send import send_email
from functions import get_prev_month_date
from dotenv import load_dotenv
import os

load_dotenv()

topic = "tesla"

api_key = os.getenv("APIKEY")

prev_date = get_prev_month_date()
url1 = f"https://newsapi.org/v2/everything?q={topic}" \
       f"&from={prev_date}&sortBy=publishedAt&" \
       f"apiKey={api_key}"

# Make request
request = requests.get(url1)

# Get a dictionary with data
content = request.json()

body = "Subject: Today's news" + "\n"
# Access the article titles and description
for article in content["articles"][:20]:
    if article['title'] is not None:
        body = body + article["title"] + "\n"\
               + article["description"] + "\n"\
               + article["url"] + 2*"\n"

body = body.encode("utf8")
send_email(message=body)