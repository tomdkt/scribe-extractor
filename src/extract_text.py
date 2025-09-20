#
# ScribeExtractor: PDF Text Extraction Script
#
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import sys
from pathlib import Path

def extract_text_from_pdf(pdf_path: Path, output_path: Path):
    """
    Extracts text from each page of a PDF, performs OCR on images,
    and saves the text incrementally to an output file.

    Args:
        pdf_path (Path): The path to the input PDF file.
        output_path (Path): The path to the output text file.
    """
    if not pdf_path.is_file():
        print(f"Error: Input file not found at '{pdf_path}'")
        print("Please check the hardcoded path in the 'main' function.")
        sys.exit(1)

    try:
        # Open the PDF document
        doc = fitz.open(pdf_path)
        num_pages = len(doc)
        print(f"Found {num_pages} page(s) in the PDF.")

        # Open the output file in write mode to clear it initially.
        # The file will be appended to for each page.
        with open(output_path, "w", encoding="utf-8") as out_file:
            print(f"Processing pages and saving output to '{output_path}'...")

            # Iterate through each page of the PDF
            for page_num in range(num_pages):
                page = doc.load_page(page_num)

                # Convert the page to a high-resolution image
                # DPI (dots per inch) can be increased for better OCR quality
                pix = page.get_pixmap(dpi=300)
                img_data = pix.tobytes("png")
                image = Image.open(io.BytesIO(img_data))

                # Use Tesseract to extract text from the image
                # Specify English as the language
                try:
                    text = pytesseract.image_to_string(image, lang='eng')

                    # Write a header for the page and then the extracted text
                    out_file.write(f"\n--- Page {page_num + 1} ---\n\n")
                    out_file.write(text)

                    # Flush the buffer to ensure the file is written to disk immediately
                    out_file.flush()
                    print(f"  - Page {page_num + 1}/{num_pages} processed.")

                except pytesseract.TesseractError as e:
                    print(f"  - Error on page {page_num + 1}: {e}")
                    out_file.write(f"\n--- OCR Error on Page {page_num + 1} ---\n")
                    out_file.flush()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if 'doc' in locals() and doc:
            doc.close()
        print("\nProcessing complete.")


def main():
    """Main function to run the extraction with hardcoded paths."""

    # Change this to your PDF file path
    pdf_input_path = Path("/path/to/your/document.pdf")

    # Output file (will be created in project root)
    text_output_path = Path("extracted_text.txt")

    extract_text_from_pdf(pdf_input_path, text_output_path)

if __name__ == "__main__":
    main()