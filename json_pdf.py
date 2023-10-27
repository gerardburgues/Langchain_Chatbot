import json
from fpdf import FPDF
import os


class PDF(FPDF):
    def __init__(self, title=None):
        super().__init__()
        self.title = title

    def header(self):
        self.set_font("Arial", "B", 12)
        title = self.title if self.title else "Transcript"
        self.cell(0, 10, title, 0, 1, "C")

    def chapter_title(self, num, label):
        self.set_font("Arial", "", 12)
        self.cell(0, 10, "Speaker: %s" % label, 0, 1, "L")

    def chapter_body(self, body):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, "Text: %s" % body)
        self.ln()


def create_pdf(data, output_name, title):
    pdf = PDF(title=title)
    pdf.add_page()

    for i, entry in enumerate(data, 1):
        pdf.chapter_title(i, entry["speaker"])
        pdf.chapter_body(entry["text"])

    pdf.output(output_name)


directory = "./json_files/"

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        with open(os.path.join(directory, filename), "r") as f:
            data = json.load(f)

        # Name the output PDF the same as the JSON file but with a .pdf extension
        output_name = os.path.join(directory, os.path.splitext(filename)[0] + ".pdf")
        title = os.path.splitext(filename)[0]  # Extract filename without extension

        create_pdf(data, output_name, title)
