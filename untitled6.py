                     ##Project on Diwali Sales

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

diwali=pd.read_csv("C:/Users/Vivek/Downloads/Diwali Sales.csv")
diwali

                     
                   ## Data Cleaning
                      
diwali.head()
diwali.info()
diwali.shape
diwali.drop(["Status","unnamed1"],axis=1,inplace=True)
diwali.isnull().sum()
diwali.dropna(inplace=True)
diwali.isnull().sum()
diwali.rename(columns={"Zone":"Region"},inplace=True)
diwali.describe()
diwali[["Amount","Age"]].describe()
diwali.rename(columns={"Cust_name":"Customer_Name"},inplace=True)
diwali["Gender"].replace("F","Female",inplace=True)
diwali["Gender"].replace("M","Male",inplace=True)
diwali.head()
diwali["Gender"]




                      ##Expolatry Data Analysis
   
sns.countplot(x="Gender",data=diwali)
plt.show()
diwali.sort_values(by="Amount",ascending=False)
diwali_spend=diwali.loc[0: ,("Gender","Amount")]  
diwali_spend                 
sales_gender=diwali_spend.groupby(["Gender"],as_index=False)["Amount"].sum().sort_values(by="Amount",ascending=False)
print(sales_gender)
sns.barplot(x="Gender",y="Amount",data=sales_gender)
plt.show()

# From above graphs we can see that most of the buyers are females and even purchasing power of the female is better then males.

age=sns.countplot(x="Age Group",data=diwali,hue="Gender")
age
for bars in age.containers:
    age.bar_label(bars)
    
By_age=diwali.groupby(["Age Group","Gender"],as_index=False)["Amount"].sum().sort_values(by=["Age Group"])
By_age
figure=plt.figure(figsize=(11,5))
age_spend=sns.barplot(x="Age Group",y="Amount",data=By_age,hue="Gender")
age_spend
for bars in age_spend.containers:
    age_spend.bar_label(bars)
    
# From above graphs we can see that most of the buyers are of age_group between (26-35) and in which mostly females are there.
    
state=diwali.groupby(["State","Region"],as_index=False)["Amount"].sum().sort_values(by="Amount")
state
x=state.sort_values(by=["Amount"],ascending=False)[0:5]
x
figure=plt.figure(figsize=(10,5))
sns.barplot(x="State",y="Amount",data=x)
plt.title("State-wise Sales")
plt.show()

state=diwali.groupby(["State","Region"],as_index=False)["Orders"].sum().sort_values(by="Orders")
state
x=state.sort_values(by=["Orders"],ascending=False)[0:5]
x
figure=plt.figure(figsize=(10,5))
sns.barplot(x="State",y="Orders",data=x)
plt.title("State-wise Orders")
plt.show()

order=diwali.groupby(["Region"],as_index=False)["Orders"].count().sort_values(by="Orders",ascending=False)[0:5]
order
plt.pie(order["Orders"],labels=order["Region"],autopct='%0.1f%%')
plt.title("Region-wise Sales")
plt.show()  

# From the above graph it shows that the maximum sales revenue is genrated from Uttar Pradesh.
# And the another graph shows that higest no of orders are perform from Uttar Pradesh. 
# And the pie chart shows that maximum sales is done from  Central Region.

x=diwali.groupby(["Occupation"],as_index=False)["Amount"].sum().sort_values(by="Amount",ascending=False)
x
plt.barh(x["Occupation"],x["Amount"])
plt.show()

# From the graph it shows that most of the buyers are below to "IT Sector" and "Healthcare"

category=diwali.groupby(["Product_Category"],as_index=False)["Orders"].count().sort_values(by="Orders",ascending=False)
x=category.head()
x
plt.pie(x["Orders"],labels=x["Product_Category"],autopct='%0.1f%%')
plt.show()

# So the above pie chart shows that coustmers mostly spend money on buying "Clothing & Apparel" items then "Food" items.  














        

