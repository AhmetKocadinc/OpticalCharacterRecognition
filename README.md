# OCR Image to Text Extraction with Flask

This project allows users to upload images and extract text from them using OCR (Optical Character Recognition) technology. The extracted text is displayed on the web interface, and users can also download the result as a `.docx` file. The application is built using **Flask**, **Tesseract OCR**, and **Python-docx** for document generation.

## Features

- Upload an image containing text
- Extract text from the uploaded image using OCR
- View the extracted text on the web interface
- Download the extracted text as a `.docx` file
- Simple and user-friendly interface

## How It Works

1. **Upload** an image containing text (e.g., a photo of a document, invoice, etc.).
2. The **OCR technology** processes the image and extracts the text.
3. The extracted text is displayed on the web interface in a clean format.
4. Option to **download the extracted text** as a `.docx` file for easy sharing and editing.

## Installation

To run this project locally, follow the steps below.

### Prerequisites

- Python 3.x
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed on your machine
- Required Python packages: Flask, pytesseract, Pillow, python-docx

### Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repo-name
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Make sure you have **Tesseract OCR** installed. You can download it from [here](https://github.com/tesseract-ocr/tesseract).

5. Ensure that the Tesseract executable path is correctly set in the `app.py` file:

    ```python
    pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    ```

### Running the Application

1. Start the Flask development server:

    ```bash
    python app.py
    ```

2. Open your browser and navigate to `http://127.0.0.1:5000` to use the application.

## Usage

1. Upload an image (e.g., a document or photo containing text).
2. The application will extract the text and display it on the web page.
3. Download the extracted text as a `.docx` file if needed.

## Example

![Screenshot of the app](static/example-screenshot.png)

1. Uploading an invoice.
2. Extracted text is displayed on the page.
3. Download option to save the result as a Word document.

## Project Structure


## Dependencies

- Flask
- pytesseract
- Pillow
- python-docx

To install these, simply run:

```bash
pip install -r requirements.txt



### Açıklamalar:
- **Features**: Uygulamanın sunduğu temel özellikler tanıtılıyor.
- **Installation**: Uygulamayı yerel olarak çalıştırmak için gerekli adımlar ve bağımlılıkların kurulumu.
- **Usage**: Kullanım adımları ve projenin ne işe yaradığı anlatılıyor.
- **Project Structure**: Projenin dosya yapısının kısa bir açıklaması yapılıyor.
- **Dependencies**: Projede kullanılan Python kütüphaneleri listeleniyor.

Bu README dosyasını doğrudan GitHub projen için kullanabilirsin. Eğer başka bir düzenleme ya da ekleme ihtiyacın olursa bana bildirebilirsin!


