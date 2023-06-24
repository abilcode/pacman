import random
import numpy as np

def transaction_obj(id):
    dict = {
        'user':{'id':id},
        'item':{}
            }
    return dict

def transaction_id(length=10):
    # define the specific string 
    sample_string = 'pqrstuvwxy123456'  
    # define the condition for random string  
    result = ''.join((random.choice(sample_string)) for x in range(length))  
    print(" Randomly generated string is: ", result) 
    return result

def add_item(data,item_name=np.nan, item_counts=np.nan, item_price=np.nan):
    new_item = [
        item_counts,
        item_price,
        item_counts*item_price
    ]
    data['item'][item_name] = new_item 
    return data

def delete_item(data,item_name):
    del data['item'][item_name]
    return data

def reset_transaction(data):
    data = {
        'user':{'id':id},
        'item':{}
            }
    
    print("Transactions have been restarted!")
    
    return data

def update_item_name(data,item_name,updated_name):
    data['item'][updated_name] = data['item'].pop(item_name)
    return data

def update_item_qty(data,item_name,updated_counts):
    data['item'][item_name][0] = updated_counts
    data['item'][item_name][2] = data['item'][item_name][0]*data['item'][item_name][1]
    return data

def update_item_price(data,item_name,updated_price):
    data['item'][item_name][1] = updated_price
    data['item'][item_name][2] = data['item'][item_name][0]*data['item'][item_name][1]
    return data

def insert_to_table(data):
    print(f"{'NO':<3}  {'Nama Item':<17} {'Jumlah Item':<17} {'Harga/Item':<17} {'Total Harga':<17}")
    count = 1
    for item in data['item'].keys():
        NO              = count
        NAMA_ITEM       = item
        JUMLAH_ITEM     = data['item'][item][0]
        HARGA           = data['item'][item][1]
        JUMLAH_HARGA    = data['item'][item][2]

        print(f"{NO:<3}  {NAMA_ITEM:<17} {JUMLAH_ITEM:<17} {HARGA:<17} {JUMLAH_HARGA:<17}")
        count += 1
        

def check_order(data):
    for i in data['item'].values():
        if np.isnan(i).any() :
            print('There is an inputation error!')
            return data
        else:
            print('Inputation is all correct!')
            return data


def check_out(data):
    sum  = 0
    disc = 0
    for i in data['item'].values():
        sum += i[-1]
            
    if sum > 500000 :
        disc = 0.07
        sum = sum * (1 - disc)
    
    elif sum > 300000 :
        disc = 0.06
        sum = sum * (1 - disc)
    else : 
        disc = 0.06
        sum = sum * (1 - disc)
    print(f"Untuk Transaksi {data['user']['id']} berikut detailnya :")
    insert_to_table(data)
    print(f"\nDiscount : {disc}\nTotal Price : {sum}\n")

    return disc, sum
  
if __name__ == "__main__":
    id = transaction_id(10)
    data = transaction_obj(id)
    add_item(data,'mobil', 1, 10000)
    print(data)
    add_item(data,'motor', 2, 2000)
    print(data)
    #delete_item(data, 'mobil')
    print(data)
    update_item_name(data,'motor','motorcycle')
    update_item_qty(data,'motorcycle',3)
    print(data)
    update_item_price(data,'motorcycle',3000)
    print(data['item'].values())
    check_order(data)

    disc, total = check_out(data)

    reset_transaction(data)
   