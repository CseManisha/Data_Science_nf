#data visualization matplotlib
import matplotlib.pyplot as plt
import pandas as pd
# line plot
'''import matplotlib.pyplot as plt
import pandas as pd
print("hi")
a=[1,2,3,4,5]
b=["a","b","c","d","e"]
plt.plot(a,b)
plt.show()'''

#bar plot 

# x=[1,2,3,4,5]
# y=[55,94,68,80,100]
# plt.title("students marks")
# plt.xlabel("students")
# plt.ylabel("marks")
# plt.plot(x,y,c="green")
# plt.plot(x,y,linestyle="--",linewidth=5,marker="o",markersize=10,markerfacecolor="blue",markeredgecolor="black")
# plt.grid()
# plt.legend()
# plt.plot(x,y)
# plt.show()

#scatter plot

'''x=[1,2,3,4,5]
y=[55,94,68,80,100]
plt.title("students marks")
plt.xlabel("students")
plt.ylabel("marks")

plt.scatter(x,y,color="blue",label="marks")

plt.grid(True)
plt.legend()

plt.show()
'''

#histogram

marks = [55,60,65,70,75,80,85,90,95]

'''plt.title("Students Marks Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.hist(
    marks,
    bins=5,
    color="orange",
    edgecolor="black"
)

plt.grid(True)

plt.show()'''


# pie chart


language = ["Python", "Java", "C++"]
student = [40, 30, 30]

plt.title("Programming Language Preference")

plt.pie(
    student,
    labels=language,
    autopct="%1.1f%%",
    colors=["skyblue", "orange", "lightgreen"],
    explode=[0.1, 0, 0],
    shadow=True,
    startangle=90,
    wedgeprops={"edgecolor": "black"}
)

plt.show()



