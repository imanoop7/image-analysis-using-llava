import ollama
from ollama import generate

import glob
import pandas as pd
from PIL import Image

import os
from io import BytesIO




# processing the images 
def process_image(image_file):
    print(f"\nProcessing {image_file}\n")
    with Image.open(image_file) as img:
        with BytesIO() as buffer:
            img.save(buffer, format='PNG')
            image_bytes = buffer.getvalue()

    full_response = ''
    # Generate a description of the image
    for response in generate(model='llava', 
                             prompt='describe this image and make sure to include anything notable about it (include text you see in the image):', 
                             images=[image_bytes], 
                             stream=True):
        # Print the response to the console and add it to the full response
        print(response['response'], end='', flush=True)
    


process_image("image.png")

    



