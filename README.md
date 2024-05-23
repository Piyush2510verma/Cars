# Vehicle Scrapping

This project consists of a Python-based application that automates the process of fetching car images based on car models listed in an Excel sheet and displays these images using a web interface. It involves several components, including Python scripts for data processing, a Flask web application for user interaction, and supporting HTML and CSS files for the frontend.

#Project Structure

car.ipynb: Jupyter notebook for processing car models from an Excel file, searching for images online, and inserting these images into the Excel file.
app.py: Flask web application to search for car images either from the local repository or online.
styles.css: CSS file for styling the web application's frontend.
index.html: HTML file serving as the main page of the web application.
vehicle_images_repository/: Directory to store downloaded car images.

#Requirements

Python 3.x
Flask
requests
BeautifulSoup4
openpyxl
Pillow (for image processing)
Jupyter (for running the notebook)

#Setup and Usage

Install dependencies:
pip install flask requests beautifulsoup4 openpyxl pillow

Run the Jupyter notebook:
Open car.ipynb in Jupyter.
Execute the notebook cells to process the car models and download images.

Run the Flask web application:
python app.py

Access the web application:
Open a web browser and go to http://127.0.0.1:5000/.
