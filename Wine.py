import pandas as pd #for reading dataset
import numpy as np # array handling functions

dataset = pd.read_csv("FINAL_USO.csv")#reading dataset
#print(dataset) # printing dataset

x = dataset.iloc[:,:-1].values #locating inputs
y = dataset.iloc[:,-1].values #locating outputs

#printing X and Y
print("x=",x)
print("y=",y)

from sklearn.model_selection import train_test_split # for splitting dataset
x_train,x_test,y_train,y_test = train_test_split(x ,y, test_size = 0.25 ,random_state = 0)
#printing the spliited dataset
print("x_train=",x_train)
print("x_test=",x_test)
print("y_train=",y_train)
print("y_test=",y_test)
#importing algorithm
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5, metric = 'euclidean' , p = 2)
print(knn.fit(x_train, y_train))#trainig Algorithm #Y=B1X1+B2X2+B3X3....BNXN
y_pred=knn.predict(x_test) #testing model
print("y_pred",y_pred) # predicted output

print("Testing Accuracy")
from sklearn import metrics
a1=float(input("ENTER THE FIXED ACIDITY VALUE= "))
b1=float(input("ENTER THE RESIDUAL SUGAR VALUE= "))
c1=float(input("ENTER THE DENSITY VALUE= "))
d1=float(input("ENTER THE PH VALUE= "))
e1=float(input("ENTER THE ALCOHOL VALUE= "))
a= knn.predict([[a1,b1,c1,d1,e1]])
print('Predicted new output value: %s' % (a))
if a == 6:
     print("wine quality")
else:
     print ("No quality")


            
