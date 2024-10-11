import os

import pytesseract
from PIL import Image

output_folder = "tmp/"

files = os.listdir(output_folder)
files.sort()
first_run = True
for x, file in enumerate(files):
    image = Image.open(os.path.join(output_folder, file))
    text = pytesseract.image_to_string(image, lang="por")
    
    if ("TÍTULO" in text):
        raw_file = os.path.splitext(os.path.basename(file))[0]
        
    with open(os.path.join("tmp2/", f"{raw_file}.txt"), "+a", encoding="utf-8") as fp:
        fp.write(text)