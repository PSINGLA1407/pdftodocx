import streamlit as st
import subprocess
import tempfile
import os
from PyPDF2 import PdfReader, PdfWriter

# Function to convert DOCX to PDF using LibreOffice
def convert_docx_to_pdf(input_path: str) -> str:
    output_path = input_path.replace(".docx", ".pdf")
    try:
        # Run LibreOffice in headless mode to convert DOCX to PDF
        subprocess.run(
            ['soffice', '--headless', '--convert-to', 'pdf', '--outdir', os.path.dirname(input_path), input_path],
            check=True
        )
        return output_path
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error during conversion: {e}")

# Function to encrypt a PDF with a password
def encrypt_pdf(input_path: str, password: str) -> str:
    output_path = input_path.replace(".pdf", "_encrypted.pdf")
    try:
        # Read the input PDF
        reader = PdfReader(input_path)
        writer = PdfWriter()

        # Copy all pages to the writer
        for page in reader.pages:
            writer.add_page(page)

        # Encrypt the writer object with the given password
        writer.encrypt(password)

        # Write the encrypted PDF to the output file
        with open(output_path, "wb") as encrypted_file:
            writer.write(encrypted_file)

        return output_path
    except Exception as e:
        raise Exception(f"Error during encryption: {e}")

# Streamlit app title
st.title("DOCX to PDF Converter and Encryptor")

# Tabs for conversion and encryption
tab1, tab2 = st.tabs(["Convert DOCX to PDF", "Encrypt PDF"])

with tab1:
    # Upload file section
    uploaded_file = st.file_uploader("Choose a DOCX file", type="docx")

    if uploaded_file is not None:
        # Save the uploaded DOCX file to a temporary directory
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_input_path = temp_file.name

        # Show the file name
        st.write(f"File '{uploaded_file.name}' uploaded successfully!")

        # Create a button for starting conversion
        if st.button("Convert to PDF"):
            try:
                # Convert DOCX to PDF
                temp_output_path = convert_docx_to_pdf(temp_input_path)

                # Display download button for the converted PDF
                with open(temp_output_path, "rb") as pdf_file:
                    st.download_button(
                        label="Download PDF",
                        data=pdf_file,
                        file_name="converted.pdf",
                        mime="application/pdf"
                    )

                # Clean up the temporary files after conversion
                os.remove(temp_input_path)
                os.remove(temp_output_path)

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

with tab2:
    # Upload file section for encryption
    uploaded_pdf = st.file_uploader("Choose a PDF file to encrypt", type="pdf")

    if uploaded_pdf is not None:
        # Save the uploaded PDF file to a temporary directory
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_pdf.read())
            temp_pdf_path = temp_file.name

        # Input password for encryption
        password = st.text_input("Enter a password for encryption", type="password")

        # Create a button for starting encryption
        if st.button("Encrypt PDF"):
            if password:
                try:
                    # Encrypt PDF
                    encrypted_pdf_path = encrypt_pdf(temp_pdf_path, password)

                    # Display download button for the encrypted PDF
                    with open(encrypted_pdf_path, "rb") as encrypted_file:
                        st.download_button(
                            label="Download Encrypted PDF",
                            data=encrypted_file,
                            file_name="encrypted.pdf",
                            mime="application/pdf"
                        )

                    # Clean up the temporary files after encryption
                    os.remove(temp_pdf_path)
                    os.remove(encrypted_pdf_path)

                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
            else:
                st.warning("Please enter a password to encrypt the PDF.")
