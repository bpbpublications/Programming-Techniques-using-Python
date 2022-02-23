my_old_price = {'eggs': 0.8, 'chocos': 3, 'rice': 1}

dollar_to_indiancurrency = 75
my_new_price = {key: value*dollar_to_indiancurrency for (key, value) in my_old_price.items()}
print(my_new_price)
