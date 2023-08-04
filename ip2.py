import os
import platform
import mysql.connector as con
#import pandas as pd 

# Connecting python with mysql using mysql.connector

# Note: the user  can only use options from 1-5.
# If the user chooses an option other than 1-5 then an error may occur asking for correct choice.
# School Management is the main menue of this program.

def selection():
    db=con.connect(user='root',passwd='',host='localhost',database='ip')
    cu=db.cursor()
    print('-------------------------------------------------------------------WELCOME TO SCHOOL MANAGEMENT SYSTEM-------------------------------------------------------------------')
    print("1. STUDENT MANAGEMENT")
    print("2. EMPLOYEE MANAGEMENT")
    print("3. FEE MANAGEMENT")
    print("4. EXAM MANGEMENT")
    print("5. Exit")
  
# Functions are used to insert,update,delete,display the data of respective tables accordingly.


# Given below are the main functions of "Student" table:

# Functions in this option are denoted by "<function>1():".

def insert1():
    sname=input("Enter student Name:")
    admne=int(input("Enter Admission No:"))
    dob=input("Enter date of Birth(yyyy-mm-dd):")
    cls=input("Enter class for admission:")
    cty=input("Enter City:")
    print("\n")
    db=con.connect(user='root',passwd='',host='localhost',database='ip')
    cu=db.cursor()
    sql="insert into student(sname,admne,dob,cls,cty) values('%s','%d','%s','%s','%s')"%(sname,admne,dob,cls,cty)
    try:
        cu.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()


def display1():
    try:
        db=con.connect(user='root',passwd='',host='localhost',database='ip')
        cu=db.cursor()
        sql="select * from student"
        cu.execute(sql)
        result=cu.fetchall()
        for c in result:
            sname=c[0]
            admne=c[1]
            dob=c[2]
            cls=c[3]
            cty=c[4]
            print("Student Name Is:%s"%sname)
            print("Admission number:%d"%admne)
            print("Date of Birth:%s"%dob)
            print("Class:%s"%cls)
            print("City:%s"%cty)
            print("---------------------------------------------------------------------------")
            
           # break
    except:
        print("Error:Unable to fetch data")
        db.close()

def update1():
    try:
        db=con.connect(user="root",passwd="",host="localhost",database="ip")
        cu=db.cursor()
        sql="select* from  student"
        cu.execute(sql)
        result=cu.fetchall()

        for c in result:
            sname=c[0]
            admne=c[1]
            dob=c[2]
            cls=c[3]
            cty=c[4]
    except:
        print("Error:Unable to fetch data")
    print()
    tempst=int(input("Enter admission No.:"))
    temp=input("Enter new class:")
    try:
        sql="update student set cls=%s where admne=%d"%(temp,tempst)
        cu.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()

def delete1():
    try:
        db=con.connect(user='root',passwd='',host='localhost',database='ip')
        cu=db.cursor()
        sql="select * from student"
        cu.execute(sql)
        result=cu.fetchall()
        for c in result:
            sname=c[0]
            admne=c[1]
            dob=c[2]
            cls=c[3]
            cty=c[4]
    except:
        print("Error:Unable to fetch data")


    temp=int(input("\n Enter admission number to be deleted:"))
    try:
        sql="delete from student where admne='%d'"%(temp)
        ans=input("Are you sure you want to delete the recore(y/n):")
        if ans=='y' or ans=='Y':
            cu.execute(sql)
            db.commit()
    except Exception as e:
        print(e)
        db.close()

#Given below are the main functions of "emp" i.e employee table:
# Functions in this option are denoted by "<function>2():"

def insert2():
    empno=int(input("Enter employee number:"))
    ename=input("Enter employee name:")
    job=input("Enter Designation:")
    hiredate=input("Enter date of joining(yyyy-mm-dd):")
    db=con.connect(user='root',passwd='',host='localhost',database='ip')
    cu=db.cursor()
    sql="insert into emp(empno,ename,job,hiredate)values('%d','%s','%s','%s')"%(empno,ename,job,hiredate)
    try:
        cu.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def display2():
    try:
        db=con.connect(user='root',passwd='',host='localhost',database='ip')
        cu=db.cursor()
        sql="select * from emp"
        cu.execute(sql)
        result=cu.fetchall()
        for c in result:
            empno=c[0]
            ename=c[1]
            job=c[2]
            hiredate=c[3]
            print("Employee Number:%d"%empno)
            print("Employee Name:%s"%ename)
            print("Designation:%s"%job)
            print("Hire Date:%s"%hiredate)
            print("---------------------------------------------------------------------------")
            
    except:
        print("Error:Unable to fetch data")
        db.close()

def update2():
    try:
        db=con.connect(user="root",passwd="",host="localhost",database="ip")
        cu=db.cursor()
        sql="select * from emp"
        cu.execute(sql)
        result=cu.fetchall()
        for c in result:
            empno=c[0]
            ename=c[1]
            job=c[2]
            hiredate=c[3]
    except:
        print("Error:Unable to fetch data")
    print()

    tempst=int(input("Enter Employee No:"))
    temp=input("Enter new designation:")
    try:
        sql="update emp set job='%s' where empno=%d"%(temp,tempst)
        cu.execute(sql)
        db.commit()
    except Exception as e:
       print(e)
       db.close()

