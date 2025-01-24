# python
import json
from urllib import parse, request
import os

from dotenv import load_dotenv

load_dotenv()

def api_calls(counter):
    api_key = os.environ.get('TOKEN')


    url = "http://api.giphy.com/v1/gifs/random"

    params = parse.urlencode({
    "q": "Anime",
    "api_key": api_key,
    "limit": "5",
    "rating" : "r"
    })

    with request.urlopen("".join((url, "?", params))) as response:
        body = response.read()

    main_body = json.loads(body)

    title = main_body['data']['title']
    url = main_body['data']['images']['downsized_large']['url']

    # print(main_body)

   
    if title == '':
        print('no title')
        print('creating a counter to create a gif name plus 1')
        counter += 1
        titleUnder = "anime" + "gif" + str(counter) + ".gif"
        print(titleUnder)
    elif title == ' ':
        print('space title')
        print('creating a counter to create a gif name plus 1')
        counter += 1
        titleUnder = "anime" + "gif" + str(counter) + ".gif"
            
        print(titleUnder)
    else:
            titleUnder = title.replace(" ", "_") + ".gif"
            print(titleUnder)
    print(title)
    print(url)


counter = 1
for x in range(10):
  print(x)
  api_calls(counter)
  

# titleUnder = title.replace(" ", "_") + ".gif"


# print(titleUnder)
#   data = json.loads(response.read())
#   encoding = response.info().get_content_charset('utf-8')
#   test = json.loads(data.decode(encoding))
# print(test)


#   data = response.json()
#   print(data)
# dumps = json.dumps(data, sort_keys=True, indent=4)
# url = dumps[0][data]
# print(url)
# print(json.dumps(data, sort_keys=True, indent=4))


# if title is not None:
#     titleUnder = title.replace(" ", "_") + ".gif"
#     print(titleUnder)
# else:
#   print("no_name.gif")