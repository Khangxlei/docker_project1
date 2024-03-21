FROM python:3.9-slim
WORKDIR /app

# Copy just the requirements file to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run the tests
CMD ["pytest"]