def delete2():
    try:
        db=con.connect(user='root',passwd='',host='localhost',database='ip')
        cu=db.cursor()
        sql="select * from emp"
        cu.execute(sql)
        result=cu.fetchall()
        for c in result:
            empno=c[0]
            ename=c[1]
            job=c[2]
            hiredate=c[3]
    except:
        print("Error:Unable to fetch data")

    temp=int(input("\n Enter employee number to be deleted:"))
    try:
        sql="delete from emp where empno='%d'"%(temp)
        ans=input("Are you sure you want to delete the record(y/n):")
        if ans=='y' or ans=='Y':
            cu.execute(sql)
            db.commit()
    except Exception as e:
       print(e)
       db.close( )


#Given below are the main functions of "fee"  table:

# Functions in this option are denoted by "<function>3():"

def insert3():
    admne=int(input("Enter admission number:"))
    fee=float(input("Enter fee amount:"))
    month=input("Enter Month:")
    db=con.connect(user='root',passwd='',host='localhost',database='ip')
    cu=db.cursor()
    sql="insert into fee(admne,fee,month)values('%d','%d','%s')"%(admne,fee,month)
    try:
        cu.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def display3():
    try:
        db=con.connect(user='root',passwd='',host='localhost',database='ip')
        cu=db.cursor()
        sql="select * from fee"
        cu.execute(sql)
        result=cu.fetchall()
        for c in result:
            admne=c[0]
            fee=c[1]
            month=c[2]
            print("Admission Number:%d"%admne)
            print("Fees:%s"%fee)
            print("Month:%s"%month)
            print("---------------------------------------------------------------------------")
            
    
    except:
        print("Error:Unable to fetch data")
        db.close()

def update3():
    try:
        db=con.connect(user="root",passwd="",host="localhost",database="ip")
        cu=db.cursor()
        sql="select * from fee"
        cu.execute(sql)
        result=cu.fetchall()
        for c in result:
            admne=c[0]
            fee=c[1]
            month=c[2]
    except:
        print("Error:Unable to fetch data")
    print()

    tempst=int(input("Enter Admission No:"))
    temp=int(input("Enter Fee Paid:"))
    try:
        sql="update fee set fee=%d where admne=%d"%(temp,tempst)
        cu.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()

def delete3():
    try:
        db=con.connect(user='root',passwd='',host='localhost',database='ip')
        cu=db.cursor()
        sql="select * from fee"
        cu.execute(sql)
        result=cu.fetchall()
        for c in result:
            admne=c[0]
            fee=c[1]
            month=c[2]
    except:
        print("Error:Unable to fetch data")

    temp=int(input("\n Enter admission number to be deleted:"))
    try:
        sql="delete from fee where admne='%d'"%(temp)
        ans=input("Are you sure you want to delete the record(y/n):")
        if ans=='y' or ans=='Y':
            cu.execute(sql)
            db.commit()
    except Exception as e:
        print(e)
        db.close()


#Given below are the main functions of "exam" table:

# Functions in this option are denoted by "<function>3():"


def insert4():
    sname=input("Enter Student Name:")
    admne=int(input("Enter Admission No:"))
    per=float(input("Enter Percentage:"))
    res=input("Enter result(Pass/Fail):")
    db=con.connect(user='root',passwd='',host='localhost',database='ip')
    cu=db.cursor()
    sql="insert into exam(sname,admne,per,res)values('%s','%d','%d','%s')"%(sname,admne,per,res)
    try:
        cu.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def display4():
    try:
        db=con.connect(user='root',passwd='',host='localhost',database='ip')
        cu=db.cursor()
        sql="select * from exam"
        cu.execute(sql)
        result=cu.fetchall()
        for c in result:
            sname=c[0]
            admne=c[1]
            per=c[2]
            res=c[3]
            print("Student Name:%s"%sname)
            print("Admission Number:%d"%admne)
            print("Percentage:%s"%per)
            print("Result:%s"%res)
            print("---------------------------------------------------------------------------")
            
    except:
        print("Error:Unable to fetch data")
        db.close()

def update4():
    try:
        db=con.connect(user='root',passwd='',host='localhost',database='ip')
        cu=db.cursor()
        sql="select * from exam"
        cu.execute(sql)
        result=cu.fetchall()

        for c in result:
            sname=c[0]
            admne=c[1]
            per=c[2]
            res=c[3]
    except:
        print("Error:Unable to fetch data")
    print()

    tempst=int(input("Enter Admission No:"))
    temp=float(input("Enter New Percentage:"))
    try:
        sql="Update exam set per='%d' where admne='%d'"%(temp,tempst)
        cu.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()

