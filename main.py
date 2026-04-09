from zap_scraper import ZapScraper

if __name__ == '__main__':
    #the main should only interact with zap parser, or with even a third script such as zap manager that handles both zap parser and zap parser
    zap_scraper = ZapScraper()
    product_name = input("enter a product name > ")
    zap_scraper.fetch_product(product_name)