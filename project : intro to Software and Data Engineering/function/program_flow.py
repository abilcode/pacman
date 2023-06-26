from function.transaction import *
#from transaction import *

def action():
    run = True
    id = transaction_id(10)
    data = transaction_obj(id)
    while run : 
        print("Masukan input untuk melakukan action")
        print("Action : ")
        action = [str(i) for i in range(5)]
        for i in action:
            print(i)
        ipt = str(input("Masukan input : "))
        if ipt == '0':
            run = False
        

if __name__ == "__main__":
    action()