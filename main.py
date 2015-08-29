from bicycles import *

   
def main():
    #Bike part building
    #SDWheel=Wheels("SDWheels",23.5*0.3)
    #SDWheels=Wheels("SDWheels",23.5*0.3)
    #SDFrame=Frame("SDFrame",23.5*0.7)
    #PlazaWheel=Wheels("PlazaWheels",24*0.3)
    #PlazaWheels=Wheels("PlazaWheels",24*0.3)
    #PlazaFrame=Frame("PlazaFrame",24*0.7)
    #DowntownWheel=Wheels("DowntownWheels",25.5*0.3)
    #DowntownFrame=Frame("DowntownFrame",25.5*0.7)
    #ultraDowntownWheel=Wheels("ultraDowntownWheels",29*0.3)
    #ultraDowntownFrame=Frame("ultraDowntownFrame",29*0.7)
    ###Manufacturer in  Business
    SDManufacturing=Manufacturer("SDManufacturing",["SD",23.5],0.3)
    print(SD.model)
    print(type(SD))
    
    PlazaManufacturing=Manufacturer("PlazaManufacturing",["Plaza",24],0.3)
    DowntownManufacturing=Manufacturer("DowntownManufacturing",["Downtown",25.5],0.3)
    ultraDowntownManufacturing=Manufacturer("ultraDowntownManufacturing",["ultraDowntown",29],0.3)
    
    #Bike Building
    #SD=Bike("SD",SDFrame,SDWheel)
    #Plaza=Bike("Plaza",PlazaFrame,PlazaWheel)
    #Downtown=Bike("Downtown",DowntownFrame,DowntownWheel)
    #ultraDowntown=Bike("ultraDowntown",ultraDowntownFrame,ultraDowntownWheel)
    
    #Bike Open Market
    BikeLandia=BikeStore("Bikelandia",10000)
    BikeLandia.buy(SD)
    BikeLandia.buy(SD)
    BikeLandia.buy(Plaza)
    BikeLandia.buy(Downtown)
    
    #Open for business
    Dan=Client("Dan",200)
    Dan.buy(BikeLandia)
    
    BikeLandia.buy(Downtown)
    BikeLandia.buy(ultraDowntown)
    
    Dan.buy(BikeLandia)
    
    Leo=Client("Leonidas",1000)
    Leo.buy(BikeLandia)
    
    Locaso=Client("Locaso",500)
    Locaso.buy(BikeLandia)
     
if __name__=='__main__':
    main()

