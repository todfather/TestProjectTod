#this doesn't work, i just used https://helpdeskgeek.com/how-to/generate-a-list-of-installed-programs-in-windows/ instead
import win32com.client 
strComputer = "." 
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator") 
objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2") 
colItems = objSWbemServices.ExecQuery("Select * from Win32_Product") 
for objItem in colItems: 
    print("Caption: ", objItem.Caption)
    print("Description: ", objItem.Description )
    print("Identifying Number: ", objItem.IdentifyingNumber )
    print("Install Date: ", objItem.InstallDate)
    print("Install Date 2: ", objItem.InstallDate2 )
    print("Install Location: ", objItem.InstallLocation )
    print("Install State: ", objItem.InstallState )
    print("Name: ", objItem.Name )
    print("Package Cache: ", objItem.PackageCache )
    print("SKU Number: ", objItem.SKUNumber )
    print("Vendor: ", objItem.Vendor )
    print("Version: ", objItem.Version) 
