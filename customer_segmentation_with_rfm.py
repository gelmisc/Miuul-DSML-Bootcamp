# importing some library
import numpy as np
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt

# set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 300)

# define the dataset file
df = pd.read_csv("/kaggle/input/flo-data-20k/flo_data_20k.csv")

# control the defined dataset
df.head()

# define a function to better understand the dataset
def check_df(dataframe, head=5):
    print(" SHAPE ".center(70,'#'))
    print('Rows: {}'.format(dataframe.shape[0]))
    print('Columns: {}'.format(dataframe.shape[1]))
    print(" INFO ".center(70,'#'))
    print(dataframe.info())
    print(" MISSING VALUES ".center(70,'#'))
    print(dataframe.isnull().sum())
    print(" DUPLICATED VALUES ".center(70,'#'))
    print(dataframe.duplicated().sum())
    print(" DESCRIBE ".center(70,'#'))
    print(dataframe.describe([0, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1]).T)
    
# use this function and checking dataset
check_df(df)

# When we examine the data set, we see that the number of purchases made and the total paid wage variables are analyzed in separate variables, 
# online and offline. Let's collect the variables and make them a single variable.
df['order_num_total'] = df['order_num_total_ever_online'] + df['order_num_total_ever_offline']
df['customer_value_total'] = df['customer_value_total_ever_offline'] + df['customer_value_total_ever_online']
df.head()

# Now we can see our order_num_total and customer_value_total variables in the dataset. 
#We created our variables for the total number of purchases made and the total amount of money spent.

# In the preparation process of RFM metrics, we need to change the type of the variables containing date information in the dataset to the 'datetime' type.
# All variables containing dates can be accessed with the expression   df.loc[:, df.columns.str.contains('date')]
# Let's convert all these variables to datetime type and assign them to the same variables.
df.loc[:, df.columns.str.contains('date')] = df.loc[:, df.columns.str.contains('date')].apply(pd.to_datetime)

# checking what we did.
print(" INFO ".center(70,'#'))
print(df.info())

# For the first metric, 'Recency', we need to calculate the time from the customer's last shopping date to the analysis date.
# Let's find the last shopping date in the dataset
df['last_order_date'].max()

# For the analysis date, I usually choose 2 days after the last shopping date.
# And keep this date as today_date variable.
today_date = dt.datetime(2021, 6, 1)
today_date

# We defined the variables we need as a new dataset by grouping them on the basis of the 'master_id' variable.
rfm = df.groupby('master_id').agg({'last_order_date': lambda last_order_date: (today_date - last_order_date.max()).days,
                                  'order_num_total': lambda order_num_total:  order_num_total,
                                  'customer_value_total': lambda customer_value_total: customer_value_total })

# check the 'rfm' dataset
rfm.head()

# Let's change the names of the 'last_order_date', 'order_num_total', 'customer_value_total' variables in the '**rfm**' dataset with RFM metrics
rfm.columns= ['recency', 'frequency', 'monetary']
rfm.head()

rfm['recency_score']= pd.qcut(rfm['recency'], 5 , [5, 4, 3, 2, 1])
rfm['frequency_score']= pd.qcut(rfm['frequency'].rank(method='first'), 5 , [1, 2, 3, 4, 5])
rfm['monetary_score']= pd.qcut(rfm['monetary'], 5 , [1, 2, 3, 4, 5])
rfm.head()

rfm['RF_SCORE']= rfm['recency_score'].astype(str) + rfm['frequency_score'].astype(str)
rfm.head()

# r'[1-2][3-4]': at_risk when reading the first digit of the score (1 or 2),
# when seen in second digit (3 or 4) argument 'regex=True' inserts 
# the string expression corresponding to the numbers read.

seg  = { r'[1-2][1-2]': 'hibernating',
         r'[1-2][3-4]': 'at_risk',
         r'[1-2]5'		: 'cant_loose',
         r'3[1-2]'		: 'about_to_sleep',
         r'33'				: 'need_attention',
         r'[3-4][4-5]': 'loyal_customers',
         r'41'				: 'promising',
         r'51'				: 'new_customers',
         r'[4-5][2-3]': 'potantial_loyalist',
         r'5[4-5]'		: 'champions' }

rfm['RF_SEGMENTS'] = rfm['RF_SCORE'].replace( seg, regex=True )
rfm.head()

import plotly.express as px
fig = px.pie(rfm, names='RF_SEGMENTS')
fig.update_layout(width = 600, height = 400,
                  margin = dict(t=0, l=0, r=0, b=0))
fig.update_traces(textfont_size=13)
fig.show()

rfm[["RF_SEGMENTS", "recency", "frequency", "monetary"]].groupby("RF_SEGMENTS").agg(["mean", "count"])

pd.merge( rfm[rfm['RF_SEGMENTS'].isin(['champions', 'loyal_customers'])] ,  
         df[ df['interested_in_categories_12'].str.contains('KADIN')], 
         on='master_id')[['master_id']].to_csv('new_brand_target_customer.cvs', index=False)

### THE END ###