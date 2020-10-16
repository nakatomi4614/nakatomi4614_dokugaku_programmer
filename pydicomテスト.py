# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:30:41 2020

@author: nakatomi
"""

from pathlib import Path
import pydicom, re
import pandas as pd
import pprint
from scipy.stats import brunnermunzel
from scipy.stats import median_test
from scipy.stats import chi2_contingency
import numpy as np
import scipy.stats as stats

#
path_data = r"C:\Users\neuph\OneDrive\文書\Documents\2020研究発表\JCRT\CTDIDLPonly.xlsx"
path_output = "C:\新しいフォルダー\研究用\CTDIDLP\CTDIDLPonly.csv"
df = pd.read_excel(path_data, sheet_name="chest", header=0)

df_std = df["標準体重CTDI"]
df_n10 = df["n=10 CTDI"]
df_all = df["all"]

x = df_all.quantile(0.75)
x1 = df_all.quantile(0.25)
x2 = x + (x-x1) * 1.5
x3 = x1 - (x-x1) * 1.5
df_all_outlier_excluded = df.query('@x3 <= all < @x2') #@変数でqueryで変数を使える
df_all_outlier_excluded = df_all_outlier_excluded["all"]

print("標準体重75パーセンタイル",df_std.quantile(0.75))
print("n=10 75パーセンタイル",df_n10.quantile(0.75))
print("全標本75パーセンタイル",df_all.quantile(0.75))
print("全標本外れ値除外75パーセンタイル",df_all_outlier_excluded.quantile(0.75))

df_stdup75 = ((df_std >= df_std.quantile(0.75)).sum())
df_n10up75 = ((df_n10 >= df_n10.quantile(0.75)).sum())
df_allup75 = ((df_all >= df_all.quantile(0.75)).sum())
df_all_outlier_excludedup75 = ((df_all_outlier_excluded >= df_all_outlier_excluded.quantile(0.75)).sum())
df_stdunder75 = df_std.count() - df_stdup75
df_n10under75 = df_n10.count() - df_n10up75
df_allunder75 = df_all.count() - df_allup75
df_all_outlier_excludedunder75 = df_all_outlier_excluded.count() - df_all_outlier_excludedup75

std_list = [df_stdup75,df_stdunder75]
all_list = [df_allup75,df_allunder75]
n10_list = [df_n10up75,df_n10under75]
all_outlier_excluded_list = [df_all_outlier_excludedup75,df_all_outlier_excludedunder75]
df2 = pd.DataFrame([n10_list,std_list])
df3 = pd.DataFrame([all_list,std_list])
df4 = pd.DataFrame([all_outlier_excluded_list,std_list])

chi2, p, dof, expected = chi2_contingency(df2, correction=False)
print("標準体重とn=10")
print(df2)
print("カイ二乗値:", chi2)
print("p値:", p)
print("自由度:", dof)
print("期待度数:", expected)
chi2, p, dof, expected = chi2_contingency(df3, correction=False)
print("外れ値除外なし")
print(df3)
print("カイ二乗値:", chi2)
print("p値:", p)
print("自由度:", dof)
print("期待度数:", expected)
chi2, p, dof, expected = chi2_contingency(df4, correction=False)
print("外れ値除外")
print(df4)
print("カイ二乗値:", chi2)
print("p値:", p)
print("自由度:", dof)
print("期待度数:", expected)
