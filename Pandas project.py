import pandas as pd 
import numpy as np
import matplotlib.pyplot as plot
sam=pd.DataFrame() 
print("Name of Excel File ")
p=input()
a=pd.read_excel(p,index_col=0) 
print(a) 
x=input("column name : ")  
y=input("which statistical value you want to know : ") 
if (y=="count") and (x=="SALARY"):
 b=a.SALARY.count() 

elif y=="mean" and x=="SALARY": 
 b=a.SALARY.mean() 

elif y=="std" and x=="SALARY":
    b=a.SALARY.std() 


 b=a.SALARY.min() 

elif y=="correation" and x=="SALARY":  
    o=input("Row_name : ") 
    p=input("Column_name : ") 
    b=a[o].corr(a[p]) 
elif y=="percentage" and x=="SALARY": 
	print("Enter the percentage?")
	q=int(input())
	z=float(q/100)
	#print(z)
	b=a.SALARY.quantile(z)

elif y=="Standard Deviation" and x=="SALARY": 
	b=a.std()

elif y=="max" and x=="SALARY": 
 b=a.SALARY.max() 
 
elif y=="count" and x=="BONUS": 
 b=a.BONUS.count() 
 
elif y=="mean" and x=="BONUS": 
 b=a.BONUS.mean() 
 
elif y=="std" and x=="BONUS": 
 b=a.BONUS.std() 
 
elif y=="min" and x=="BONUS": 
 b=a.BONUS.min() 
 
elif y=="correation" and x=="BONUS":
    o=input("Row_name : ")  
    p=input("Column_name : ") 
    b=a[o].corr(b[p]) 
 
elif y=="percentage" and x=="BONUS": 
	print("Enter the percentage?")
	q=int(input())
	z=float(q/100)
	#print(z)
	b=a.SALARY.quantile(z) 

elif y=="Standard Deviation" and x=="BONUS": 
	b=a.std()

elif y=="max" and x=="BONUS":
 b=a.BONUS.max() 
 
#c=a.BONUS.mean() 
#print(c) 
print(y," of salary",b) 
print("which chart you want to see : ") 
m=input() 
if m=="bar": 
    o=input("which value you want to add in X-axis : ") 
    p=input("which value you want to add in Y-axis : ")
     
    #print(a.plot.bar(x=o,y=p,rot=0)) 
    a.plot.bar(x=o, y=p, rot=70, title="Bar Diagram");

    print(plot.show(block=True))
 
elif m=="scatter": 
    o=input("which value you want to add in X-axis") 
    p=input("which value you want to add in Y-axis") 

    a.plot.scatter(x = o, y = p,s=100, title="scatter Diagram");
    print(plot.show(block=True)) 
 
elif m=="pie": 
    x=input("which column you want to add") 
    o=int(input("Width?")) 
    p=int(input("Height?"))
    a.plot(kind='pie',y=x, figsize=(o, p), title="Pie Diagram");
    print(plot.show(block=True))
