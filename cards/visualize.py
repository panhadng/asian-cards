import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt


def visualize_cards(cards, rows, cols):
    # Set up the figure for specified rows and columns
    size = (cols * 2, rows * 2)  # Adjust size based on rows and columns
    fig, axs = plt.subplots(rows, cols, figsize=size)  # rows, cols

    # Ensure axs is always a 2D array
    if rows == 1:
        axs = [axs]  # Convert to a list for consistent indexing

    for i, card in enumerate(cards):
        url = card.image
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))

        # Place image in the correct subplot
        if i < rows * cols:
            axs[i // cols][i % cols].imshow(img)  # Adjusted indexing
            axs[i // cols][i % cols].axis('off')  # Hide axes

    plt.tight_layout()  # Adjust layout
    plt.show()
