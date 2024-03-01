import mysql.connector as connector 
from datetime import datetime
import time
import os

connectionObject = connector.connect(host="localhost", user = "root", password = "root", database = "Parkingsystem")
cursorObject = connectionObject.cursor()

# registration function 
def registerAdmin():
    print("********************************************************************************\n")
    print("\t\t ****** ADMIN REGISTRATION PAGE ****** \n")
    print("********************************************************************************\n")
    AdminName = input("Enter admin name: ")
    AdminPassword = input("Enter admin Password: ")
    print("********************************************************************************\n")
    print("\t\t\tRegistering Admin...")
    time.sleep(1)
    print("\t\t\tRegistered Succesfully")
    time.sleep(2)
    os.system("cls")

    query = "insert into adminTable(admin_name, admin_password) values ('{}','{}')".format(AdminName,AdminPassword)
    cursorObject.execute(query)
    connectionObject.commit()

    # cursorObject = connectionObject.cursor()
    query = "select admin_id from adminTable where admin_name =  '{}'  and admin_password = '{}' ".format(AdminName,AdminPassword)
    cursorObject.execute(query)

    for id in cursorObject:
        print("\n\n")
        print("\t\t\tAdmin ID for '{}' is : {}".format(AdminName,id[0]))

    
    return True

# login function
def IsLoggedIn(username, password, adminId):
    query = "select admin_name, admin_password from adminTable where admin_id = {}".format(adminId)
    cursorObject.execute(query)

    for data in cursorObject:
        if data[0] == username:
            if data[1] == password:
                return True
            else:
                return False
        else:
            print("Username or Password Mismatched!!")

def displayFunctionnality():
    print("1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. Parking Status")
    print("4. Add Slot")
    print("5. Remove Slot")
    print("6. Exit")

def Showstatus(optionId):
    print("\n")
    print("\t\t\t\t    :: SHOWING PARKING STATUS ::\n")
    if optionId == 1:
        query = "select parking_id, occupied from fourwheeler"
        cursorObject.execute(query)
        for data in cursorObject:
            print(" \t\t\t\t'{}'\t\t\t\t{}".format(data[0],data[1]))
            if data[1] == 0:
                avail = True
            else:
                avail = False
    
    return avail

# recent data table insertion/ updation
def insertToCustomerData(VehicleNumber, Duration):
    query = "select entry_time, exit_time from fourwheeler where vehicle_no = '{}'".format(VehicleNumber)
    cursorObject.execute(query)
    

    Customerdata = cursorObject.fetchone()
    CustomerEntryTime, CustomerExitTime = Customerdata
    
    fineCharged = Duration * 0.167
    fineCharged = round(fineCharged)
    
    query = "insert into customerdata(vehicle_no, entry_time,exit_time,duration,paid_amount) values ('{}','{}','{}',{},{})".format(VehicleNumber,CustomerEntryTime,CustomerExitTime,Duration,fineCharged)
    cursorObject.execute(query)
    connectionObject.commit()
    

def VehicleParkingStatus(ParkingChoice):
    if ParkingChoice == 1:
        print("***********************************************************************************************")
        print("{:<15} {:<15} {:<20} {:<15} {:<15}".format("PARKING ID", "VEHICLE NO", "ENTRY TIME", "EXIT TIME", "PARKING STATUS"))
        query = "select * from fourwheeler"
        cursorObject.execute(query)

        print("***********************************************************************************************")
        for row in cursorObject:
            formatted_row = []
            for i,item in enumerate(row):
                if item is None:
                    formatted_row.append("None")
                elif i in [2, 3]:  # Index 2 and 3 correspond to entry time and exit time
                    formatted_row.append(item.strftime("%Y-%m-%d %H:%M:%S"))
                else:
                    formatted_row.append(item)
            print("{:<15} {:<15} {:<20} {:<15} {:<15}".format(*formatted_row))
        print("***********************************************************************************************")
        # print("************************************************************************")
    elif ParkingChoice == 2:
        print("PARKING ID\tVEHICLE NO\tENTRY TIME\t\tEXIT TIME\tPARKING STATUS")
        query = "select * from twowheeler"
        cursorObject.execute(query)

        for data in cursorObject:
            print("'{}'\t\t'{}'\t\t'{}'\t\t'{}'\t\t{}".format(data[0],data[1],data[2],data[3],data[4]))
    
    
    
    
    
    

