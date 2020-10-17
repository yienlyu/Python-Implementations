# data format: <user_name> <user_id> <click_timestamp> <product_id> <sale>

# store the costumers' information with a list of tuples
def store_allInfo(a, all_info): 
    a = tuple(str(x) for x in a.split(" "))
    all_info.append(a)

# store the products' information with a dictionary {product_id : {(user_id, sale), ...}}
def store_productInfo(a, product_info): 
    a = tuple(str(x) for x in a.split(" "))
    if a[3] in product_info:
        product_info.get(a[3]).add((a[0], a[4]))
    else: 
        product_info[a[3]] = {(a[0], a[4])}

# store by coustumers with a dictionary {user_id : {(click_timestamp, product_id)}}
# def store_costumerInfo():

# count and print the information of the product's sales
def count_sales(sales_list, product_id, click):
    purchase = 0
    users = []
    num = len(sales_list)
    for i in range(num):
        purchase = purchase + int(sales_list[i][1])
        users.append(sales_list[i][0])
    print(f'product {product_id}: {purchase} purchase / {click} click')
    for i in range(num):
        print(users[i])

# print sales and user who purchase among all clicks of the product (using filter)
def product_sales(product_id, product_info):
    click = len(product_info.get(product_id))
    sales_list = list(filter(lambda sale : sale[1] > "0", product_info.get(product_id)))
    count_sales(sales_list, product_id, click)

# return the products clicked by both two users (using set intersection)
# def users_intersect(user_id1, user_id2, all_info):

# return 5 products the user most recently clicked
# def users_recentClick(user_id, costumerInfo):

# (after adding classification of products)
# return 5 recommended products to the user
# def users_recommend(user_id, product_info):

# read and process the data 
def readData(all_info, product_info):
    for i in range(15):
        a = input()
        store_allInfo(a, all_info)
        store_productInfo(a, product_info)
    # print(f'all_info: {all_info}')
    # print(f'product_info: {product_info}')

if __name__ == '__main__':
    all_info = []
    product_info = {}
    
    readData(all_info, product_info)
    product_sales("14667", product_info)
    product_sales("3k495", product_info)
