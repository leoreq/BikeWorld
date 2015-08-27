class Bike(object):
    """"This class will build a bike and price it in inverse relationship to the weight"""
    def __init__(self,model,weight):
        self.model=model
        self.weight=self.checkWeight(weight)
        self.price=self.setPrice(self.weight)
        print""
        print("A great Machine has been built !!! \nFor only {} $, you can have a - {} Freestyle Bike - that weighs {} pounds").format(self.price,self.model,self.weight)
    
    def checkWeight(self,insertWeight):
        """Weight calculation Sanity Check: Given the price creation formulae, weight has to be always above the 21.6 thresshold"""
        while (insertWeight<21.6):
            print(" WEIGHT LOAD ERROR: weight has to be in pounds and above 21.6 , please insert again.")
            reinsertedWeight=raw_input()
            insertWeight=round(float(reinsertedWeight),2)
        return insertWeight
        
    def setPrice(self,insertWeight):
        """Price has an inverse relationship to weight, prices are modeled according to ->http://www.thebicyclelink.com/haro/masi-2015 """
        price=round((40000/((insertWeight-21.5)*insertWeight)),2)
        return price

class BikeStore(object):
    def __init__(self,name,cash):
        self.name=name
        self.cash=cash
        inventory=dict()
        self.inventory=inventory
        print""
        print ("{} has been invested in the bike industry , and finally now {} is open for business").format(self.cash,self.name)
        
    def buy(self,bike):
        """this will update the inventory dictionary with the model,n price. We can then worry about adding same types"""
        ##print("DEBUGGING: check if the bike object info is accesible. The bike name is {}").format(bike.model)
        if (bike.price>self.cash):
            print(" Not enough CASH for the operation. You have {} and need {} ").format(self.cash,bike.price)
        else:
            self.cash-=bike.price
            modelCount=self.inventory.get(bike.model,[0,0])[1]
            ##print("DEBUGGING the list within the dict:Value is {}").format(modelCount)
            self.inventory[bike.model]=[bike.price,modelCount+1]
            #Assumtion: We will be using "market Price", last price will be set for the whole stock as current price"
            print""
            print("Nice Purchase from {} store. \nIt now has {} bikes of - {} model - ,priced at {} each").format(self.name,self.inventory[bike.model][1],bike.model,self.inventory[bike.model][0])

SD=Bike("SD",22)

BikeLandia=BikeStore("Bikelandia",5000)
BikeLandia.buy(SD)
BikeLandia.buy(SD)
SD=Bike("Plaza",23)
BikeLandia.buy(SD)

print(BikeLandia.inventory)
