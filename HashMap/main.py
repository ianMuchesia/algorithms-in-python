my_dict = {"ian":"001", "msodoki":"002","joe":"003"}
print(my_dict)
print(type(my_dict))


new_dict = dict()
print(new_dict)


new_dict = dict(Ian="001", Msodoki="002")
print(new_dict)


emp_details = {"Employee":{"ian":{"id":"001", "designation":"Team lead"},"hilla":{"id":"002", "designation":"frontend"}}}


print(emp_details)


#perfoming operations in hashtables
#accessing items 
print(my_dict["ian"])

print(my_dict.keys())

print(my_dict.values())

print(my_dict.get('ian'))

trial = my_dict.get('ian')
if my_dict.get('in'):
    print(trial, "hssssssss")
else:
    print("nooooooooo")
for x in my_dict:
    print(x)
    
for x in my_dict.values():
    print(x)
    
    
for x, y in my_dict.items():
    print(x,y)
    
    
    
#updating values
my_dict['ian']="004"
my_dict['chris']="003"
print(my_dict)


#deleting items from a dictionary
#my_dict.pop('chris')
my_dict.popitem()
print(my_dict)

del my_dict['joe']
print(my_dict)



#converting a dictionary to a data frame
# import pandas as pd