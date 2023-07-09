#from function.transaction import *
from transaction import *
# from database import *

def action():
    run = True
    id = transaction_id(10)
    data = transaction_obj(id)
    while run : 
        print("Masukan input untuk melakukan action")
        print("Action : ")
        array_action = ['Exit','Add Items','Reset Transaction','Delete Item','Update Item Name','Update Item Quantity','Update Item Price','Check Orders','Checkout']

        for count,act in enumerate(array_action):
            print(f'{count} {act}')
        ipt = str(input("Masukan input : "))

        if ipt == '0':
            print('Berikut adalah transaksi final:')
            run = False

        if ipt == '1':
            add_item(data)

        elif ipt =='2':
            data = reset_transaction(data)
            print('Transaksi telah direset, silahkan melakukan input kembali!')

        elif ipt == '3':
            if len(data['item'])!=0:
                print('Items sementara di keranjang :')
                insert_to_table(data)
                delete_item(data,item_name=None)
            else :
                print('Keranjang anda kosong! silahkan mencari barang terlebih dahulu!')
        
        elif ipt =='4':
            insert_to_table(data)
            update_item_name(data,item_name=None,updated_name=None)
            print('Nama telah diubah, pastikan sudah benar!')

        elif ipt =='5':
            insert_to_table(data)
            update_item_qty(data,item_name=None,updated_counts=None)
            print('Jumlah barang telah diubah, pastikan sudah benar!')
        
        elif ipt =='6':
            insert_to_table(data)
            update_item_price(data,item_name=None,updated_price=None)
            print('Harga barang telah diubah, pastikan sudah benar!')

        elif ipt == '7':
            check_order(data)

        else:
            check_out(data)
            ipt = '0'
        

if __name__ == "__main__":
    action()