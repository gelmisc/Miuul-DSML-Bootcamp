
# CRM -  Customer Relationship Management

CRM Analytics allows to express the communication or interaction with customers with visual techniques and to bring them into a traceable form with various KPIs and follow them.

- Communication (language, color, images, campaigns)
- Customer acquisition/finding studies
- Customer retention (abandonment) studies
- Cross-sell, up-sell
- Customer segmentation studies are handled within this scope.


### KPI - Key Performance Indicator
They are mathematical indicators used to evaluate the performance of a company, department or employee.

#### KPI Examples
-   Customer Acquisition Rate
-   Customer Retention Rate
-   Customer Churn Rate
-   Conversion Rate
-   Growth Rate

#### Cohort Analysis

**Cohort:** It refers to a group of people with common characteristics.
**Cohort Analizi:** It is the analysis of the behavior of a group of people with common characteristics.

## Customer Segmentation with RFM

### RFM (Recency - Frequency - Monetary)
RFM Analysis is a technique used for customer segmentation.
It enables customers to be divided into groups based on their purchasing habits and to develop strategies specific to these groups.

It provides the opportunity to take data-based actions on many topics for CRM studies.

| RFM Metrics|What does it mean?|
|:-:|-|
|Recency|Last shopping date, customer's freshness|
|Frequency|Total number of purchases, frequency of transactions|
|Monetary|Monetary return of the customer, his expenses|

> Example:

||R|F|M|
|:-:|:-:|:-:|:-:|
|**Customer1**|80|250|==5200==|
|**Customer2**|7|==560==|2300|
|**Customer3**|==1==|120|3000|
|~|~|~|~|
|**Customer1000**|35|300|4500|

Since the **Recency** metric indicates the time elapsed since the last purchase date, the smallest value is considered the best result, while the largest values ​​for the **Frequency** and **Monetary** metrics are considered the best result.

In order to interpret the data in the table above, a scoring process is required. A kind of standardization is done so that they are compatible and comparable with each other.

> Example:

||R|F|M|RFM|
|:-:|:-:|:-:|:-:|:-:|
|**Customer1**|1|4|==5==|145
|**Customer2**|4|==5==|4|454
|**Customer3**|==5==|1|3|513
|~|~|~|~|~
|**Customer1000**|2|4|4|244

We make the data interpretable by giving scores between 1 and 5, from worst to best.
On the far right of the table, we create the customer's **RFM** score by bringing together the R, F, M scores.

### Creating Segments on Scores

||**5**|cant loose them|cant loose them|loyal customers|loyal customers|champions|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
||**4**|at risk|at risk|loyal customers|potential loyalist|**champions**
|==**F**==|**3**|at risk|at risk|need attention|potential loyalist|**potential loyalist**
||**2**|hibernating|hibernating|about to sleep|potential loyalist|**potential loyalist**
||**1**|hibernating|hibernating|about to sleep|promising|**new customers**
|||1|2|3|4|5
|||||==**R**==||

The distribution of the "F" frequency and "R" recency values ​​in the table indicates the segments of the customers. The champions and loyal customers segments are the segments where companies aim to position their customers. This is because they are the most loyal and most monetary segments.

For example; When we examine the “need attention” segment, it shows that the customers in this segment come to the company with a certain frequency and add a certain amount of monetary value, but this stops after a while. In this case, the studies for the customers in the need attention segment show that these customers can be brought back to the company. We can say that if customers in this segment are lost over time, the probability of customers falling into the "horse risk" segment, which is a lower step, is high, and this is an undesirable situation for companies.

The ultimate goal of companies in their CRM Analytics work is to try to attract the customers in the segment in the lower left part of the table to the segments in the upper right part.

After creating the scoring and segments, the final form of our table will be as follows.

|						 		|		R |		F |		M |RFM		|Segments						|
|:-------------:|:---:|:---:|:---:|:-----:|:-----------------:|
|**Customer1**		|1		|4		|==5==|145		|At Risk						|
|**Customer2**		|4		|==5==|4		|==454==|==Loyal Customers==|
|**Customer3**		|==5==|1		|3		|==513==|==New Customers==	|
|~							|~		|~		|~		|~			|~									|
|**Customer1000**|2		|4		|4		|244		|At risk						|
