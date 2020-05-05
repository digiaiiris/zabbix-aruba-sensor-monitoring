#!/usr/bin/python

# Python imports
import json
from argparse import ArgumentParser
from aruba_client import ArubaClient


class ArubaSensor(object):
    """Retrieve sensor status from Aruba's status API."""

    def __init__(self, aruba_client):
        self._client = aruba_client

    def sensor_status(self, sensor_uid):

        # Declare variables
        sensor_data = []

        # Query the API for sensor data
        response = self._client.do_request()

        # Retrieve sensor data from response
        for nodes in response.get("payload").get("nodes"):
            if nodes.get("state_summary").get("sensors"):
                for sensor in nodes.get("state_summary").get("sensors"):
                    sensor_data.append(sensor)

        # Check sensor data
        if not sensor_data:
            return None

        # Loop sensor data and try to retrieve specified sensor state
        for item in sensor_data:
            if item.get("uid") == sensor_uid:
                return item.get("state")


def main(args=None):
    parser = ArgumentParser(
        description="Retrieve sensor status from Aruba's status API."
    )

    # Parse command-line arguments
    parser.add_argument("api_url", help="Aruba API URL.")
    parser.add_argument("api_key", help="Aruba API-Key.")
    parser.add_argument("app_id", help="Aruba AppID.")
    parser.add_argument("sensor_uid", help="Aruba sensor UID.")
    args = parser.parse_args(args)

    # Instantiate Aruba client
    aruba_client = ArubaClient(args)

    # Instantiate Aruba sensor instance
    sensor = ArubaSensor(aruba_client)

    # Retrieve and output sensor status
    status = sensor.sensor_status(args.sensor_uid)
    print(status)


if __name__ == "__main__":
    main()
