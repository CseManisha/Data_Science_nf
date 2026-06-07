#data visulization matplotlib

from matplotlib import color_sequences
# definig data set
plt.style.use("seaborn-v0_8")
age=[19,20,30,40,50]
salrary=[15000,25000,19000,22000,15000]

# adjust figure size
plt.figure(figsize=(10,5))
#plot line charts
plt.plot(age,salrary,marker='s',color="blue",linestyle='--',linewidth=2,markerfacecolor="pink",markeredgecolor="red")

#add labels and title

plt.xlabel("Age",color="blue")
plt.ylabel("salrary",color="blue")
plt.title("age vs salrary",color="blue")

#add grid
plt.grid(True,color="skyblue",linestyle=':')
#show plot
plt.show()


# definig dataset witj dictonary
import pandas as pd
marks={
    "marks":[20,30,50,50,80]

}
var=pd.DataFrame(marks)
#  adjust figure size
plt.figure(figsize=(10,5))
#plot line charts
plt.plot(var["marks"],marker="s",color="blue",linestyle="--",linewidth=2)
# using labels
plt.xlabel("index")
plt.ylabel("marks")
plt.title("marks vs index")
#add grid
plt.grid(True,color="skyblue",linestyle=":")
#show plot
plt.show()

# histogram
#define dataset
marks=[23,46,57,89,30,45,55,48]
#plot
plt.hist(marks,bins=8,edgecolor="black",color="skyblue",alpha=0.5)
#labels
plt.title("marks distribution")
plt.xlabel("marks")
plt.ylabel("frequency")

#grid
plt.grid(axis="y",linestyle=":",color="blue")
#show plot
plt.show()

# bar chart
# adjust figue size
plt.figure(figsize=(10,5))

from matplotlib.lines import lineStyles
# single bar chart
subject=['phy','hindi',"chem",'maths','eng']
Score=[88,45,66,76,86]

# plot bar
plt.bar(subject,Score,color=['blue','green','skyblue'])

#labels
plt.xlabel("subject")
plt.ylabel("score")
plt.title("Marks")

# grid

plt.grid(axis='y',linestyle=":",color="blue")

for index, value in enumerate(Score):
  plt.text(index,value+1,str(value),ha="center")

#show plot
plt.show()  


#pie chart
#define dataset

Quarters=['q1','q2',"q3",'q5']
profit=[40000,50000,60000,70000]
rang=['red','blue','pink','green']

#plot
plt.pie(profit,labels=Quarters,autopct="%1.0f%%",startangle=90,explode=[0.1,0.2,0.2,0.2],shadow=True)

#labels
plt.legend(Quarters,title=profit)
plt.title("profit")
#used to align circle shape
plt.axis("equal")


#show plot
plt.show()

#Scatter plot 
from numpy import size
#scatter plot
hrs=[2,3,4,5,7]
income=[7000,6000,8000,9000,10000]
size=[100,300,500,700,1000]
colors=['red','blue','pink','green','yellow']

#plot
plt.scatter(hrs,income,s=size,c=colors)
#labels
plt.xlabel("hours")
plt.ylabel("income")
plt.title("hours vs income")
# display
plt.show()

# categorical data

import matplotlib.pyplot as plt
plt.style.use("ggplot")
x1=[1,2,3,4]
y1=[3,5,6,9]
x2=[3,6,7,10]
y2=[2,3,5,8]

plt.scatter(x1,y1,label="group a")
plt.scatter(x2,y2,label="group b")
plt.legend()
plt.show()

