"""
After recently joining Instacart's beta testing developer group, you decide to experiment with their new API. You know that the API returns item-specific display-ready strings like 10.0% higher than in-store or 5.0% lower than in-store that inform users when the price of an item is different from the one in-store. But you want to extend this functionality by giving people a better sense of how much more they will be paying for their entire shopping cart.

Your app lets a user decide the total amount x they are willing to pay via Instacart over in-store prices. This you call their price sensitivity.

Your job is to determine whether a given customer will be willing to pay for the given items in their cart based on their stated price sensitivity x.

Example

For
prices = [110, 95, 70],

notes = ["10.0% higher than in-store", 
         "5.0% lower than in-store", 
         "Same as in-store"]
and x = 5, the output should be
solution(prices, notes, x) = true.

In-store prices of the first and the second items are 100, and the price of the third item is 70, which means the customer is overpaying 10 - 5 + 0 = 5, which they are willing to do based on their price sensitivity.

For
prices = [48, 165],

notes = ["20.00% lower than in-store", 
         "10.00% higher than in-store"]
and x = 2, the output should be
solution(prices, notes, x) = false.

The in-store price of the first item is 60, and the second item is 150. The overpayment equals 15 - 12 = 3, which is too much for the customer to be willing to pay.
"""


def solution(prices, notes, x):

    def get_note_percent(note):
        percent_word = note.split(" ")[0].split("%")[0]
        print(percent_word)
        return float(percent_word)

    origin_prices = []
    result = 0

    for idx, price in enumerate(prices):
        tmp_price = 0
        if "higher" in notes[idx]:
            percent = get_note_percent(notes[idx])
            tmp_price = (price / (100 + percent)) * 100
            origin_prices.append(price - tmp_price)
        elif "lower" in notes[idx]:
            percent = get_note_percent(notes[idx])
            tmp_price = (price / (100 - percent)) * 100
            origin_prices.append(price - tmp_price)
        elif "Same" in notes[idx]:
            origin_prices.append(0)

    print(origin_prices)
    for price in origin_prices:
        result += price

    return False if result > x else True
