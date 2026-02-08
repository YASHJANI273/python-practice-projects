import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv("diamonda.csv")
print (df)
df.head(5)
df.tail(5)
df.shape
df.columns
df.info()
df.dtypes
df.describe()

df1=df.drop(columns='Unnamed: 0')

df1['carat'].value_counts()

cutCounts=df1['cut'].value_counts()
cutCounts

colorCounts=df1['color'].value_counts()
colorCounts

plt.figure(figsize=[12,6])
plt.hist(df["price"], bins=80, color="purple")
plt.xlabel("Price in USD")
plt.ylabel("Frequency")
plt.title("Diamonds Price Histogram")
plt.show()

# To visulize how the price changes with the carat
plt.figure(figsize=(12, 6))
plt.plot(df1['price'],df1['carat'])
plt.title('Carat v/s Price')
plt.xlabel('Price')
plt.ylabel('Carat')
plt.show()

# To visulize how the price changes with the incrase in depth
plt.figure(figsize=(12, 6))
plt.plot(df1['price'],df1['depth'])
plt.title('Depth v/s Price')
plt.xlabel('Price')
plt.ylabel('Depth')
plt.show()

plt.figure(figsize=(12, 6))
cutCounts.plot(kind='line', color='orange')
plt.title('Distribution of Diamond Cuts')
plt.xlabel('Cut Type')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

plt.figure(figsize=(12, 6))
colorCounts.plot(kind='line', color='green')
plt.title('Distribution of Diamond Colors')
plt.xlabel('Color Type')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()

plt.figure(figsize=(12, 6))
cutCounts.plot(kind='bar', color='skyblue')
plt.title('Distribution of Diamond Cuts')
plt.xlabel('Cut Type')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--')
plt.show()

plt.scatter(df1['x'],df1['y'])
plt.title(" X-axis v/s Y-axis")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

df.loc[(df['x'] == 0) | (df['y'] == 0) | (df['z'] == 0)]

drop_index = df.loc[(df['x'] == 0) | (df['y'] == 0) | (df['z'] == 0)].index
df = df.drop(drop_index)
df.describe()

print(df['cut'].unique())
print(df['color'].unique())
print(df['clarity'].unique())

df['color'] = df['color'].factorize()[0]
df['cut'] = df['cut'].factorize()[0]
df['clarity'] = df['clarity'].factorize()[0]
df.head()

#WHICH DIAMOND TO BUY?
buy = df.copy()
buy['price_per_carat'] = buy['price'] / buy['carat']
buy = buy.sort_values(by='price_per_carat', ascending=True)
print(f"Best value for money: {round(min(buy['price_per_carat']), 2)}$")
print("The first 3:\n")
buy.head(3)
df['cut'].value_counts()
df['color'].value_counts()
df['clarity'].value_counts()
labels = df['cut'].unique()
plt.pie(df['cut'].value_counts(), labels = labels)
plt.show()
labels = df['color'].unique()
plt.pie(df['color'].value_counts(), labels = labels)
plt.show()




