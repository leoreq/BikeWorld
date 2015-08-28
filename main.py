from bicycles import Client
from bicycles import BikeStore
from bicycles import Bike

   
def main():

    #Bike Stocking
    SD=Bike("SD",23.5)
    BikeLandia=BikeStore("Bikelandia",10000)
    BikeLandia.buy(SD)
    BikeLandia.buy(SD)
    Plaza=Bike("Plaza",24)
    BikeLandia.buy(Plaza)
    Downtown=Bike("Downtowm",25.5)
    BikeLandia.buy(Downtown)
    
    #Open for business
    Dan=Client("Dan",200)
    Dan.buy(BikeLandia)
    
    ultraDowntown=Bike("ultraDowntown",29)
    BikeLandia.buy(Downtown)
    BikeLandia.buy(ultraDowntown)
    
    Dan.buy(BikeLandia)
    
    Leo=Client("Leonidas",1000)
    Leo.buy(BikeLandia)
    
    Locaso=Client("Locaso",500)
    Locaso.buy(BikeLandia)
     
if __name__=='__main__':
    main()

