import os
from PIL import Image

# Set the directory path
directory = "."

# Loop through all the files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        # Open the image file
        image = Image.open(os.path.join(directory, filename))

        # Resize the image to 800x600 pixels
        image = image.resize((1000, 700))

        # Save the resized image
        image.save(os.path.join(directory, filename))

