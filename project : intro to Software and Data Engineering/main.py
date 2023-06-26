from function.transaction import *
from function.program_flow import *



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
    data = reset_transaction(data)
    print(data)