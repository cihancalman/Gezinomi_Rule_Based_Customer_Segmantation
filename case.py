# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 23:45:29 2023

@author: cihan
"""

import numpy as np
import pandas as pd


df = pd.read_excel("./miuul_gezinomi.xlsx")


df.head()


bins = [-1,7,30,90,df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]
          
df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins,labels=labels)        
          
agg_df = df.groupby(by=["SaleCityName","ConceptName","Seasons"]).agg({"Price":"mean"}).sort_values("Price",ascending=False)  


agg_df = agg_df.reset_index()


agg_df["sales_level_based"] = [col[0].upper() + "_" + col[1].upper()+"_" +   col[2].upper() for col in agg_df.values]

agg_df["SEGMENT"]=pd.qcut(agg_df["Price"], 4,["D","C","B","A"])


agg_df = agg_df[["sales_level_based","SEGMENT","Price"]]


user = "İZMIR_HERŞEY DAHIL_LOW"

agg_df[agg_df["sales_level_based"] ==  user ]   # A Segment 74.3









