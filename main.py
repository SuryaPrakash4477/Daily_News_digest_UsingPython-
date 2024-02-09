import requests

url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-01-09&sortBy=publishedAt&apiKey=" \
      "0f386d02df7849d9a94be18d4aaf12cc"
# Passing the keuy of API
api_key = "0f386d02df7849d9a94be18d4aaf12cc"
request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])