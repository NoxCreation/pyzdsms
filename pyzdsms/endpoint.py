import requests

URL_ENDPOINT = "https://zdsms.cu/"
VERSION_ENDPOINT = "api/v1"

ENDPOINTS = {
    "me": "/me",
    "sendsms": "/message/send",
    "getallsms": "/message/",
    "getallsms_paginate": "/message/paginated?page=PAGE",
    "detailsms": "/message/ID/status",
    "sendcampaign": "/campaign/send",
    "allcampaign": "/campaign/"
}

def get_request(endpoint, headers, payload={}, method="GET"):
    url = f"{URL_ENDPOINT}{VERSION_ENDPOINT}{endpoint}"
    response = requests.request(method, url, headers=headers, data=payload)
    return response
