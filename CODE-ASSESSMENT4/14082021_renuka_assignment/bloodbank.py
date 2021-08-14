import pymongo
import re
import logging,smtplib
client=pymongo.MongoClient("mongodb://localhost:27017/bloodbankdb")
mydatabase=client["bloodbankdb"]
collection_name=mydatabase["bloodbanks"]
banklist=[]
try:
    def validate(name,address,pincode,mobilenum,bloodgroup,place):
        valname=re.search("^[A-Za-z]{0,25}$",name)
        valaddress=re.search("^[A-Za-z]{0,25}",address)
        valpincode=re.search("^[4-9][0-9]{6}$",pincode)
        valmobilenum=re.search("^[7-9][0-9]{10}",mobilenum)
        valbloodgrp=re.search("^[A|B|AB|O][\+|\-]$",bloodgroup)
        valplace=re.search("^[A-Za-z]{0,25}$",place)
    class bloodbank:
        def addDonors(self,name,address,bloodgroup,pincode,mobilenum,last_donated_date,place):
            custdict={"name":name,"address":address,"bloodgroup":bloodgroup,"pincode":pincode,"mobilenum":mobilenum,"last_donated_date":last_donated_date,"place":place}
            banklist.append(custdict)
    obj=bloodbank()
    while(True):
        print("1.Add Donors")
        print("2.Search donors based on blood group")
        print("3.Search donors based on blood group AND place")
        print("4.Update all the donor details with their mobile number")
        print("5.Delete the donor based on mobile number")
        print("6.Display the total donars on each blood group")
        print("7.View all Donors")
        print("8.Immediate notification to all via mail")
        print("9.Exit")
        choice=int(input("Enter your choice"))
        if choice==1:
            name=input("Enter your name")
            address=input("Enter your address")
            bloodgroup=input("Enter your bloodgroup")
            pincode=input("Enter your pincode")
            mobilenum=input("Enter your mobile number")
            last_donated_date=input("Enter the last donated date")
            place=input("Enter your place")
            x=validate(name,address,bloodgroup,pincode,mobilenum,place)
            if x:
                obj.addDonors(name,address,bloodgroup,pincode,mobilenum,last_donated_date,place)
                result=collection_name.insert_many(banklist)
                print(result.inserted_ids)
            else:
                logging.error("Enter valid details")
        if choice==2:
            bloodgrp=input("enter the blood group")
            result=collection_name.find({"bloodgroup":bloodgrp})
            for i in result:
                print(i)
        if choice==3:
            bloodgrp=input("Enter the blood group")
            place=input("Enter the place")
            result=collection_name.find({"$and":[{"bloodgroup":bloodgrp},{"place":place}]})
            for i in result:
                print(i)
        if choice==4:
            mobilenum=input("Enter the mobile number")
            name=input("enter the name to be updated")
            bloodgroup=input("enter the bloodgroup to be updated")
            place=input("enter the place to be updated")
            address=input("enter the address to be updated")
            pincode=input("enter the pincode to be updated")
            last_donated_date=input("enter the last date to be updated")
            result=collection_name.update_many({"mobilenum":mobilenum},{"$set":{"name":name,"bloodgroup":bloodgroup,"place":place,"address":address,"pincode":pincode,"last_donated_date":last_donated_date}})
            print("data updated")
        if choice==5:
            mobilenum=input("enter the mobile number")
            result=collection_name.delete_one({"mobilenum":mobilenum})
            print(result.deleted_count)
        if choice==6:
            result=collection_name.aggregate([{"$group":{"_id":"$bloodgroup","no_of_donors":{"$sum":1}}}])
            for i in result:
                print(i)
        if choice==7:
            result=collection_name.find()
            for i in result:
                banklist.append(i)
                print(i)
        if choice==8:
            break
except:
    logging.error("ENTER VALID DETAILS")
        