# driver code
ans = "y"
while ans == "y":
    os.system("cls")
    print("********************************************************************************\n")
    print("\t\t\t\tParking system")
    print("\n********************************************************************************")
    
    print("\n\n1.Registration\n2.Login")
    print("\n********************************************************************************")
    choice = int(input("Enter the choice: "))
    os.system("cls")
    if choice == 1:
        if registerAdmin():
            pass
        else:
            print("\n\n")
            print("\t\t\tRegistration Unsuccessfull :( ")
    elif choice == 2:
        print("\n********************************************************************************\n")
        print("\t\t\t**** ADMIN LOGIN PAGE ****")
        print("\n********************************************************************************")
        
        id = int(input("Enter the Admin ID: "))
        userName = input("Enter Admin Username : ")
        PassWord = input("Enter Admin Password : ")
        print("\n********************************************************************************")
        os.system("cls")
        print("\t\t\tLogging In")
        time.sleep(2)
        if IsLoggedIn(username = userName, password= PassWord,adminId = id):
            print("\t\t\tSuccessfully Logged In..")
            time.sleep(2)
            os.system("cls")
            print("*********************************************************************************************")
            print("\t\t\t\t****  PARKING SYSTEM  ****")
            print("*********************************************************************************************\n\n")
            print("1. 4 Wheeler Parking \n2. 2 Wheeler Parking")
            print("\n\n*********************************************************************************************")
            parkingChoice = int(input("Enter the parking choice: "))
            if parkingChoice == 1:
                FourWheelerOption = "y"
                while FourWheelerOption == "y":
                    os.system("cls")
                    print("\n*********************************************************************************************")
                    print("\t\t\t\t**** 4 wheeler Parking ****")
                    print("\n*********************************************************************************************")
                    displayFunctionnality()
                    print("\n*********************************************************************************************")
                    FunctionChoice = int(input("Enter the option: "))
                    os.system("cls")
                    if FunctionChoice == 1:
                        # park vehicle
                        if Showstatus(parkingChoice) :
                            print("\n*********************************************************************************************")
                            parkVehicleId = input("\tEnter the parking Slot: ")
                            parkVehicleNo = input("\tEnter the vehicle Number: ")
                            parkStatus = int(input("\tEnter the Parking Status:(0/1) "))
                            query = "update fourwheeler set vehicle_no = '{}', entry_time = CURRENT_TIMESTAMP() , occupied = {} where parking_id = '{}' ".format(parkVehicleNo,parkStatus,parkVehicleId)
                            cursorObject.execute(query)
                            connectionObject.commit()
                            print("\n*********************************************************************************************\n")
                        else:
                            print("\tNo Slot found..")
                        
                        
                    elif FunctionChoice == 2:
                        os.system("cls")
                        print("\n*************************************************************************\n")
                        print("\t\t\t** REMOVE VEHICLE **")
                        print("\n*************************************************************************\n")
                        removeVehicleno = input("Enter the Vehicle No.: ")
                        print("\t\t\tRELEASING VEHICLE..")
                        time.sleep(2)
                        print("\n*************************************************************************\n")
                        query="update fourwheeler set exit_time = CURRENT_TIMESTAMP() where vehicle_no='{}'".format(removeVehicleno)
                        cursorObject.execute(query)
                        connectionObject.commit()
                        
                        
                        query = "SELECT TIMESTAMPDIFF(MINUTE, entry_time, exit_time) AS duration FROM fourwheeler WHERE vehicle_no = '{}'".format(removeVehicleno)
                        cursorObject.execute(query)
                        
                        DurationDifference = cursorObject.fetchone()[0]
                        print("Duration is : ",(DurationDifference/60))
                        
                        insertToCustomerData(removeVehicleno,DurationDifference)
                        
                        query = "update fourwheeler set vehicle_no = NULL, entry_time = NULL, exit_time = NULL, occupied = 0 where vehicle_no = '{}'".format(removeVehicleno)
                        cursorObject.execute(query)
                        connectionObject.commit()
                        
                    elif FunctionChoice == 3:
                        os.system("cls")
                        print("***********************************************************************************************")
                        print("\t\t\t   **** FOUR WHEELER PARKING STATUS ****\n")
                        VehicleParkingStatus(parkingChoice)
                        time.sleep(2)
                            
                    elif FunctionChoice == 4:
                        # add slot
                        os.system("cls")
                        print("***********************************************************************************************\n")
                        print("\t\t\t**** ADDING 4 WHEELER PARKING SLOT ****")
                        print("\n***********************************************************************************************")
                        SlotId = input("Enter the SLOT ID: ")
                        
                        query = "select parking_id from fourwheeler"
                        cursorObject.execute(query)
                            
                        for pId in cursorObject:
                            print(pId)
                            if pId[0] == SlotId:
                                val = 1
                                break
                            else:
                                val = 0
                                
                        print("val = ",val)
                        if val == 0:
                            query = "insert into fourwheeler(parking_id) values('{}')".format(SlotId)
                            cursorObject.execute(query)
                            connectionObject.commit()
                            print("SLOT ID ADD TO DATABASE")
                        else:
                            print("SLOT ID ALREADY EXISTS")
                        print("\n***********************************************************************************************")
                    
                    elif FunctionChoice == 5:
                        # remove slot
                        os.system("cls")
                        print("\n***********************************************************************************************\n")
                        print("\t\t\t**** REMOVING 4 WHEELER PARKING SLOT ****")
                        print("\n***********************************************************************************************\n")
                        SlotId = input("Enter the SLOT ID to Remove: ") 
                        query = "select parking_id from fourwheeler"
                        cursorObject.execute(query)
                            
                        for pId in cursorObject:
                            print(pId)
                            if pId[0] != SlotId:
                                val = 1
                                # break
                            else:
                                val = 0
                                
                        print("val = ",val)
                        if val == 0:
                            query = "delete from fourwheeler where parking_id = '{}'".format(SlotId)
                            cursorObject.execute(query)
                            connectionObject.commit()
                            print("SLOT ID REMOVED FROM DATABASE")
                        else:
                            print("SLOT ID DOES NOT EXISTS")
                        print("\n***********************************************************************************************\n")
                    else:
                        print("Entered Wrong Option")
                
                    FourWheelerOption = input("Do You Want To Continue With 4 wheel Parking:(y/n): ")
                            
            # 2 wheeler parking starts here 
            elif parkingChoice == 2:
                print("2 wheeler parking")
                displayFunctionnality()
                FunctionChoice = int(input("Enter the option: "))
                if FunctionChoice == 1:
                    # park vehicle
                    print('calling')
                    if Showstatus(parkingChoice) :
                        parkVehicleId = input("Enter the parking Slot: ")
                        parkVehicleNo = input("Enter the vehicle Number: ")
                        parkStatus = int(input("Enter the Parking Status:(0/1) "))
                        query = "update twowheeler set vehicle_no = '{}', entry_time = CURRENT_TIMESTAMP() , occupied = {} where parking_id = '{}' ".format(parkVehicleNo,parkStatus,parkVehicleId)
                        cursorObject.execute(query)
                        connectionObject.commit()
                    else:
                        print("No Slot found..")
                    
                    
                elif FunctionChoice == 2:
                    removeVehicleno = input("Enter the Vehicle No.: ")
                    query="update twowheeler set exit_time = CURRENT_TIMESTAMP() where vehicle_no='{}'".format(removeVehicleno)
                    cursorObject.execute(query)
                    connectionObject.commit()
                    
                    
                    query = "SELECT TIMESTAMPDIFF(MINUTE, entry_time, exit_time) AS duration FROM twowheeler WHERE vehicle_no = '{}'".format(removeVehicleno)
                    cursorObject.execute(query)
                    
                    DurationDifference = cursorObject.fetchone()[0]
                    print("Duration is : ",(DurationDifference/60))
                    
                    insertToCustomerData(removeVehicleno,DurationDifference)
                    
                    query = "update twowheeler set vehicle_no = NULL, entry_time = NULL, exit_time = NULL, occupied = 0 where vehicle_no = '{}'".format(removeVehicleno)
                    cursorObject.execute(query)
                    connectionObject.commit()
                    
                elif FunctionChoice == 3:
                    print("Parking Status")
                    print("2 Wheeler parking status")
                    VehicleParkingStatus(2)
                        
                elif FunctionChoice == 4:
                    # add slot
                    print("Addind slot")
                    SlotId = input("Enter the SLOT ID: ")
                    
                    query = "select parking_id from twowheeler"
                    cursorObject.execute(query)
                        
                    for pId in cursorObject:
                        print(pId)
                        if pId[0] == SlotId:
                            val = 1
                            break
                        else:
                            val = 0
                            
                    print("val = ",val)
                    if val == 0:
                        query = "insert into twowheeler(parking_id) values('{}')".format(SlotId)
                        cursorObject.execute(query)
                        connectionObject.commit()
                    else:
                        print("SLOT ID ALREADY EXISTS")
                        
                    
                        
                elif FunctionChoice == 5:
                    # remove slot
                    print("Removing Slot")
                    SlotId = input("Enter the SLOT ID to Remove: ") 
                    query = "select parking_id from twowheeler"
                    cursorObject.execute(query)
                        
                    for pId in cursorObject:
                        print(pId)
                        if pId[0] != SlotId:
                            val = 1
                            # break
                        else:
                            val = 0
                            
                    print("val = ",val)
                    if val == 0:
                        query = "delete from twowheeler where parking_id = '{}'".format(SlotId)
                        cursorObject.execute(query)
                        connectionObject.commit()
                    else:
                        print("SLOT ID DOES NOT EXISTS")
        else:
            print("Invalid Credentials")
    else:                                                                                                                     
        print("Invalid option")
    
    ans = input("Do you wan to continue:(y/n): ")
