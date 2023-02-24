# IntroductionToPython_CaseStudy2

 **1. Using the ListComprehension structure, _capitalize_ the names of the numeric variables in the car_crashes data set and prepend it with _"NUM"_.**
 - _The names of non-numeric variables should also grow._
- _A single list comprehension structure should be used._
 
 ```python
import seaborn as sns
df = sns.load_dataset("car_crashes")

pd.set_option('display.width', 500)  
pd.set_option('display.max_columns', None)

df.columns
```

> **Solution:**
>```python
>["NUM_" + col.upper() if df[col].dtype != "0" else col.upper() for col in df.columns]
>```
___
 **2. Using the ListComprehension structure, put _"FLAG"_ at the end of the variables that do not contain _"no"_ in their names in the car_crashes data set.**
- _All variable names must be uppercase._
- _A single list comprehension structure should be used._

> **Solution:**
> ```python
>[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in cc.columns]
>```
___
**3. Select the ones other than the following variables with ListComprehension and create a new dataframe.**

```python
og_list = ["abbrev", "no_previous"]
```
 - _First, create a new list named new_cols by using list comprehension according to the given list._
 - _Then create a new dataset named new_df by selecting these variables with df[new_cols]_

> **Solution:**
> ```python
> new_cols = [col for col in df.columns if col not in og_list]
> new_df = df[new_cols]
> new_df.head()


