#from Tkinter import *
#root = Tk()
#root.mainloop()
from datetime import *
import csv
import pandas as pd

guest_list = pd.read_csv("C:\Users\MSI CES 2014\Documents\IST 303 GuestList.csv", index_col = 0)
service_list = pd.read_csv("C:\Users\MSI CES 2014\Documents\IST 303 services.csv", index_col = 0)



class customer:

    def __init__(self, input_id):
        self.input_id = input_id

    def check_for_cust(self):
        for lab, row in guest_list.iterrows():
            if answer.input_id== lab:
                print "yes"
                return True
        print "no"
        return False

    def lookup_service(self):
        #if not customer.check_for_cust():
        #    return
        for lab, row in guest_list.iterrows():
            if answer.input_id == lab:
                print "Customer ID is valid. Here are the reservation info"
                print row
                for lab1, row1 in service_list.iterrows():
                    if answer.input_id == lab1:
                        print row1
                print "No reservation yet"
                return
        print "Customer ID is not valid"






class reservations(customer):
    def __init__(self, mineral_bath, massage, facial, specialty):
        self.mineral_bath = mineral_bath
        self.massage = massage
        self.facial = facial
        self.specialty = specialty




#answer = customer(input("Enter customer ID"))
#answer.check_for_cust()


answer = customer(input("Enter customer ID"))
#answer.check_for_cust()
answer.lookup_service()