def delete4():
    try:
        db=con.connect(user='root',passwd='',host='localhost',database='ip')
        cu=db.cursor()
        sql="select * from exam"
        cu.execute(sql)
        result=cu.fetchall()
        for c in result:
            sname=c[0]
            admne=c[1]
            per=c[2]
            res=c[3]
    except:
        print("Error:Unable to fetch data")

    temp=int(input("\n Enter admission number to be deleted:"))
    try:
        sql="delete from exam where admne=%d"%(temp)
        ans=input("Are you sure you want to delete the record(y/n):")
        if ans=='y' or ans=='Y':
            cu.execute(sql)
            db.commit()
    except Exception as e:
        print(e)
        db.close()
#__main__
#selection()

# From here the main loops of the program begins where the user have to choose options from the main menue and choose respective sub-options accordingliy.
while True:
    selection()
    ch=int(input("\n Enter your choice(1-5):"))
    if ch==1:
        while True:

            # Give below is the main menue of   Student Management System.
            
            print("------------------------------------------------------------------- WELCOME TO STUDENT MANGEMENT SYSTEM-------------------------------------------------------------------")
            print("a. NEW ADMISSION")
            print("b. UPDATE STUDENT DETAILS")
            print("c. ISSUE TC")
            print("d. DISPLAY ALL THE DATA")
            print("e. EXIT")
            #while True:
            c=input("Enter your choice(a-e):")
            if c=="a":
                insert1()
                print("\n")
                print("----Modified details are:----")
                print("\n")
                display1()
            elif c=="b":
                update1()
                print("\n")
                print("----Modified details are:---- ")
                print("\n")
                display1()
            elif c=="c":
                delete1()
                print("\n")
                print("----Modified details are:---- ")
                print("\n")
                display1()
            elif c=="d":
                print("\n")
                print("----Modified details are:----")
                print("\n")
                display1()
            elif c=="e":
                break
            else:
                print("Enter correct choice.....!!")

    elif ch==2:
        while True:

            # Give below is the main menue of   Employee  Management System.
            
            print("-------------------------------------------------------------------WELCOME TO EMPLOYEE MANAGEMENT SYSTEM------------------------------------------------------------------- ")
            print("a. NEW EMPLOYEE")
            print("b. UPDATE STAFF DETAILS")
            print("c. DELETE EMPLOYEE")
            print("d. DISPLAY ALL THE DATA")
            print("e. EXIT")
            c=input("Enter your choice:-(a-e)")
            if c=="a":
                insert2()
                print("\n")
                print("----Modified details are:----")
                print("\n")
                display2()
            elif c=="b":
                update2()
                print("\n")
                print("----Modified details are:---- ")
                print("\n")
                display2()
            elif c=="c":
                delete2()
                print("\n")
                print("----Modified details are:----")
                print("\n")
                display2()
            elif c=="d":
                print("\n")
                print("----Modified details are:----")
                display2()
            elif c=="e":
                break
            else:
                print("Enter your correct choice...!!")

    elif ch==3:
        while True:
            # Give below is the main menue of   Fee Management System.
            
            print("-------------------------------------------------------------------WELCOME TO FEE MANAGEMENT------------------------------------------------------------------- ")
            print("a. NEW FEE")
            print("b. UPDATE FEE")
            print("c. EXEMPT FEE")
            print("d. DISPLAY ALL THE DATA")
            print("e. EXIT")
            c=input("Enter your choice:-(a-e)")
            if c=="a":
                insert3()
                print("\n")
                print("----Modified details are:----")
                print("\n")
                display3()
            elif c=="b":
                update3()
                print("\n")
                print("----Modified details are:----")
                print("\n")
                display3()
            elif c=="c":
                delete3()
                print("\n")
                print("----Modified details are:----")
                print("\n")
                display3()
            elif c=="d":
                print("\n")
                print("----Modified details are:----")
                print("\n")
                display3()
            elif c=="e":
                break
            else:
                print("Enter correct choice...!!")

    elif ch==4:
        while True:
            # Give below is the main menue of   Exam Management System.
            
            print("-------------------------------------------------------------------WELCOME TO EXAM MANAGEMENT SYSTEM-------------------------------------------------------------------")
            print("a. EXAM DETAILS")
            print("b. UPDATE DETAILS")
            print("c. DELETE DETAILS")
            print("d. DISPLAY ALL THE DATA")
            print("e. EXIT")
            c=input("Enter your choice:(a-e):")
            if c=="a":
                insert4()
                print("\n")
                print("----Modified details are:----")
                print("\n")
                display4()
            elif c=="b":
                update4()
                print("\n")
                print("----Modified details are:----")
                print("\n")
                display4()
            elif c=="c":
                delete4()
                print("\n")
                print("----Modified details are:----")
                print("\n")
                display4()
            elif c=="d":
                print("\n")
                print("----Modified details are:----")
                print("\n")
                display4()
            elif c=="e":
                break
            else:
                print("Enter correct choice...!!")
    elif ch==5:
        break
    # The above option is used to kill/stop main program run.
    else:
        print("Enter correct choice...!!")
    

            




