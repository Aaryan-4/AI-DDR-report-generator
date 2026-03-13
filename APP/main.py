import os
from pdf_parser import extract_pdf
from ai_engine import generate_ddr
from report_writer import create_report

# Input PDF paths
inspection_pdf = "data/input/sample_report.pdf"
thermal_pdf = "data/input/thermal_report.pdf"

# Image output folders
inspection_img = "data/images/inspection"
thermal_img = "data/images/thermal"

# Create folders if they don't exist
os.makedirs(inspection_img, exist_ok=True)
os.makedirs(thermal_img, exist_ok=True)
os.makedirs("output", exist_ok=True)

print("Extracting Inspection Report...")

inspection_text = extract_pdf(
    inspection_pdf,
    inspection_img
)

print("Extracting Thermal Report...")

thermal_text = extract_pdf(
    thermal_pdf,
    thermal_img
)

print("Generating DDR using Groq AI...")

ddr = generate_ddr(
    inspection_text,
    thermal_text
)

print("Building final report...")

create_report(
    ddr,
    inspection_img,
    thermal_img,
    "output/DDR_Report.docx"
)

print("DDR Report Generated Successfully!")
print("Output saved in: output/DDR_Report.docx")