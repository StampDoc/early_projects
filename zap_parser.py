import zap_scraper
from request_manager import RequestManager
from zap_scraper import ZapScraper


class ZapParser:
# uses bs4
    def __init__(self, scraper: ZapScraper):
        self.zap_scraper = scraper

    def extract_title(self):
        print()