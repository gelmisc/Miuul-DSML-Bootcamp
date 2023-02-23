# IntroductionToPython_CaseStudy1

 **1. Examine the types of variables below**
 
 ```python
 x = 8
type(x)

 y = 3.2
type(y)

 z = 8p + 12
type(z)

 a = "Hello World"
type(a)

 b = True
type(b)

 c = 23 < 22
type(c)

 l = [1,2,3, 4.5, "John", "Jane"]
type(l)

 t = ("Machine Learning", "Data Science", "Python")
type(t)

 s = {"Pandas", "Numpy", "Seaborn"}
type(s)

 d = {"Name": "Fatih",
		 "Age": 32,
		 "Address": "Istanbul"}
type(d)
```
___
 **2. Convert all letters of the given string to uppercase. Put space instead of commas and periods, separate them word by word.**

 ```python
text = ("ne mutlu türküm diyene")
```

> **Solution:**
> ```python 
> text.upper().replace(".", " ").replace(",", " ").split()
> ```
___
**3. Apply the following steps to the given list.**

```python
lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
```

 - See the number of items in the given list.

> **Solution:**
> ```python
> len(lst)

 - Call the elements in the zeroth and tenth index.

> **Solution:**
> ```python
> lst[0], lst[10]

 - Create a list["D", "A", "T", "A"] from the given list.

> **Solution:**
> ```python
> new_lst = (lst[0:4])

 - Delete the element in the eighth index.

> **Solution:**
> ```python
> lst.pop(8)

 - Add a new element.

> **Solution:**
> ```python
> lst.append("S")

 - If the eighth index, repeat the "N" element

> **Solution:**
> ```python
> lst.insert(8, "R")
___
**4. Perform the following steps on the given dictionary structure.**
```python
dict = {'Christian': ["America", 18],
	'Daisy': ["England", 12],
	'Antonio': ["Spain", 22],
	'Dante': ["Italy", 25]}
```

 - Access the keys.

> **Solution:**
> ```python
> dict.keys()

 - Access the values.

> **Solution:**
> ```python
> dict.values()

 - Update Daisy's 12 value to 13.

> **Solution:**
> ```python
> dict["Daisy"][1]=13

 - Add a new data with key name Ahmet, values ​​["Turkey", 24].

> **Solution:**
> ```python
> dict.update({"Ahmet": ["Turkey", 24]})

 - Delete Antonio from dictionary.

> **Solution:**
> ```python
> dict.pop("Antonio")
___
**5. Enter a function that takes a list as an argument, assigns the odd and even numbers within the list to separate lists, and returns the lists.**

```python
l = [2, 13, 18, 93, 22]
```

> **Solution:**
> ```python def func(list):  
>     odd=[]  
>     even=[]  
>     for number in list:  
>         if number % 2 == 0:  
>             even.append(i)  
>         else:  
>             odd.append(i)  
>     return odd, even
> 
> 
>   odd, even = func(l)   odd, even 
>   ```
___
**6. In the list below, there are the names of the students who entered the degree in engineering and medical faculty. The first three students show the engineering faculty and the last three students show the medical school success rank. Print student degrees by faculty using enumerate.**

```python
students = ["John", "Marry", "Kane", "Dennis", "Lloyd", "Cindy"]
```

> **Solution:**
> ```python
> for index, student in enumerate(students):  
>    if index < 3:  
>        index += 1
>        print("Engineering Fac.", index, ". student:", student)
>    else:  
>        index -= 2  
>        print("Medical Fac.", i, ". student:", student)
> ```
___
**7. Print the three lists below using Zip.**
```python
lessons = ["MATH1001", "CMSC7001", "PSC4101"]
credits = [4,4,2]
quotas = [120, 90, 60]
```

> **Solution:**
> ```python
> for lessons, credits, quotas in zip(lessons, credits, quotas):
>     print(f"{credits} credit {lessons} lesson quotas are {quotas} person.")
> ```
___
**8. Below are 2 sets. if set 1 includes set 2, print their common elements, else print the difference of set 2 from set 1**

```python
set1 = (["data", "python"])
set2 = (["data", "function", "qcut", "lambda"], "python", "miuul")
```

> **Solution:**
> ```python
> set1.issuperset(set2)  
> set2.issuperset(set1)  
>
> set1.intersection(set2)  
> set2.intersection(set1)  
>
> set1.difference(set2)  
> set2.difference(set1)
> ```

