# Define the dance moves and their effects
dance_moves_effects = {
    ('Twirl', 'Twirl'): 'Fireflies light up the forest.',
    ('Leap', 'Spin'): 'Gentle rain starts falling.',
    ('Spin', 'Leap'): 'A rainbow appears in the sky.',
    ('Twirl', 'Spin'): 'A gust of wind blows through the forest.',
    ('Spin', 'Twirl'): 'The forest is filled with a beautiful melody.',
    ('Leap', 'Twirl'): 'A flurry of leaves dances in the air.',
    ('Twirl', 'Leap'): 'A shower of petals rains down.',
    ('Spin', 'Spin'): 'A misty fog envelops the forest.',
    ('Leap', 'Leap'): 'A chorus of birds begins to sing.'
}

print("Start")

# Define the dance sequences for Lox and Drako
lox_moves = ['Twirl', 'Leap', 'Spin', 'Twirl', 'Leap']
drako_moves = ['Spin', 'Twirl', 'Leap', 'Leap', 'Spin']

# Iterate over the sequences
for i in range(5):
    # Get the dance moves for this sequence
    lox_move = lox_moves[i]
    drako_move = drako_moves[i]

    # Look up the effect of these dance moves
    effect = dance_moves_effects.get((lox_move, drako_move))

    # Print the state of the forest after this sequence
    print(f'After sequence {i+1}, {effect}')

import requests
from PIL import Image
import io

def get_dalle_image(text):
    # Replace with the actual DALLE-3 API endpoint
    #url = "https://sbp-gctfs-offsite24-oai.openai.azure.com/openai/deployments/dalle3/images/generate?api-version=1.0"
    url = "https://sbp-gctfs-offsite24-oai.openai.azure.com/openai/deployments/dalle3/images/generations?api-version=2023-12-01-preview"

    # Define the headers for the request, including the API key
    headers = {
        "API-Key": "YOUR_API_KEY",
    }

    # Send a POST request to the DALLE-3 API
    response = requests.post(url, json={"prompt": text}, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Convert the response content to an image
        image = Image.open(io.BytesIO(response.content))
        return image
    else:
        print(f"Request failed with status code {response.status_code}")
        return None
    
# Iterate over the sequences
for i in range(5):
    # Get the dance moves for this sequence
    lox_move = lox_moves[i]
    drako_move = drako_moves[i]

    # Look up the effect of these dance moves
    effect = dance_moves_effects.get((lox_move, drako_move))

    # Get the DALLE-3 image for this effect
    image = get_dalle_image(effect)

    # Display the image
    if image is not None:
        image.show()

    # Print the state of the forest after this sequence
    print(f'After sequence {i+1}, {effect}')
