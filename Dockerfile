FROM python:3.12-slim

#Choosing a working directory
WORKDIR /usr/src/app

#Creates non root user
RUN useradd -u 1001 nonroot

#First copy only the requirements to make sure it only invalidates if dependecies change (quicker builds)
COPY requirements.txt .

#install requirements (no chache for a smaller image)
RUN pip install  --no-cache-dir -r requirements.txt

#Switch to the non root user
USER nonroot

#Copy all the code (only for the user)
COPY --chown=nonroot:nonroot . .

#Using entrypoint because the city name is used 
ENTRYPOINT ["python", "weather_s3.py"]