from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import re

def region_based_extraction(input_pdf):

    pages = convert_from_path(input_pdf, dpi=300)

    for i, page in enumerate(pages):

        # Convert to RGB (important)
        page = page.convert("RGB")

        # Example coordinates (YOU must adjust)
        sn_region = page.crop((100, 150, 800, 350))
        temp_region = page.crop((1200, 500, 1800, 900))
        img_region = page.crop((100, 50, 800, 150))

        sn_text = pytesseract.image_to_string(sn_region, config="--psm 6")
        temp_text = pytesseract.image_to_string(temp_region, config="--psm 6")
        img_text = pytesseract.image_to_string(img_region, config="--psm 6")

        sn_match = re.search(r"\d+", sn_text)
        temps = re.findall(r"([\d.]+)", temp_text)
        img_match = re.search(r"RB\d+X\.JP[G|C]", img_text)

        print("Page:", i+1)
        print("SN:", sn_match.group(0) if sn_match else "Unknown")
        print("Temps:", temps)
        print("Image:", img_match.group(0) if img_match else "Unknown")
        print("-"*40)

path = r"D:\Desktop\DDR report generator\data\input\Thermal Images.pdf"

region_based_extraction(path)
