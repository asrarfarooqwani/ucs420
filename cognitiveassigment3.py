#Assignment 3

import pandas as pd

data={
    "Tid":[1,2,3,4,5,6,7,8,9,10],
    "Refund":["yes","no","no","yes","no","no","yes","no","no","no"],
    "Martial Status":["single","married","single","married","divorced","married","divorced","single","married","single"],
    "Taxable Income":["125k","100k","70k","120k","95k","60k","220k","85k","75k","90k"],
    "Cheat":["no","no","no","no","yes","no","no","yes","no","yes"]
}
df=pd.DataFrame(data)

print(df.iloc[[0,4,7,8]])
 

print(df.iloc[3:8])
print(df.iloc[4:9,2:5])
print(df.iloc[:,1:4])
df=pd.read_csv("Iris.csv")
print(df.head())

df.drop(4,axis=0,inplace=True)
df.drop(df.columns[3],axis=1,inplace=True)
print(df)
data=pd.DataFrame({
    "Employee id":[101,102,103,104,105],
    "Name":["Alice","Bob","Charlie","Diana","Edward"],
    "Department":["HR","IT","IT","Marketing","Sales"],
    "Age":[29,34,41,28,38],
    "Salary":[50000,70000,65000,55000,60000],
    "Years_Of_Experience":[4,8,10,3,12],
    "Joining_Date":["2020-03-15","2017-07-19","2013-06-01","2021-02-10","2010-11-25"],
    "Gender":["Female","Male","Male","Female","Male"],
    "Bonus":[5000,7000,6000,4500,5000],
    "Rating":[4.5,4.0,3.8,4.7,3.5]
})
print(data)
print(data.shape)
print(data.info())
print(data.describe())
print(data.head(5))
print(data.tail(3))
avg=data["Salary"].mean()
print(avg)

bonus=data["Bonus"].sum()
print(bonus)

y=data["Age"].min()
print(y)

rat=data["Rating"].max()
print(rat)
sorted=data.sort_values(by="Salary",ascending=False)
print(sorted.head())
def category(rating):
  if(rating>=4.5):
    return "Excellent"
  elif (rating>=4.0 and rating<4.5):
    return "Good"
  else:
    return "Average"

data["Performance"]=data["Rating"].apply(category)
print(data.head())
miss=data.isnull()
print(miss)
data.rename(columns={"Employee id":"ID"},inplace=True)
print(data.head())

print(data["Years_Of_Experience"]>5)
print(data["Department"]=="IT")
filtered_data = data[(data["Years_Of_Experience"] > 5) & (data["Department"] == "IT")]
print(filtered_data)
data ["Tax"]=data["Salary"]*0.10
print(data.head())
data.to_csv("ans.csv",index=False)