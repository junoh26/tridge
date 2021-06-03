# Question 3
import pandas as pd


df = pd.read_csv('dataSet.csv')

"""
First, we should delete parts of the values for Variety column and Grades column.
EX: Avocado / Variety / Hass -> Hass
    Avocado / Grade / Second Quality -> Second Quality

Pseudo Code:
df['Variety'].replace(r"\w \bVariety\b ", "", inplace=True)
df['Grades'].replace(r"\w \bGrade\b ", "", inplace=True)
"""

print(df.isna().sum() / len(df) * 100)
"""
By checking the percentage of missing values in each column,
we see that 10.9 % of rows are missing values in Variety, and
38.5% of rows are missing values in Grades, and
over 80% of rows are missing values in weekly prices.

Missing values can lead to several issues. There are possible
preprocessing methods to solve these issues. 

We could drop missing data, replace missing data, or
leave missing data as they are. I would not replace msissing data, because
replacing categorical data with the most frequent category or replacing 
price data with the average price would corrupt the data in general. 
Different products might be seen as same type of product if their values for
all categorical columns are the same. Also, maintaing exact weekly price seems
to be important in terms of the usage of these data. There wouldn't be any point
in recording average price for weekly prices across several years. 
Therefore, I think we should drop missing data first for certain cases and leave missing 
data as they are for the rest.

1. There are many rows with no values for any weekly prices.
    -> We can delete these rows as they lack any kind of price data.
    -> If we happen to gain information about their price in the future,
       we could add them to database accordingly.

    Pseudo Code:   
    df.dropna(subset=[every weekly price column],axis=0,inplace=True)

2. Some rows are missing values in Variety and Grades.
   This leads to a problem in which some rows have the same value for
   other remaining columns. Then, we are not able to differentiate these items.
    -> Group rows with same value for columns other than the prices.
    -> Join them as one row and could possibily use the mean value of the available prices.

    Pseudo Code:
    duplicateRows = df.groupby(["Product", "Country", "Variety", "Grades", "Region"])
                        .agg({every weakly price column: 'mean'})

Regarding possible normalization methods, I am not sure whether we need to use
normalization methods such as MinMax and Z-Score if we are not trying to construct
any machine learning models. 
"""
