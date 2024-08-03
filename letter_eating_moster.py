import os

DATA_DIR = './data'
letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
num_images_to_delete = 50

for letter in letters:
    letter_dir = os.path.join(DATA_DIR, letter)
    if os.path.exists(letter_dir):
        # Get a list of all image files in the directory
        image_files = [f for f in os.listdir(letter_dir) if f.endswith('.jpg')]
        
        # Sort the image files to ensure we delete the last 50
        image_files.sort()
        
        # Get the last 50 image files
        images_to_delete = image_files[-num_images_to_delete:]
        
        # Delete each image file
        for image_file in images_to_delete:
            file_path = os.path.join(letter_dir, image_file)
            os.remove(file_path)
            print(f"Deleted {file_path}")
    else:
        print(f"Directory {letter_dir} does not exist.")