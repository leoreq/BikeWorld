def printProduced(item,price,model,weight):
    print""
    print("A new {} has been built \nFor only {} $, you can have a - {} - that weighs {} pounds").format(item,price,model,weight)
    
def checkWeight(insertWeight,factor):
        """Weight calculation Sanity Check: Given the price creation formulae, weight has to be always above the 21.6 per bike thresshold"""
        while (insertWeight<21.6*factor):
            print(" WEIGHT LOAD ERROR: weight has to be in pounds and above {}, please insert again.").format(21.6/factor)
            reinsertedWeight=raw_input()
            insertWeight=round(float(reinsertedWeight),2)
        return insertWeight
        
def setPrice(insertWeight,factor):
    """Price has an inverse relationship to weight, prices are modeled according to ->http://www.thebicyclelink.com/haro/masi-2015 """
    price=round((40000*factor/((insertWeight/factor-21.5)*insertWeight/factor)),2)
    return price

class Wheels(object):
    """"This class will represent wheels"""
    def __init__(self,model,weight):
        self.model=model
        self.factor=0.3
        self.weight=checkWeight(weight,self.factor)
        self.price=setPrice(self.weight,self.factor)
        printProduced(self.__class__.__name__,self.price,self.model,self.weight)

class Frame(object):
    """"This class will represent Frames"""
    def __init__(self,model,weight):
        self.model=model
        self.factor=0.7
        self.weight=checkWeight(weight,self.factor)
        self.price=setPrice(self.weight,self.factor)
        printProduced(self.__class__.__name__,self.price,self.model,self.weight)


class Bike(object):
    """"This class will build a bike and price it in inverse relationship to the weight"""
    def __init__(self,model,frame,wheels):
        self.model=model
        self.frame=frame
        self.wheels=wheels
        self.weight=self.checkWeight(frame.weight+wheels.weight)
        self.price=self.setPrice(self.weight)
        print""
        print("A great Machine has been built !!! \nFor only {} $, you can have a - {} Freestyle Bike - that weighs {} pounds.\n It has a {} frame and {} Wheels ").format(self.price,self.model,self.weight,self.frame.model,self.wheels.model)
    
    def checkWeight(self,insertWeight):
        """Weight calculation Sanity Check: Given the price creation formulae, weight has to be always above the 21.6 per bike thresshold"""
        while (insertWeight<21.6):
            print(" WEIGHT LOAD ERROR: weight has to be in pounds and above 21.6 , please insert again. Current weight is {}").format(insertWeight)
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
        self.margin=0.2
        self.profit=0
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
            self.printInventory()
            
    def sell(self,model):
        modelPrice=self.inventory.get(model,[0,0])[0]
        modelCount=self.inventory.get(model,[0,0])[1]
        print""
        if (modelCount==0):
            print("{} model is not in stock. Please check our list of available items.").format(model)
        else:
            markupPrice=modelPrice*(1+self.margin)
            self.inventory[model]=[modelPrice,modelCount-1]
            self.profit+=(markupPrice-modelPrice)
            self.cash+=markupPrice
            print("Model {} - has been sold for {}, leaving only {} in stock. The profit of the operation is {} and the company now has {} of cash.").format(model,markupPrice,self.inventory[model][1],(markupPrice-modelPrice),self.cash)
            self.printInventory()
    def printInventory(self):
        print""
        print ("{} inventory is now:").format(self.name)
        for model,priceList in self.inventory.iteritems():
            print("Model: {} || Price: {} || Quantity: {} ").format(model,priceList[0],priceList[1])

class Client(object):
    """This class will represent the behaviour of a bike lover. Will buy the best bike he can afford."""
    def __init__(self,name,cash):
        self.name=name
        self.cash=cash
        self.assets=dict()
        print ""
        print ("We welcome {} to this bike lovin block. You have {} to spend as you wish.").format(self.name,self.cash)
    
    def buy(self,store):
        """Buying function will check all items, and choose the most expensive it can afford."""
        modelChosen=""
        priceChosen=0
        for model,priceList in store.inventory.iteritems():
            if (priceList[1]<=0) or (priceList[0]>self.cash) or (priceChosen>=priceList[0]):#this condition looks to check the price only if there is ammount of stock to sell and price can be aforded.
                continue
            else:
               priceChosen=priceList[0]
               modelChosen=model
        if (modelChosen!=""):
            self.cash-=priceChosen
            self.assets[modelChosen]=[priceChosen]
            print ""
            print("{} has just added a {} to his ownership. He spent {} and now has {} left.").format(self.name,modelChosen,priceChosen,self.cash)
            store.sell(modelChosen)
        else: print("Sorry {}. {} has no bike that fits you, please come back again !!").format(self.name,store.name)
        