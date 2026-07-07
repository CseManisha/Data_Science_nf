#advanceed visualization with seaborn
# box plot ,heat map, vilon plot, pair plot, kde plots

#kde --> kernal density  estimation 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("penguins.csv").head(50)
print(df.shape)
print(df.columns)
corr=df.corr(numeric_only=True)

# hera are types of plots

# sns.displot(df['body_mass_g'])

# sns.scatterplot(data=df, x="bill_length_mm",y="bill_depth_mm",hue="species")

# sns.barplot(data=df, x="bill_length_mm",y="bill_depth_mm",hue="species",color="pink")

# sns.countplot(data=df, x="bill_length_mm")

# sns.histplot(data=df,x="bill_length_mm" ,y="bill_depth_mm",hue="species")

# sns.boxplot(data=df,x="bill_length_mm",y="bill_depth_mm",color="red")

# sns.violinplot(data=df, x="bill_length_mm",y="bill_depth_mm",color="pink")

# sns.pairplot(data=df,vars=["bill_length_mm","bill_depth_mm"],hue="species")

sns.heatmap(corr, annot=True, cmap="plasma")

plt.title("penguin bill length vs bill depth")
plt.show()

