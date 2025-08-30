# Use official Python image
FROM python:3.10-slim

# Prevent interactive apt installs
ENV DEBIAN_FRONTEND=noninteractive

# Set working directory inside container
WORKDIR /app

# Install system dependencies for browsers & allure
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    wget \
    git \
    default-jre \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*

# Install Allure CLI
RUN curl -o allure.tgz -L https://github.com/allure-framework/allure2/releases/download/2.29.0/allure-2.29.0.tgz \
    && tar -zxvf allure.tgz -C /opt/ \
    && ln -s /opt/allure-2.29.0/bin/allure /usr/bin/allure \
    && rm allure.tgz

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install browsers for Playwright
RUN playwright install --with-deps

# Copy project files into container
COPY . .

# Expose port for Allure server
EXPOSE 5252

# Default command (runs pytest and generates allure-results)
CMD ["pytest", "-v", "--alluredir=allure-results"]
