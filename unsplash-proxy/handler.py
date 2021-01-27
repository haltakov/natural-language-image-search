import boto3
import logging
from urllib.request import urlopen


log = logging.getLogger()
log.setLevel(logging.DEBUG)


def get_photo(event, context):
    """ Function that proxies the call to the Unsplash API to retrieve the photo meta data """

    # Get the photo ID from the parameters
    photo_id = event["pathParameters"]["id"]

    # Get the Unsplash Access Key from the Parameter Store
    client = boto3.client("ssm")
    access_key = client.get_parameter(Name="UNSPLAH_API_ACCESS_KEY")["Parameter"][
        "Value"
    ]

    # Call the Unsplash API to get the photo metadata
    photo_data_url = (
        f"https://api.unsplash.com/photos/{photo_id}?client_id={access_key}"
    )
    log.debug(f"Fetching URL: {photo_data_url}")
    photo_data = urlopen(photo_data_url).read().decode("utf-8")

    # Create the repsonse and return
    headers = {
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET",
    }

    return {
        "statusCode": 200,
        "headers": headers,
        "body": photo_data,
    }
