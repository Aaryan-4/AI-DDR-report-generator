import fitz
import os

def extract_pdf(pdf_path, image_folder):

    doc = fitz.open(pdf_path)

    os.makedirs(image_folder, exist_ok=True)

    text = ""

    for page_index in range(len(doc)):

        page = doc[page_index]
        text += page.get_text()

        images = page.get_images(full=True)

        for img_index, img in enumerate(images):

            xref = img[0]
            base_image = doc.extract_image(xref)

            image_bytes = base_image["image"]
            ext = base_image["ext"]

            img_name = f"{image_folder}/page{page_index+1}_{img_index}.{ext}"

            with open(img_name, "wb") as f:
                f.write(image_bytes)

    return text