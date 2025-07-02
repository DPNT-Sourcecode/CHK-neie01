from dataclasses import dataclass
from collections import Counter

@dataclass
class Item:
    name: str
    price: int
    offers: str = None

def _quantity_for_price_offer(offer_quantity, offer_price, item_quantity, item_price) -> int:
    total_price = (item_quantity // offer_quantity) * offer_price
    total_price += (item_quantity % offer_quantity) * item_price
    return total_price


def _item_off_offer(basket: dict, prices: dict, item: str, item_quantity_for_offer: int, offer_item: str, offer_quantity: int):
        total_free_item = basket[item] // item_quantity_for_offer
        total_cost = basket[item] * prices[item]
        basket[offer_item] = max(0, basket[offer_item] - total_free_item)

        return total_cost


class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str) -> int:

        prices = {
            "A": 50,    
            "B": 30,    
            "C": 20,
            "D": 15,
            "E": 40,
            "F": 10,
        }

        for char in skus:
            if char not in prices:
                return -1

        # Count each items in the basket
        basket_counter = Counter(skus)

        total_cost = 0

        # Process E first
        if "E" in basket_counter:
            total_cost += _item_off_offer(
                basket=basket_counter,
                prices=prices, item="E",
                item_quantity_for_offer=2,
                offer_item="B",
                offer_quantity=1,
            )
        
        if "A" in basket_counter:
            total_5a_deals = basket_counter["A"] // 5
            total_cost += total_5a_deals * 200
            remaining_5a = basket_counter["A"] % 5

            total_3a_deals = remaining_5a // 3
            total_cost += total_3a_deals * 130
            remaining_3a = remaining_5a % 3

            total_cost += remaining_3a * prices["A"]
        
        if "B" in basket_counter:
            num_2b_deals = basket_counter["B"] // 2
            total_cost += num_2b_deals * 45
            total_cost += basket_counter["B"] % 2 * prices["B"]
        
        if "C" in basket_counter:
            total_cost += basket_counter["C"] * prices["C"]

        if "D" in basket_counter:
            total_cost += basket_counter["D"] * prices["D"]

        if "F" in basket_counter:
            total_3fs = basket_counter["F"] // 3
            total_cost += total_3fs * 2 * prices["F"]
            total_cost += (basket_counter["F"] % 3) * prices["F"]
                
        
        return total_cost

