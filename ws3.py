import fitz
import os

file = "league-of-legends-beginners-guide_compress.pdf"

doc = fitz.open(file)

print("จำนวนหน้า:", len(doc))
print("metadata:", doc.metadata)
print("ขนาดไฟล์:", os.path.getsize(file), "bytes")

import fitz

# doc = fitz.open("league-of-legends-beginners-guide_compress.pdf")

# for page in doc:
#     text = page.get_text()
#     print(text)

import fitz

doc = fitz.open("league-of-legends-beginners-guide_compress.pdf")

for page_index in range(len(doc)):
    page = doc[page_index]
    images = page.get_images()

    for img_index, img in enumerate(images):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]

        with open(f"img_{page_index}_{img_index}.png", "wb") as f:
            f.write(image_bytes)