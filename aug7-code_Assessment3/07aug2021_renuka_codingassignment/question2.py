import json,smtplib,re,logging
studentlist=[]
class Student:
    def addStudent(self,name,rollno,admino,college,parentname,mobilenumber,emailid):
        self.name=name
        self.rollno=rollno
        self.admino=admino
        self.college=college
        self.parentname=parentname
        self.mobilenumber=mobilenumber
        self.emailid=emailid
        list1=[self.name,self.rollno,self.admino,self.college,self.parentname,self.mobilenumber,self.emailid]
        return list1
class Sem1Result(Student):
    def addStudentResult(self,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
        self.sub1mark=sub1mark
        self.sub2mark=sub2mark
        self.sub3mark=sub3mark
        self.sub4mark=sub4mark
        self.sub5mark=sub5mark
        list2=[self.sub1mark,self.sub2mark,self.sub3mark,self.sub4mark,self.sub5mark]
        return list2
d=Sem1Result()
def validate(name,rollno,mobilenumber,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
        name1=re.search("[A-Za-z]{0,25}$",name)
        print(name1)
        rollno1=re.search("[0-9]{0,7}$",rollno)
        print(rollno1)
        mobilenumber1=re.search("[6-9]\d{9}$",mobilenumber)
        print(mobilenumber1)
        emailid1=re.search("[A-Za-z0-9]{0,20}@[a-z]+\.[a-z]{2,4}$",emailid)
        print(emailid1)
        sub1mark1=re.search("[0-3]{1}[0-9]{1}|40$",sub1mark)
        print(sub1mark1)
        sub2mark1=re.search("[0-3]{1}[0-9]{1}|40$",sub2mark)
        sub3mark1=re.search("[0-3]{1}[0-9]{1}|40$",sub3mark)
        sub4mark1=re.search("[0-3]{1}[0-9]{1}|40$",sub4mark)
        sub5mark1=re.search("[0-3]{1}[0-9]{1}|40$",sub5mark)
        if name1 and rollno1 and mobilenumber1 and emailid1 and sub1mark1 and sub2mark1 and sub3mark1 and sub4mark1 and sub5mark1 :
            return True
        else:
            return False
try:
    if __name__ == "__main__":
        while(True):
            print("1.Add Student with Mark")
            print("2.View all student details with marks using JSON File")
            print("3.View all student details based on Ranking using JSON File")
            print("4.Send an email to all parents less than 50% mark")
            print("5.Exit")
            option=int(input("Enter your option :"))
            if option==1:
                name = input("Enter the name of student: ")
                rollno=input("Ënter the RollNo of student:")
                admno=input("Enter the admno of Student:")
                college=input("Enter the college of student:")
                parentname=input("Enter the parent name:")
                mobilenumber=input("Enter the mobilenumber:")
                emailid=input("Enter the email:")
                sub1mark=input("Enter the sub1 mark:")
                sub2mark=input("Enter the sub2 mark:")
                sub3mark=input("Enter the sub3 mark:")
                sub4mark=input("Enter the sub4 mark:")
                sub5mark=input("Enter the sub5 mark:")
                total=int(sub1mark)+ int(sub2mark)+int(sub3mark)+int(sub4mark)+int(sub5mark)
                if validate(name,rollno,mobilenumber,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
                    a=d.addStudent(name,rollno,admno,college,parentname,mobilenumber,emailid)
                    dict1={'totalmarks':total}
                    b=d.addStudentResult(sub1mark,sub2mark,sub3mark,sub4mark,sub5mark)
                    student=["name","rollno","admino","college","parentname","mobilenumber","emailid"]
                    marks=["sub1","sub2","sub3","sub4","sub5"]
                    for i in range(len(a)):
                        dict1[student[i]]=a[i]
                    for j in range(len(b)):
                        dict1[marks[j]]=b[j]
                    studentlist.append(dict1)
                    print(studentlist)
                else:
                    logging.error("wrong")
            
            
            
            if option==2:
                jsondata=json.dumps(studentlist)
                with open("newjson.json","w+",encoding="utf-8") as fi:
                    fi.write(jsondata)

            if option==3:
                data=(sorted(studentlist,key=lambda i:i["totalmarks"],reverse=True))
                print(data)
                jsondata=json.dumps(data)
                with open("newjson1.json","w+",encoding="utf-8") as fi:
                    fi.write(jsondata)

            if option==4:
                for i in studentlist:
                    if i['totalmarks']<100:
                        message=str(i)
                        print(message)
                        connection=smtplib.SMTP("smtp.gmail.com",587)
                        connection.starttls()
                        connection.login("chavala.sridhar476@gmail.com","Sridhar123@")
                        connection.sendmail("chavala.sridhar476@gmail.com","chavala.renuka@gmail.com",message)
                        connection.quit
                        print("Mail sent")

            if option==5:
                break
except:
    logging.error("something went wrong")
    print("error")