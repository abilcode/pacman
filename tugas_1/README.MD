Please Install the requirement.txt on you virtual env!

## Explaination : 
         +-----------------+
         |   Start Program |
         +--------+--------+
                  |
                  v
           +------+------+-------------------------+
           |               action()               |
           +------+------+-------------------------+
                  |
                  v
         +--------+-------+-------------------------+
         |  Print Menu    |   Get User Input         |
         |   Options      |    (action to perform)   |
         +--------+-------+-------------------------+
                  |
                  v
      +-----------+------------+
      |  Perform Selected     |
      |   Action Function     |
      +-----------+------------+
                  |
                  v
           +------+------+-------------------------+
           |               Check Input             |
           +------+------+-------------------------+
                  |
         +--------+-------+---------+
         |   If Input is '0' | Exit   |
         +--------+-------+---------+
                  |
                  v
        +---------+-----------+
        |   Print Final       |
        |   Transaction      |
        +---------+-----------+
                  |
                  v
         +--------+--------+
         |   End Program   |
         +-----------------+


The program starts by calling the action() function.
The action() function displays a menu of options to the user and waits for input.
Based on the user's input, the corresponding action function is executed.
After performing the action, the program checks the user's input to determine the next steps.
If the input is '0' (Exit), the program prints the final transaction and ends.
If the input is any other value, the program loops back to the menu to allow the user to select another action.
The loop continues until the user chooses to exit by entering '0'.
Note: The code includes several function definitions (transaction_obj, transaction_id, add_item, delete_item, reset_transaction, update_item_name, update_item_qty, update_item_price, insert_to_table, check_order, check_out) that are called within the action() function. However, their flow and internal logic are not explicitly shown in the provided code snippet.


