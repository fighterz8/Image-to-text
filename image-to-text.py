import io
import os
from google.cloud import vision

def setup_client():
    credential_path = os.path.join(os.path.dirname(__file__), "image-to-text-388416-01d1a4ed8a36.json")
    return vision.ImageAnnotatorClient.from_service_account_json(credential_path)

def load_images(image_paths):
    images = []
    for image_path in image_paths:
        try:
            with io.open(image_path, 'rb') as image_file:
                content = image_file.read()
            image = vision.Image(content=content)
            images.append(image)
        except Exception as e:
            print(f"Error reading file {image_path}: {e}")
    return images

def extract_text(client, image):
    try:
        response = client.text_detection(image=image)
        texts = response.text_annotations
        return texts[0].description if texts else 'No text detected.'
    except Exception as e:
        print(f"Error in text detection: {e}")
        return None

def save_text(image_path, detected_text):
    try:
        image_filename = os.path.basename(image_path)
        output_file = f"{image_filename}_text.txt"
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(detected_text)
        print('Text extracted and saved to', output_file)
    except Exception as e:
        print(f"Error writing to file: {e}")


def main():
    client = setup_client()
    image_dir = r"C:\Python311\Custom scripts\bloomfeedback"
    
    # Get a list of all file names in that directory
    image_files = os.listdir(image_dir)
    
    # Add the directory path back onto the file names
    image_paths = [os.path.join(image_dir, image_file) for image_file in image_files]
    
    images = load_images(image_paths)
    for i, image in enumerate(images):
        detected_text = extract_text(client, image)
        if detected_text:
            save_text(image_paths[i], detected_text)

if __name__ == "__main__":
    main()
