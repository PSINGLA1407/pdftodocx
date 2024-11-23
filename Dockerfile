# Step 1: Use Ubuntu 22.04 as the base image
FROM ubuntu:22.04

# Avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Step 2: Install system dependencies
# Include Python, pip, LibreOffice, and other necessary utilities
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    software-properties-common \
    curl \
    wget \
    libreoffice \
    wkhtmltopdf \
    libgs-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Step 3: Set the working directory inside the container
WORKDIR /app

# Step 4: Copy the current directory contents into the container
COPY . /app

# Step 5: Install Python dependencies from requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Step 6: Expose the port that Streamlit runs on (default is 8501)
EXPOSE 8501

# Step 7: Define the command to run the Streamlit app when the container starts
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
