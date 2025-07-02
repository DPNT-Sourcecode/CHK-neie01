from dataclasses import dataclass
from collections import Counter

@dataclass
class Item:
    name: str
    price: int
    offer: str = None

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str) -> int:

        items = {
            "A": Item(name="A", price=50, offer="3:130"),    
            "B": Item(name="B", price=30, offer="2:45"),    
            "C": Item(name="C", price=20),
            "D": Item(name="D", price=15),
        }

        basket_counter = Counter(list(skus))

        basket_total = 0
        for item_name, quantity in basket_counter.items():
            if item_name not in items:
                return -1
            
            item: Item = items[item_name]
            if item.offer is None:
                basket_total += item.price * quantity
            
            else:
                offer = tuple(map(int,item.offer.split(":")))
                basket_total += (quantity // offer[0]) * offer[1] + (quantity % offer[0]) * item.price
        
        return basket_total