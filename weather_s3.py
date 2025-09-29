import os, sys
from datetime import datetime
import dotenv
from get_weather import get_weather
from s3_utils import upload_to_s3, list_recent_files, get_file

def main():
    dotenv.load_dotenv()
    api_key = os.getenv("OWM_API_KEY")
    bucket = os.getenv("S3_BUCKET")

    if not api_key or not bucket:
        print("Error: Missing API key or S3 bucket.")
        return

    if len(sys.argv) < 2:
        recent_files = list_recent_files(bucket, limit=3)
        if not recent_files:
            print("No files found in the S3 bucket.")
            return

        print("Showing last 3 weather snapshots:\n")
        for key in recent_files:
            data = get_file(bucket, key)
            print(f"{key}")
            print(f"City: {data['city']}")
            print(f"Temp: {data['temp']} °C\n")

    if len(sys.argv) > 1:
        city = sys.argv[1]
        data = get_weather(city, api_key)
        filename = f"{city}-{datetime.now().strftime('%Y%m%d-%H:%M:%S')}.json"

        upload_to_s3(bucket, filename, data)
        print(f"Uploaded {filename} to {bucket}")

if __name__ == "__main__":
    main()
