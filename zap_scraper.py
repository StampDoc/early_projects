from request_manager import RequestManager
from zap_refactor import results


class ZapScraper:
# the manager

    zap_url = "https://www.zap.co.il/search.aspx?keyword={}"

    def __init__(self):
        self.request_manager = RequestManager() ## allows scrapper to communicate with the site

    def fetch_product(self, product: str): # returns a soup object
        print("fetching product....")
        product_url = self.zap_url.format(product)
        result = self.request_manager.get(product_url)
        print(result)

    def retry(self):
        print()

    def handle_proxy(self):
        print()