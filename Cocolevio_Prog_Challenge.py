#COCOLEVIO PROGRAMMING CHALLENGE
#DENNIS HANNUSCH



# Using class structure to store the data
class company:

    def __init__(self,companyName,amount,price):
        self.name = companyName
        self.amount = amount
        self.price = price
        # Calculate utility in order to compare values
        self.utility = price - amount


# Using insertion sort algorithm to sort the data by utility values
# This sorting algorithm will sort the data from greatest to least
def InsertionSort(companyUtil):
    
    for index in range(1,len(companyUtil)):
        currentValue = companyUtil[index].utility
        currentCompany = companyUtil[index]
        position = index

        while position>0 and companyUtil[position-1].utility<currentValue:
            companyUtil[position] = companyUtil[position-1]
            position = position - 1

        companyUtil[position] = currentCompany




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

    # Displaying the data before sorting
    print("--Pre-Sorted Data--")
    for c in companyList:
        print("Company:",c.name," Amount:",c.amount," Price:",c.price," Util:",c.utility) 
    print()

    # Enter the total amount of material in supply
    material_amount = input("Enter the total amount of materials to be sold: ")
    print()
    
    # Sort the data by utlity
    InsertionSort(companyList)

    # Displaying the data after sorting
    print("--Companies sorted by utility--")
    for c in companyList:
        print("Company:",c.name," Amount:",c.amount," Price:",c.price," Util:",c.utility) 
    print()

    # Parse through list to find which companies to sell to


    # Display the results


    


main()
