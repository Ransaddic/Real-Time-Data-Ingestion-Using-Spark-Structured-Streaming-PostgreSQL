# Import the necessary libraries
import os
import csv
import uuid
import random
from datetime import datetime
import time


# Configuration
OUTPUT_DIR = 'data/stream_data' # Directory to save the generated csv files
EVENT_TYPES =['view', 'click', 'add_to_cart','purchase'] # Types of events to generate
PRODUCTS=[
    {"id": "P1001", "name": "Smartphone"},
    {"id": "P1002", "name": "Laptop"},
    {"id": "P1003", "name": "Headphones"},
    {"id": "P1004", "name": "Camera"},
    {"id": "P1005", "name": "Smartwatch"}
]
USERS= [f'user_{i}' for i in range(1, 101)] # generate fake 100 users

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True) # Create the output directory if it doesn't exist

# Function to generate a random event
def generate_event():
    product = random.choice(PRODUCTS) # Randomly select a product
    return {
        "event_id": str(uuid.uuid4()),
        "user_id": random.choice(USERS),
        "product_id": product["id"],
        "product_name":product["name"],
        "event_type": random.choice(EVENT_TYPES),
        "event_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# Function to write events to a CSV file
def write_event_to_csv(filename, num_event):
    # Write the event to a CSV file
    file_path = os.path.join(OUTPUT_DIR, filename)
    with open(file_path,mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[
            "event_id", "user_id", "product_id","product_name","event_type", "event_time"])
        writer.writeheader()
        for _ in range(num_event):
            event = generate_event()
            writer.writerow(event)

if __name__ == "__main__":
    file_count = 0
    while True:
          file_count += 1
          file_name = f"stream_data_{file_count}.csv"
          print(f'Generating {file_name}...')
          write_event_to_csv(file_name, num_event=50) # Generate 50 events
          time.sleep(5) # Wait for 5 seconds before generating the next file
