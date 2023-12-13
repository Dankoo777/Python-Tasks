class Medicine:
    def __init__(self,med_id,med_name,manufacturer,price,quantity):
        self.med_id = med_id
        self.med_name = med_name
        self.manufacturer = manufacturer
        self.price = price
        self.quantity = quantity
    def Display(self):
        print(f"Med ID: {self.med_id}\nMed Name: {self.med_name}\nManufacturer: {self.manufacturer}\nPrice: {self.price}\nQuantity: {self.quantity}\n")
    def Sale(self,quantity_sold):
        self.quantity -= quantity_sold
        if self.quantity < 0:
            self.quantity = 0
        print(f"Quantity NOW: {self.quantity}\n")
    def Purchase(self,quantity_bought):
        self.quantity += quantity_bought
        print(f"Quantity NOW: {self.quantity}\n")

def Search_by_name(lst,name):
    count = 0
    for med in lst:
        if med.med_name == name:
            print("There is medicine with that name")
            print(med.Display())
            count += 1
    if count == 0:
        print("No medicine with that name!!")
    
def Sort_Meds(lst):
    lst.sort(key = lambda x: x.med_name)
    for med in lst:
        print(med.Display())

n = int(input("Input number of meds: "))
Meds = []
for i in range(n):
    id = input("Input Med ID: ")
    name = input("Input Med Name: ")
    manuf = input("Input Manufacturer: ")
    price = int(input("Input Price: "))
    quantity = int(input("Input Quantity: \n"))
    med = Medicine(id,name,manuf,price,quantity)
    Meds.append(med)
searched_name = input("Input Med name to search: \n")
Sort_Meds(Meds)
Search_by_name(Meds,searched_name)
sold = int(input("Input quantity sold: \n"))
for med in Meds:
    if med.med_name == searched_name:
        med.Sale(sold)

    