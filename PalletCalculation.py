"""
There is types of spools: small or bigs. The small ones have half of heigh of the big ones.
For now is difined each spool layer have 12 spools.

How many pallets are need?
How many layers there are on last pallet?
How many spools there on last layer?
"""
#read inputs
spoolsQuantity  =int(input("Fill the spool number to load   "))
spoolsType      =int(input("Spool type: Big Spools -> 1 Small Spools -> 2   "))

configLayersPallet=spoolsType*3
configSpoolsByLayer=12

def palletQty(spoolsQty,spoolsByLayer,maxLayers):
    palletDict={}
    spoolsByPallet  =spoolsByLayer*maxLayers
    palletQty       =spoolsQty/spoolsByPallet

    spoolsLastPallet    =(palletQty-int(palletQty))*spoolsByPallet
    layersLastPallet    =spoolsLastPallet/spoolsByLayer
    spoolsLastLayer     =(spoolsLastPallet-int(layersLastPallet)*spoolsByLayer);  
          
    if spoolsLastPallet>0:
        tempPalletQty=int(palletQty)+1
    else:
        tempPalletQty=int(palletQty)
 
    if spoolsLastLayer>0:
        tempLayersLastPallet=int(layersLastPallet)+1
        tempSpoolsLastlayer=int(spoolsLastLayer)
    else:
        tempLayersLastPallet=int(layersLastPallet)
        tempSpoolsLastlayer=spoolsByLayer

    palletDict["PalletQty"]                 =tempPalletQty    
    palletDict["CompledtedPalletQty"]       =int(palletQty)
    palletDict["LayersLastPallet"]          =tempLayersLastPallet 
    palletDict["CompletedLayersLastPallet"] =int(layersLastPallet)
    palletDict["SpoolsLastLayer"]           =int(tempSpoolsLastlayer)
    
    #Plausability Check Results
    spoolsCalculation=palletDict["CompledtedPalletQty"]*spoolsByPallet+palletDict["CompletedLayersLastPallet"]*spoolsByLayer+spoolsLastLayer
    if spoolsCalculation==spoolsQty:
        palletDict["DataOk"]="OK"
    else:
        palletDict["DataOk"]="NOK"   
    return palletDict

if spoolsType!=1 and spoolsType!=2:
    print("Error - Spool Type Does Not Exist")
else: 
    print(palletQty(spoolsQuantity,configSpoolsByLayer,configLayersPallet))

