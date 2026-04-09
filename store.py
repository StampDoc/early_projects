from dataclasses import dataclass

class Store:
    #each store only has its class once, regardless of how many times it has appeared
    reviews: int
    total_reviews: int
    yearly_reviews: int
    #data type hasn't been decided yet, int(s) are just placeholders