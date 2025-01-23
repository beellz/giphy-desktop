import TenGiphPy
import json

# Initialize Giphy API with your token
g = TenGiphPy.Giphy(token='*')

# Fetch a random GIF with a specific tag
# response = g.random(tag="Anime")

# Print the response in JSON format
# print(json.dumps(response, indent=4))

# url = json.dumps(response, indent=4)
# get all the json url 


response = g.random(tag="Anime")['data'] 
# print(g.random(tag="Anime")['data']['images']['downsized_large']['url'])

# print (rest)

title = json.dumps(response['title'], indent=4)
url = json.dumps(response['images']['downsized_large']['url'], indent=4)

print(title)
print(url)




# # t = TenGiphPy.Tenor(token='APITOKEN')
# g = TenGiphPy.Giphy(token='6jWDfEh91JLdGgem0GqBRKSzo86dcODl')

# #sync
# # print(t.random("GIFTAG"))



# print(g.random(tag="Anime"))

# get the list of tags

# tags = [ 'anime', 'anime_smoking', 'nature', 'cars' ]

# for i in tags:
#     print(i)
#     print(g.random(tag=i)[])











# get the output of tags using loop 
#run everything on func
# make sure to get the json file 
# get the key out of the json file 
# store the key on one of the file 
