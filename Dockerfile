# Step 1: Use an official Python runtime as a base image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container
COPY . /app

# Step 4: Install system dependencies that your app needs
# LibreOffice for DOCX to PDF conversion and other necessary utilities
RUN apt-get update && apt-get install -y \
    libreoffice \
    wkhtmltopdf \
    libgs-dev \
    && rm -rf /var/lib/apt/lists/*

# Step 5: Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Expose the port that Streamlit runs on (default is 8501)
EXPOSE 8501

# Step 7: Define the command to run the Streamlit app when the container starts
CMD ["streamlit", "run", "app.py"]
