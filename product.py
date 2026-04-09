from dataclasses import dataclass

import store


@dataclass
class Product:
    name: str
    max_price: float
    min_price: float
    store: list#[dict{"store": store : "price": float}]
