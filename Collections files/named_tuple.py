from collections import namedtuple
# Student = namedtuple('same name',[list of attributes(names of attributes)]) 
Student = namedtuple('Student',['name','rollno','branch'])
# //create instances 
s1=Student('Mohit',1,'IT')
s2=Student('Ravi',2,'IT')
s3=Student('Utkarsh',3,'Marine Eng')
s4=Student('Anubhav',2,'Mech')
print(s1)
# //accessing by name
print('Name, rollno , branch are as follows', s1.name,s1.rollno,s1.branch)
# accessing by index
print('Name, rollno , branch are as follows', s1[0],s1[1],s1[2])


S = Student('Nandini','19','2541997') 
# using _asdict() to return an OrderedDict() 
print ("The OrderedDict instance using namedtuple is ._asdict() : ") 
print (S._asdict()) 
  
# initializing iterable  
li = ['Manjeet', '19', '411997' ] 
# using _make() to return namedtuple() 
print ("The namedtuple instance using iterable is  ._make(iterable): ") 
print (Student._make(li))   

# initializing dict 
di = { 'name' : "ABHISHEK", 'rollno' : 19 , 'branch' : 'civil' }
# using ** operator to return namedtuple from dictionary 
print ("The namedtuple instance from dict is Student(**di) : ") 
print (Student(**di)) 
  
