input data format: <user_name> <user_id> <click_timestamp> <product_id> <sale>

##########

"server.py" would read and store the data inputed. The data is stored in the dictionary format, with string <user_id> as key, 
and a list of tuple (click\_timestamp, product\_id) as value.

There are a few operations:

count\_sales(): count and print the information of the product's sales
product\_sales(): print sales and user who purchase among all clicks of the product (using filter)

(below are some unfinished functions)
users\_intersect(): return the products clicked by both two users (using set intersection)
users\_recentClick(): return 5 products the user most recently clicked
users\_recommend(): return 5 recommended products to the user (would add products' classsification to the data first)
