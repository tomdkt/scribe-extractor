
# ScribeExtractor

A Python tool for extracting text from image-based PDFs using OCR (Optical Character Recognition). Perfect for digitizing scanned documents, books, and PDFs that contain images instead of selectable text.

## Features

- **OCR Text Extraction**: Uses Tesseract OCR to extract text from PDF pages
- **High-Quality Processing**: Converts PDF pages to 300 DPI images for better OCR accuracy
- **Incremental Output**: Saves extracted text page by page as processing continues
- **Error Handling**: Gracefully handles OCR errors and continues processing
- **Progress Tracking**: Shows real-time progress as pages are processed

## Quick Start

### 1. Install System Dependencies

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install tesseract-ocr

# macOS
brew install tesseract

# Windows
# Download and install from: https://github.com/UB-Mannheim/tesseract/wiki
```

### 2. Install Python Package

```bash
# Using uv (recommended)
uv pip install -e .

# Or using pip
pip install -e .
```

### 3. Extract Text from PDF

```bash
# Run the extraction tool
extract

# Or run directly with Python
python src/extract_text.py
```

## Configuration

Before running, update the file paths in `src/extract_text.py`:

```python
# Change this to your PDF file path
pdf_input_path = Path("/path/to/your/document.pdf")

# Output file (will be created in project root)
text_output_path = Path("extracted_text.txt")
```

## Usage Examples

### Basic Usage
```bash
# Extract text from a PDF
extract
```

### Custom Processing
```python
from pathlib import Path
from extract_text import extract_text_from_pdf

# Extract text from any PDF
pdf_path = Path("my_document.pdf")
output_path = Path("output.txt")
extract_text_from_pdf(pdf_path, output_path)
```

## Output Format

The extracted text is saved with page separators:

```
--- Page 1 ---

[Extracted text from page 1]

--- Page 2 ---

[Extracted text from page 2]
```

## Requirements

- Python 3.8+
- Tesseract OCR engine
- PyMuPDF (for PDF processing)
- pytesseract (OCR wrapper)
- Pillow (image processing)

## Troubleshooting

### Common Issues

**"TesseractNotFoundError"**
- Make sure Tesseract is installed and in your PATH
- On Windows, you may need to set the tesseract path manually

**"Input file not found"**
- Check that the PDF path in `main()` function is correct
- Use absolute paths to avoid confusion

**Poor OCR Quality**
- Increase DPI in the code (currently 300)
- Ensure your PDF has good image quality
- Consider preprocessing images for better results

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Feel free to use and modify as needed.
