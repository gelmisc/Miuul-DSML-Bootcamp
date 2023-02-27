
# IntroductionToPython_CaseStudy3

 **1. Define the _"titanic"_ dataset from the _"Seaborn"_ library.**
> **Solution:**
> ```python
> import seaborn as sns
> df = sns.load_dataset("titanic")
>
> pd.set_option('display.width', 500)
> pd.set_option('display.max_columns', None)
>
> df.head()
___

 **2. Find the sum of the female and male passengers in the Titanic dataset.**
> **Solution:**
> ```python
>df["sex"].value_counts()
___

**3. Find the number of unique values ​​for each column.**
> **Solution:**
> ```python
> df.nunique()
___

 **4. Find the number of unique values ​​of the variable pclass.**
> **Solution:**
> ```python
>df["pclass"].nunique()
___

**5. Find the number of unique values ​​of pclassveparch variables.**
> **Solution:**
> ```python
> df[["pclass", "parch"]].nunique()
___

 **6. Check the type of the embarked variable. Change the type to category and check again.**
> **Solution:**
> ```python
> df["embarked"].dtype  
> df["embarked"] = df["embarked"].astype("category")  
> df["embarked"].dtype
___

**7. Show all value from the embarked value _"C"_.**
> **Solution:**
> ```python
> df[df["embarked"] == "C"].head()
___

 **8. Show all value from the embarked value with no_"S"_.**
> **Solution:**
> ```python
>df[df["embarked"] != "S"].head()
___

**9. Show all information for passengers younger than 30 years old and female.**
> **Solution:**
> ```python
> df[(df["age"] < 30) & (df["sex"] == "female")].head()  
> df.loc[(df["age"] < 30) & (df["sex"] == "female")].head()
___
**10. Show the information of the passengers whose fare is over 500 or over 70 years of age.**
> **Solution:**
> ```python
> df[(df["fare"] > 500) | (df["age"] > 70)].head()  
> df.loc[(df["fare"] > 500) | (df["age"] > 70)].head()
___

 **11. Find the sum of the nulls in each variable.**
> **Solution:**
> ```python
>df.isnull().sum()
___

**12. Remove the who variable from the dataframe.**
> **Solution:**
> ```python
>df.pop("who")  
>df.columns
___
**13. Fill the empty values ​​in the deck variable with the most repeated value (mode) of the deck variable.**
> **Solution:**
> ```python
> type(df["deck"].mode())  
> df["deck"].mode()[0]  
> df["deck"].fillna(df["deck"].mode()[0], inplace=True)  
> df["deck"].isnull().sum()
___
**14. Fill the empty values ​​in the age variable with the median of the age variable.**
> **Solution:**
> ```python
> df["age"].fillna(df["age"].median(),inplace=True)  
> df["age"].isnull().sum()
___

 **15. Find the sum, count, mean values ​​of the pclass and gender variables of the survived variable.**
> **Solution:**
> ```python
> df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]})
___

**16. Write a function that returns 1 to those under 30 and 0 to those above or equal to 30. Using the function you wrote, create a variable named age_flag in the titanic dataset. (use apply and lambda)**
> **Solution:**
> ```python
> df["age_flag"] = df["age"].apply(lambda x: 1 if x < 30 else 0)
___
**17. Define the Tips dataset from the Seaborn library**
> **Solution:**
> ```python
> df = sns.load_dataset("tips")  
> df.head()
___
**18. Find the sum of the total_bill values, min, max and mean according to the categories of the _"time"_ variable**
> **Solution:**
> ```python
> df.groupby("time").agg({"total_bill" : ["min","max","sum","mean"]})
___

 **19. Find the sum, min, max and mean of the total_bill values ​​according to the days and time variables.**
> **Solution:**
> ```python
> df.groupby(["day", "time"]).agg({"total_bill" : ["min","max","sum","mean"]})
___

**20. Find the sum, min, max and average of the total_bill and tip values ​​of the lunch time and female customers according to the day.**
> **Solution:**
> ```python
> df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({
>	"total_bill": ["min","max","sum","mean"], "tip": ["min","max","sum","mean"]})
___
**21. What is the average of orders with a size less than 3 and a total_bill greater than 10? (use loc)**
> **Solution:**
> ```python
> df.loc[(df["size"] < 3) & (df["total_bill"] > 10)].mean()
___

 **22. Define a new variable called total_bill_tip_sum. Return the total_bill and tip total paid by each customer.**
> **Solution:**
> ```python
> df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
___

**23. Sort by the total_bill_tip_sum variable in descending order and assign the first 30 people to a new dataframe.**
> **Solution:**
> ```python
> new_df = df.sort_values("total_bill_tip_sum", ascending=False).head(30)  
> new_df.shape
___


