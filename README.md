# weather-with-aws

A simple Python CLI app that gets weather data from [OpenWeatherMap](https://openweathermap.org/api)  
and interacts with AWS S3 for storing or retrieving snapshots.  
The project can run in both venv and Docker.

## Features
- Gets the current weather for a given city (temperature and name of the city).
- List the last 3 saved snapshots from an S3 bucket (default when no city is passed).
- Uses `.env` file for secure API keys and AWS credentials.
- Lightweight Docker image (`python:3.12-slim`) with a non-root user for security.
- Easy to run with `make`.
- can also be run locally with uv venv

## Requirements
- Docker installed
- An OpenWeatherMap API key
- AWS account (Free Tier works just fine) with an S3 bucket
- `.env` file (see example below)

## Setup

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/weather-cli.git
   cd weather-cli

2. Create a .env file based on the example:
    ```bash
    OWM_API_KEY=your_openweather_api_key
    AWS_ACCESS_KEY_ID=your_aws_access_key
    AWS_SECRET_ACCESS_KEY=your_aws_secret
    AWS_REGION=us-east-1
    S3_BUCKET=your-bucket-name

3. Build the image:
    make build

## Usage (Docker)
1. List last 3 snapshots saved on S3 (default)
    make run

Example output:
    Showing last 3 weather snapshots:

    BudapeSt-20250922-01:35:21.json
    City: Budapest
    Temp: 19.51 °C

    Kyoto-20250922-01:31:59.json
    City: Kyoto
    Temp: 26.15 °C

    Krakow-20250920-23:55:27.json
    City: Krakow
    Temp: 17.12 °C

2. Saves weather for the city on that day on S3
    make run CITY=Name_of_City

Example output:
    Uploaded Tokyo-20250929-19:19:33.json to weather-s3-testing

## Local Usage (with uv)
1. Create a virtual environment (once):
    uv venv

2. Activate the environment:
    source .venv/bin/activate

3. install dependecies:
    python -m pip install -r requirements.txt

4. Run the app:
    - With city:
        python weather_s3.py Tokyo
    - List from S3:
        python weather_s3.py

## Tech Stack
- Python 3.12
- Requests + python-dotenv
- AWS S3 (Free Tier)
- Docker

## Possible Improvements
- Saving and showing the weather for the day
- Add CI/CD workflow with GitHub Actions.
- Deploy on AWS Lambda or EC2 for automation.