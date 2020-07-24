FROM python:3.7.3-stretch

## Step 1:
# Create a working directory
RUN mkdir /app

## Step 2:
# Copy source code to working directory
COPY src/app.py app/
COPY src/requirements.txt app/
WORKDIR /app

## Step 3:
# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir

## Step 4:
# Expose port 80
EXPOSE 80

## Step 5:
# Run app.py at container launch
CMD ["python", "app.py"]
