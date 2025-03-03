"""
Contains variables for image-size, model paths, and labels required by other modules.
"""

IMAGE_SIZE = 50  # Image dimensions: 50x50 pixels
MODEL_PATH = "model.keras"

LABELS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
          'n','o', 'p', 'q','r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']

NUM_CLASSES = len(LABELS)  # Automatically detect number of classes

# Confidence threshold for predictions
THRESHOLD = 50  # Minimum percentage confidence required for valid predictions
