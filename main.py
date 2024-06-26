import requests
from send_email import send_email

topic = "tesla"

url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-01-09&sortBy=publishedAt&apiKey=" \
      "0f386d02df7849d9a94be18d4aaf12cc" \
      "&langauge=en"
# Passing the keuy of API
api_key = "0f386d02df7849d9a94be18d4aaf12cc"
request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"][:20]:
      body = "Subject: Today's News" + \
            "\n" + body + str(article["title"]) + "\n" \
             + str(article["description"]) \
             + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)