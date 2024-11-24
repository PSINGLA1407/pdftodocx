# 📄 Docx to PDF Converter with Password Protection

Hosted and live at http://34.45.129.202:8501/

![image](https://github.com/user-attachments/assets/aa5e6a95-ff33-45bd-9289-739dcfd8cf3a)

This repository provides a **Docx to PDF Converter** built using **Streamlit** and **LibreOffice**, containerized with **Docker**. Additionally, the app includes a feature to add password protection to the generated PDF files.

## 🚀 Features

- Upload `.docx` files and convert them to `.pdf`.
- Add password protection to the converted PDF files.
- Intuitive web interface built with **Streamlit**.
- Cross-platform support using Docker for seamless deployment.

---

![image](https://github.com/user-attachments/assets/f8329022-6432-40dc-8f3f-7f93a7b0314a)


## 🛠️ Tech Stack

- **Streamlit**: Interactive web interface.
- **LibreOffice**: Conversion from Docx to PDF.
- **PyPDF2**: Adding password protection to PDFs.
- **Docker**: Containerized deployment for platform independence.

---

## 🔧 Installation and Usage

### Prerequisites
- **Docker** installed on your system.

### Steps

1. **Clone this repository**:
    ```bash
    git clone https://github.com/psingla1407/docxtopdf.git
    cd docxtopdf
    ```

2. **Build the Docker image**:
    ```bash
    docker build -t docx-to-pdf-converter .
    ```

3. **Run the Docker container**:
    ```bash
    docker run -p 8501:8501 docx-to-pdf-converter
    ```

4. **Access the application**:
    Open your browser and navigate to `http://localhost:8501`.

---

## 🖥️ Application Interface

### Tabs:
1. **Docx to PDF Converter**:
   - Upload a `.docx` file.
   - Convert it to a `.pdf` file.

2. **Password Protect PDF**:
   - Upload a `.pdf` file.
   - Set a password for the file.
   - Download the password-protected PDF.

---



