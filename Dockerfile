FROM python:3.9

# Set the working directory
WORKDIR /src

# Install any needed packages specified in requirements.txt
COPY requirements.txt /src

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Copy the current directory contents into the container at /app
COPY . /src

# Run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port" , "8000"]