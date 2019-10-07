#!/usr/bin/python

# Python imports
import json
from argparse import ArgumentParser
from aruba_client import ArubaClient


class ArubaDiscoverSensors(object):
    """Discover sensors from Aruba's status API."""

    def __init__(self, aruba_client):
        self._client = aruba_client

    def list_sensors(self):

        # Query the API for sensor data
        response = self._client.do_request()

        # Retrieve sensor data from response
        sensor_data = response.get("payload").get("nodes")[0].get(
            "state_summary").get("sensors")

        # List sensors from response
        sensor_list = []
        for item in sensor_data:
            sensor_list.append(item)

        return sensor_list


def main(args=None):
    parser = ArgumentParser(
        description="Discover sensors from Aruba's status API."
    )

    # Parse command-line arguments
    parser.add_argument("api_url", help="Aruba API URL.")
    parser.add_argument("api_key", help="Aruba API-Key.")
    parser.add_argument("app_id", help="Aruba AppID.")
    args = parser.parse_args(args)

    # Instantiate Aruba client
    aruba_client = ArubaClient(args)

    # Instantiate discovery client
    discovery_client = ArubaDiscoverSensors(aruba_client)

    # Retrieve sensors using discovery client
    sensor_list = discovery_client.list_sensors()

    # Loop sensor data and retrieve sensor names and UIDs
    sensors = []
    for item in sensor_list:
        sensors.append({
            "{#SENSOR_NAME}": item.get("name"),
            "{#SENSOR_UID}": item.get("uid")
        })

    # Output sensor data
    print(json.dumps({"data": sensors}))


if __name__ == "__main__":
    main()
