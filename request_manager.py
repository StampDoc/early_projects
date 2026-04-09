from fake_useragent import UserAgent
import requests

requests_exception = requests.exceptions.RequestException
class RequestManager:

    def __init__(self, timeout=10):
        self.session = requests.session()
        self.timeout = timeout
        self.headers = {"User-Agent": UserAgent().random}

    def get(self, url: str):
        """Returns the content of the page as a Unicode string"""
        try:
            response = requests.get(url,headers=self.headers, timeout=self.timeout)
            return response.text
        except requests.exceptions.RequestException as e:
            print("🐞 an error occurred, trying to handle exception...")
            self.handle_exception(e)
            return None

    @staticmethod
    def handle_exception(exception: requests_exception):
        #IMPLEMENT ERROR HANDLING
        if exception == requests_exception:
            print("🐞 ")