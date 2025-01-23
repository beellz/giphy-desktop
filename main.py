import TenGiphPy
import json
import requests

# Initialize Giphy API with your token
g = TenGiphPy.Giphy(token='$TOKEN')

# Fetch a random GIF with the tag "Anime"
response = g.random(tag="Anime")['data']

# Extract title and URL
title = response['title']
url = response['images']['downsized_large']['url']

# Print title and URL
print("Title:", title)
print("URL:", url)

# Function to download image from URL
def download_image(image_url, image_title):
    # Send a GET request to the image URL
    response = requests.get(image_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Create a valid filename by replacing spaces with underscores and removing special characters
        filename = f"{image_title.replace(' ', '_')}.gif"  # Save as .gif since it's a GIF

        # Open a file in write-binary mode and save the image content
        with open(filename, 'wb') as file:
            file.write(response.content)
        
        print(f"Image '{filename}' downloaded successfully!")
    else:
        print("Failed to download image. Status code:", response.status_code)

# Download the image using the extracted URL and title
download_image(url, title)
