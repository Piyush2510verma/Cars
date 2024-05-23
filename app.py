import os
import requests
from flask import Flask, request, render_template, url_for
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image

app = Flask(__name__)

# Path to the directory where images are stored
REPOSITORY_PATH = os.path.join(app.static_folder, 'vehicle_images_repository')

# Create a dictionary to map car models to their image file paths
car_image_map = {}

# Populate the dictionary with image file paths
if os.path.exists(REPOSITORY_PATH):
    for filename in os.listdir(REPOSITORY_PATH):
        if filename.endswith(".jpg"):
            car_model = filename.replace("_", " ").replace(".jpg", "")
            car_image_map[car_model.upper()] = filename

def search_car_image_online(brand, model):
    search_query = f"{brand} {model} car"
    url = f"https://www.google.com/search?q={search_query}&tbm=isch"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_elements = soup.find_all('img')
    
    # Extract the first image URL
    if image_elements:
        image_url = image_elements[1].get('src')
        if image_url.startswith('http'):
            return image_url
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search_car_image():
    car_model = request.args.get('model')
    if not car_model:
        return render_template('index.html', error="No car model provided")
    
    # Preprocess the user input to match the format of car_model keys
    car_model_processed = car_model.replace(" ", "_").upper()
    
    if car_model_processed in car_image_map:
        image_filename = car_image_map[car_model_processed]
        # Generate URL for the image
        image_url = url_for('static', filename=f'vehicle_images_repository/{image_filename}')
        return render_template('index.html', image_url=image_url)
    else:
        # If the car model is not found locally, search it online
        brand, model = car_model.split()[0], ' '.join(car_model.split()[1:])
        image_url = search_car_image_online(brand, model)
        if image_url:
            # Assume you have a function to save the image URL to the database
            save_image_to_database(car_model, image_url)
            return render_template('index.html', image_url=image_url)
        else:
            return render_template('index.html', error="Car model not found. Searching online...")

def save_image_to_database(car_model, image_url):
    # Assume you have a function to save the image URL to the database
    pass

if __name__ == '__main__':
    app.run(debug=True)
