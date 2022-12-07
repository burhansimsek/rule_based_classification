# Rule-Based Classification - Potential Customer Profit Calculation

# A gaming company wants to create level-based personas using some characteristics of its customers,
# create segments based on these new customer personas,
# and based on these segments estimate how much new customers can earn on average for the company.
# For example: We want to determine how much a 25-year-old male IOS user from Turkey can earn on average.

import pandas as pd

# PRICE - Customer's spending amount
# SOURCE - Type of device the client is connected to
# SEX - Gender of the customer
# COUNTRY - Customer's country
# AGE - Age of the customer

df = pd.read_csv("Python Programming for Data Science/pycharm/persona.csv")
df.head()
df.shape
df.info()
df.nunique()
df["SOURCE"].value_counts()
df["PRICE"].unique()
df["PRICE"].value_counts()
df["COUNTRY"].value_counts()
df.groupby("COUNTRY").agg({"PRICE": "sum"})
df.groupby("SOURCE").agg({"PRICE": "count"})
df.groupby("COUNTRY").agg({"PRICE": "mean"})
df.groupby("SOURCE").agg({"PRICE": "mean"})
df.pivot_table("PRICE", "COUNTRY", "SOURCE")
# What are the average earnings by COUNTRY, SOURCE, SEX, AGE?
# df.iloc[:, 1:].columns
agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values(by="PRICE", ascending=False)
agg_df.columns
agg_df.index
agg_df.shape
agg_df.ndim
agg_df.reset_index(inplace=True)
agg_df
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], [0, 18, 23, 30, 40, 70], labels=["0_18", "19_23", "24_30", "31_40", "41_70"])
agg_df

# {country+"_"+source+"_"+sex+"_"+age_cat, price for country, source, sex, age_cat, price in agg_df }

agg_df["customer_level_based"] = [value[0].upper()+"_"+value[1].upper()+"_"+value[2].upper()+"_"+value[3].upper()
                                  for value in agg_df.loc[:, ["COUNTRY", "SOURCE", "SEX", "AGE_CAT"]].values]
agg_df.head()

last_df = agg_df.groupby("customer_level_based").agg({"PRICE": "mean"})
last_df.reset_index(inplace=True)
last_df.head()
last_df.info()
last_df
df.info()
last_df["SEGMENT"] = pd.qcut(last_df["PRICE"], 4, labels=["D", "C", "B", "A"])
last_df
last_df.value_counts().any() != 1
last_df.groupby("SEGMENT").agg({"PRICE": "mean"})
last_df[last_df["customer_level_based"] == "tur_ios_male_19_23"]
