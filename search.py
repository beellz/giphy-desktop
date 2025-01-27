# import TenGiphPy
# # import json
# import requests
# import time
# import os
# from dotenv import load_dotenv

# load_dotenv()

# api_key = os.environ.get('TOKEN')


# def call():
#     g = TenGiphPy.Giphy(token=api_key)

#     response = g.search(tag="Anime")
#     print(response)   

#     # Extract title and URL
#     # title = response['title']
#     # url = response['images']['downsized_large']['url']
#     # print("Title:", title)
#     # print("URL:", url)




# call()


# python
import json
from urllib import parse, request
import os
from dotenv import load_dotenv

load_dotenv()

def api_calls():
    api_key = os.environ.get('TOKEN')


    url = "http://api.giphy.com/v1/gifs/search"

    params = parse.urlencode({
    "q": "Anime",
    "api_key": api_key,
    "limit": "5",
    "rating" : "r",
    "lang" : "eng",
    "bundle" : "messaging_non_clips"
    })

    with request.urlopen("".join((url, "?", params))) as response:
        body = response.read()

    main_body = json.loads(body)
    # print(main_body)

    dumps = json.dumps(main_body, sort_keys=True, indent=4)
    print(dumps)

    all_url = []
    for i in dumps:
        jump = dumps[data][i][images][url]
        all_url = jump.append
    

    print(all_url)
    # title = main_body['data']['title']
    # url = main_body['data']['images']['downsized_large']['url']

api_calls()