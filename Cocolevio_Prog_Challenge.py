#COCOLEVIO PROGRAMMING CHALLENGE
#DENNIS HANNUSCH
#Code written in Python



# Using class structure to store the data
class company:

    def __init__(self,companyName,amount,price):
        self.name = companyName
        self.amount = amount
        self.price = price
        # Calculate utility in order to compare values
        self.utility = price - amount


# Marketplace class holds methods for the sorting and maximization algorithm
class marketplace:

    def __init__(self):
        # Here are the variables for profit and the
        # materials sold to be able to access later outside of the class
        self.profit = 0
        self.materials_sold = 0

           
    def maximize(self,cList,mAmount):
        # Parse through list to find which companies to sell to
        # Sort this list of companies using Insertion Sort method
        companyList = self.InsertionSort(cList)
        
        material_amount = mAmount           # -> the amount of materials available to sell
        done = False                        # -> flag to stop while loop
        index = len(companyList)-1          # -> index starts at the end of the list where the greatest utility is
        sell_to = []                        # -> sell_to list will store which companies we should sell to

        while(not done and index>=0):
            self.materials_sold += companyList[index].amount
            if(self.materials_sold==material_amount):
                self.profit += companyList[index].price
                sell_to.append(companyList[index].name)
                done = True
            elif(self.materials_sold>material_amount):
                self.materials_sold -= companyList[index].amount
            else:
                self.profit += companyList[index].price
                sell_to.append(companyList[index].name)
            index -= 1

        return(sell_to)
    

    # Using insertion sort algorithm to sort the data by utility values
    # Insertion Sort will be the fastest because it is assumed that the
    # data will be nearly sorted
    def InsertionSort(self,companyUtil):
        
        for index in range(1,len(companyUtil)):
            currentValue = companyUtil[index].utility
            currentCompany = companyUtil[index]
            position = index

            while position>0 and companyUtil[position-1].utility>currentValue:
                companyUtil[position] = companyUtil[position-1]
                position = position - 1

            companyUtil[position] = currentCompany

        return(companyUtil)



def main():

    # Enter sample data in order to test the code by
    # creating a list of company class objects
    companyList = []
    companyList.append(company("A",1,1))
    companyList.append(company("B",2,5))
    companyList.append(company("C",3,8))
    companyList.append(company("D",4,9))
    companyList.append(company("E",5,10))
    companyList.append(company("F",6,17))
    companyList.append(company("G",7,17))
    companyList.append(company("H",8,20))
    companyList.append(company("I",9,24))
    companyList.append(company("J",10,30))

    # Enter the total amount of material in supply
    material_amount = eval(input("Enter the total amount of materials to be sold: "))
    print()

    # Creates a marketplace object
    MaterialMarket = marketplace()

    # maximize function with parameters companyList and material_amount
    # returns the results
    results = MaterialMarket.maximize(companyList,material_amount)      

    # Display the results
    print("Sell Materials To Companies:",results)
    print("Materials Sold:",MaterialMarket.materials_sold," Profit:",MaterialMarket.profit)


main()
