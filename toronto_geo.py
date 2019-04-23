#%% [markdown]
# **I used the csv file to merge with the dataframe created in the previous assignment.**
#%% [markdown]
# *Rows were removed where the Borough was Not assigned.
# Neighbourhood was replaced by the Borough if Neighbourhood was Not assigned.
# Neighbourhood was renamed since I am not British.
# Postcode was renamed for the merge.*

#%%
import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\Users\AmyFurey\Desktop\Toronto.csv")
df.drop(df.loc[df['Borough']=='Not assigned'].index, inplace=True)
df['Neighbourhood'].loc[df['Neighbourhood']=='Not assigned']= df['Borough']
df.rename(columns={'Postcode': 'PostalCode', 'Neighbourhood':'Neighborhood'}, inplace=True)
print (df)

#%% [markdown]
# *Neighborhoods were grouped by Borough and separated by a comma.*

#%%
df1=df.groupby(['PostalCode','Borough'])['Neighborhood'].apply(','.join)
df1=df1.reset_index()

print (df1.head(10))


#%%
df1.shape

#%% [markdown]
# *Reading in the latitude and longitude data*

#%%
geo=pd.read_csv(r"C:\Users\AmyFurey\Desktop\geospatial_toronto.csv")
geo.rename(columns={'Postal Code':'PostalCode'}, inplace=True)
print (geo.head())

#%% [markdown]
# *Merging the toronto data with the geo data.*

#%%
df_geo=pd.merge(df1, geo, on=['PostalCode'], how='left')
print (df_geo.head(20))
print (df_geo.shape)


#%%



