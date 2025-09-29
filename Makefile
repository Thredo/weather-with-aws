build:
	docker build -t weather-s3 .

# Default: no city → list last 3 snapshots
run: build
	docker run --rm --env-file .env weather-s3 $(CITY)