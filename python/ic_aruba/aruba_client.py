#!/usr/bin/python

# Python imports
import requests


class ArubaClient(object):
    """Aruba API client class."""

    def __init__(self, args):
        """Initializes an Aruba client instance."""

        # Validate arguments
        if args.api_url == "":
            raise Exception("API URL was not provided.")
        elif args.api_key == "":
            raise Exception("API-Key was not provided.")
        elif args.app_id == "":
            raise Exception("AppID was not provided.")

        # Set instance variables from arguments
        self.api_url = args.api_url
        self.headers = {
            "X-API-KEY": args.api_key,
            "X-APP-ID": args.app_id,
            "content-type": "application/json"
        }

    def do_request(self):
        """Query the Aruba sensor status API."""

        try:
            response = requests.get(self.api_url, headers=self.headers)
        except requests.exceptions.RequestException as e:
            raise Exception("There was an ambiguous exception that occurred " +
                            "while handling your request. {}".format(e))
        except requests.exceptions.ConnectionError as e:
            raise Exception("A Connection error occurred: {}".format(e))
        except requests.exceptions.HTTPError as e:
            raise Exception("An HTTP error occurred. {}".format(e))
        except requests.exceptions.URLRequired as e:
            raise Exception("A valid URL is required to make a request. " +
                            "{}".format(e))
        except requests.exceptions.TooManyRedirects as e:
            raise Exception("Too many redirects. {}".format(e))
        except requests.exceptions.ConnectTimeout as e:
            raise Exception("The request timed out while trying to connect " +
                            "to the remote server. {}".format(e))
        except requests.exceptions.ReadTimeout as e:
            raise Exception("The server did not send any data in the " +
                            "allotted amount  of time. {}".format(e))
        except requests.exceptions.Timeout as e:
            raise Exception("The request timed out. {}".format(e))

        # Check request HTTP status code
        if response.status_code != 200:
            raise Exception("HTTP status code error. {}".format(
                            response.status_code))

        # Return response JSON
        return response.json()


if __name__ == "__main__":
    pass
