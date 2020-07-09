#BLL                                                                                                                                                  
                                                                                                                                                      
idlist=[]                                                                                                                                             
namelist=[]                                                                                                                                           
agelist=[]                                                                                                                                            
numberlist=[]                                                                                                                                         
                                                                                                                                                      
                                                                                                                                                      
def addCustomer(id,name,age,number):                                                                                                                  
    idlist.append(id)                                                                                                                                 
    namelist.append(name)                                                                                                                             
    agelist.append(age)                                                                                                                               
    numberlist.append(number)                                                                                                                         
def searchCustomer(id):                                                                                                                               
    i=idlist.index(id)                                                                                                                                
    return i                                                                                                                                          
def deleteCustomer(id):                                                                                                                               
    a=idlist.index(id)                                                                                                                                
    idlist.pop(a)                                                                                                                                     
    namelist.pop(a)                                                                                                                                   
    agelist.pop(a)                                                                                                                                    
    numberlist.pop(a)                                                                                                                                 
def modifyCustomer(id,name,age,mob):                                                                                                                  
    i=idlist.index(id)                                                                                                                                
    namelist[i]=name                                                                                                                                  
    agelist[i]=age                                                                                                                                    
    numberlist[i]=mob#PL                                                                                                                              
                                                                                                                                                      
def showCustomer(i):                                                                                                                                  
    print(f"customer id: {idlist[i]},customer name: {namelist[i]}, customer age: {agelist[i]},customer number: {numberlist[i]}")                      
                                                                                                                                                      
print("welcome to my Customer Management System!")                                                                                                    
                                                                                                                                                      
while(1):                                                                                                                                             
    print("enter a choice below:")                                                                                                                    
    print("1 for add","2 for search","3 for delete","4 for show","5 for modify","6 for exit",sep="\n")                                                
    choice=input()                                                                                                                                    
    if(choice=="1"):                                                                                                                                  
        id = input("enter your id")                                                                                                                   
        name = input("enter your name")                                                                                                               
        age = input("enter your age")                                                                                                                 
        number = input("enter your  mobile number")                                                                                                   
        addCustomer(id,name,age,number)                                                                                                               
        print("customer added successfully!")                                                                                                         
    elif(choice=="2"):                                                                                                                                
        id=input("enter id")                                                                                                                          
        i=searchCustomer(id)                                                                                                                          
        showCustomer(i)                                                                                                                               
    elif(choice=="3"):                                                                                                                                
        id=input("enter id")                                                                                                                          
        deleteCustomer(id)                                                                                                                            
        print("deleted successfully!")                                                                                                                
    elif(choice=="4"):                                                                                                                                
        for i in range(len(idlist)):                                                                                                                  
            showCustomer(i)                                                                                                                           
                                                                                                                                                      
    elif(choice=="5"):                                                                                                                                
            id=input("Enter Cust Id to modify:")                                                                                                      
            name=input("Enter Cust updated Name:")                                                                                                    
            age = input("Enter Cust updated Age:")                                                                                                    
            mob = input("Enter Cust updated Mob:")                                                                                                    
            modifyCustomer(id,name,age,mob)                                                                                                           
            print("Customer Modified Successfully")                                                                                                   
    elif(choice=="6"):                                                                                                                                
        print("thanks for using my CMS")                                                                                                              
        exit(0)                                                                                                                                       
                                                                                                                                                      
                                                                                                                                                      
