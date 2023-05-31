# Image-to-text
A simple python script designed to scan images for text then save the output to a file on your local desktop.

Image-to-Text Script
This script is designed to extract text from images using the Google Cloud Vision API. It takes a directory containing images as input and saves the extracted text from each image to separate text files.

Prerequisites
Before running the script, you need to set up the following:

Python 3.11 or a compatible version.

Install the required dependencies by running the following command:
pip install google-cloud-vision

Obtain a service account JSON key file from the Google Cloud Console for the Cloud Vision API. Place it in the same directory as the script.

Usage
Place the images you want to process in a directory.

Set the image_dir variable in the script to the path of the directory containing the images.

Run the script using the following command:

Copy code
python script_name.py
Make sure to replace script_name.py with the actual name of the script file.

Output
The script will process each image in the specified directory and save the extracted text to separate text files. The output files will be named after the original image file with "_text.txt" appended to them.

Note
If any errors occur during the execution of the script, relevant error messages will be displayed in the console.
