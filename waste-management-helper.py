import random

# Sample waste types and categories
waste_categories = {
    "Plastic bottle": "Recyclable",
    "Banana peel": "Organic",
    "Battery": "Hazardous",
    "Cardboard box": "Recyclable",
    "Glass jar": "Recyclable",
    "Leftover food": "Organic",
    "Paint can": "Hazardous"
}

# Function to classify waste
def classify_waste(item):
    return waste_categories.get(item, "Unknown type. Please refer to local guidelines.")

# User input
item = "Battery"  # Example waste item

# Classify waste
category = classify_waste(item)
print(f"The item '{item}' should be disposed of as: {category}")
