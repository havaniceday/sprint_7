import json
import requests


class HttpClient:
    def get(self, url, params=None, headers={}):
        response = requests.get(url=url, params=params, headers=headers)
        return self.get_response(response)

    def post(self, url, body=None, headers={}):
        headers.update({"Content-Type": "application/json"})
        response = requests.post(url=url, data=json.dumps(body), headers=headers)
        return self.get_response(response)

    def delete(self, url, params=None, headers={}):
        response = requests.delete(url=url, params=params, headers=headers)
        return self.get_response(response)

    def put(self, url, params=None, headers={}):
        response = requests.put(url=url, params=params, headers=headers)
        return self.get_response(response)

    def get_response(self, response):
        if 'application/json' in response.headers['Content-Type']:
            return response.json(), response.status_code
        else:
            return response.text, response.status_code
