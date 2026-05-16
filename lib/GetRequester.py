# Start with importing utilities
import requests
import json

"""
Create a class to hold all functions for OOP functionality. It is responsible for sending GET requests and parsing JSON responses from the API.
"""
class GetRequester:
    
    """
    Constructor triggers when the class is called it will save the URL so all methods can reach it at self.url.
    URL is a paramater needed, make sure to put the full URL in the URL variable.
    """
    def __init__(self, url):
        self.url = url
    
    """
    Function for receiving response from API after the GET request is sent to self.url. Parse the response into JSON below since it is returned here as a string. Return what is gathered from the API.
    """
    def get_response_body(self):
        response = requests.get(self.url)
        return response.text

    """
    Function for loading and parsing JSON returned output from the prior function.
    """
    def load_json(self):
        raw = self.get_response_body()
        return json.loads(raw)