```
log tugas 1 : 
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 1
None None None
Masukan Nama Barang : ayam
Masukan Jumlah Barang : 1
Masukan Harga Barang per-Buah : 1000
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 7
Inputation is all correct!
NO   Nama Item         Jumlah Item       Harga/Item        Total Harga      
1    ayam              1                 1000.0            1000.0           
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 1
None None None
Masukan Nama Barang : pasta gigi
Masukan Jumlah Barang : 1
Masukan Harga Barang per-Buah : 1500
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 7
Inputation is all correct!
NO   Nama Item         Jumlah Item       Harga/Item        Total Harga      
1    ayam              1                 1000.0            1000.0           
2    pasta gigi        1                 1500.0            1500.0           
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 3
Items sementara di keranjang :
NO   Nama Item         Jumlah Item       Harga/Item        Total Harga      
1    ayam              1                 1000.0            1000.0           
2    pasta gigi        1                 1500.0            1500.0           
Masukan Nama Barang yang ingin dihapus: pasta gigi
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 7
Inputation is all correct!
NO   Nama Item         Jumlah Item       Harga/Item        Total Harga      
1    ayam              1                 1000.0            1000.0           
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 1   
None None None
Masukan Nama Barang : sapi
Masukan Jumlah Barang : 1
Masukan Harga Barang per-Buah : 10000
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 7
Inputation is all correct!
NO   Nama Item         Jumlah Item       Harga/Item        Total Harga      
1    ayam              1                 1000.0            1000.0           
2    sapi              1                 10000.0           10000.0          
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 2
Transactions have been restarted!
Transaksi telah direset, silahkan melakukan input kembali!
NO   Nama Item         Jumlah Item       Harga/Item        Total Harga      
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 1
None None None
Masukan Nama Barang : ayam
Masukan Jumlah Barang : 1
Masukan Harga Barang per-Buah : 1000
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 1
None None None
Masukan Nama Barang : kambing
Masukan Jumlah Barang : 1
Masukan Harga Barang per-Buah : 2000
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 4
NO   Nama Item         Jumlah Item       Harga/Item        Total Harga      
1    ayam              1                 1000.0            1000.0           
2    kambing           1                 2000.0            2000.0           
Masukan nama barang yang ingin diganti: ayam
Masukan nama pengganti barang: itik
Nama telah diubah, pastikan sudah benar!
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 7
Inputation is all correct!
NO   Nama Item         Jumlah Item       Harga/Item        Total Harga      
1    kambing           1                 2000.0            2000.0           
2    itik              1                 1000.0            1000.0           
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 5
NO   Nama Item         Jumlah Item       Harga/Item        Total Harga      
1    kambing           1                 2000.0            2000.0           
2    itik              1                 1000.0            1000.0           
Masukan nama barang yang ingin diganti: kambing
Masukan jumlah pengganti dari barang kambing: 2
Jumlah barang telah diubah, pastikan sudah benar!
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 7
Inputation is all correct!
NO   Nama Item         Jumlah Item       Harga/Item        Total Harga      
1    kambing           2                 2000.0            4000.0           
2    itik              1                 1000.0            1000.0           
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 6
NO   Nama Item         Jumlah Item       Harga/Item        Total Harga      
1    kambing           2                 2000.0            4000.0           
2    itik              1                 1000.0            1000.0           
Masukan nama barang yang ingin diganti: ayam
Masukan harga pengganti dari barang ayam: 1300
Traceback (most recent call last):
  File "/Users/abilfad/Documents/CODE/pacman/tugas_1/project : intro to Software and Data Engineering/main.py", line 7, in <module>
    action()
  File "/Users/abilfad/Documents/CODE/pacman/tugas_1/project : intro to Software and Data Engineering/function/program_flow.py", line 51, in action
    update_item_price(data,item_name=None,updated_price=None)
  File "/Users/abilfad/Documents/CODE/pacman/tugas_1/project : intro to Software and Data Engineering/function/transaction.py", line 81, in update_item_price
    data['item'][item_name][1] = updated_price
KeyError: 'ayam'
(pacman) abilfad@abils-MacBook-Air pacman % /opt/anaconda3/envs/pacman/bin/python "/Users/abilfad/Documents/CODE/pacman/tugas_1/project : intro to Software and Data E
ngineering/main.py"
 Randomly generated string is:  256w23uuwt
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 1
None None None
Masukan Nama Barang : ayam
Masukan Jumlah Barang : 1
Masukan Harga Barang per-Buah : 1000
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 6
NO   Nama Item         Jumlah Item       Harga/Item        Total Harga      
1    ayam              1                 1000.0            1000.0           
Masukan nama barang yang ingin diganti: ayam
Masukan harga pengganti dari barang ayam: 1300
Harga barang telah diubah, pastikan sudah benar!
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 7
Inputation is all correct!
NO   Nama Item         Jumlah Item       Harga/Item        Total Harga      
1    ayam              1                 1300.0            1300.0           
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 2
Transactions have been restarted!
Transaksi telah direset, silahkan melakukan input kembali!
NO   Nama Item         Jumlah Item       Harga/Item        Total Harga      
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 1
None None None
Masukan Nama Barang : kasur
Masukan Jumlah Barang : 10000
Masukan Harga Barang per-Buah : 2000
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 7
Inputation is all correct!
NO   Nama Item         Jumlah Item       Harga/Item        Total Harga      
1    kasur             10000             2000.0            20000000.0       
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 7
Inputation is all correct!
NO   Nama Item         Jumlah Item       Harga/Item        Total Harga      
1    kasur             10000             2000.0            20000000.0       
Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 8
Untuk Transaksi <built-in function id> berikut detailnya :
NO   Nama Item         Jumlah Item       Harga/Item        Total Harga      
1    kasur             10000             2000.0            20000000.0       

Discount : 0.07
Total Price : 18600000.0

Masukan input untuk melakukan action
Action : 
0 Exit
1 Add Items
2 Reset Transaction
3 Delete Item
4 Update Item Name
5 Update Item Quantity
6 Update Item Price
7 Check Orders
8 Checkout
Masukan input : 0
Berikut adalah transaksi final:
NO   Nama Item         Jumlah Item       Harga/Item        Total Harga      
1    kasur             10000             2000.0            20000000.0       
Untuk Transaksi <built-in function id> berikut detailnya :
NO   Nama Item         Jumlah Item       Harga/Item        Total Harga      
1    kasur             10000             2000.0            20000000.0       

Discount : 0.07
Total Price : 18600000.0

(pacman) abilfad@abils-MacBook-Air pacman % 

```