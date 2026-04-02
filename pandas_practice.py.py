# pandas practice and notes ----- Sarthak Ahuja-----

# ----------INDEX OF NOTES---------- 
# 1 create dataframe
# 2 basic dataframe understanding
# 3 save and load data in csv file
# 4 rows and columns selection
# 5 filter dataframe
# 6 Rows and Columns operations (add, update, delete)
# 7 working with date values (formating)
# 8 handling missing values
# 9 aggregation and groupby
# 10 concatenate and merge dataframe


import pandas as pd


# 1) create dataframe ----------

data = {
    'name' : ['priya', 'rahul', 'panda', 'suraj'],
    'age' : [18, 23, 25, 19],
    'salary' : [15000, 50000, 65000, 45000]
}

df = pd.DataFrame(data)
print(df)

# 2) basic dataframe understanding  ----------

print(df.head(2)) # gives top n numbers of values which we passed in paranthesis
print(df.tail(1)) # gives least n numbers of values which we passed in paranthesis
print(df.shape) # gives size of the table in rows and columns
print(df.columns) # gives columns name
df.rename(columns = {'salary' : 'monthly_salary'}, inplace = True) # it used to rename the columns and inplace used to directly change into our data base
print(df.columns)
print(df.info()) # gives the information about dataset
print(df.describe()) #  it gives statistical summary (mean, std, min/max etc)


# 3) save and load data in csv file  ----------

df.to_csv('my_pandas_file.csv' , index = False) # 'index = False' used for remove row value

data_import = pd.read_csv('my_pandas_file.csv') #import/read csv file 
print('data import successfully', data_import)

# 4) rows and columns selection  ==========

print(df[['name' , 'monthly_salary']]) # for selecting columns
print(df.loc[df.name == 'panda']) # for select rows (label value based)
print(df.iloc[1]) # for select rows by passing index (index based)


# 5) filter dataframe  ----------

print(df[df['age'] > 20]) # filtering values
print(df[(df['age'] >= 20) & (df['monthly_salary'] >= 50000)]) # for multiple conditions by using '&' operator
print(df.where(df['age'] >= 20))


# 6) Rows and Columns operations (add, update, delete) ----------
#columns
df['team'] = ['ceo', 'hr', 'ba', 'da'] # create column
df['bonus'] = df['monthly_salary'] * 0.2 # calculating bonus
print(df)

#rows
df.loc[len(df)] = ['abc', 21, 21000, 'it', 2000] # adding data into row
df.loc[0, "monthly_salary"] = 95000 # "0" is the index and monhly_salary will be update whos index is "0"

# delete values
delete = df.drop(df[df.name == 'suraj'].index) # deleting row
print(delete)

print(df.drop('bonus', axis = 1)) # axis = (1 = column) or (0 = rows), deleting column

# data sorting
print(df.sort_values('monthly_salary')) # monthly_salary sorting in ascending order
print(df.sort_values("monthly_salary", ascending = False)) # monthly_salary sorting in descending order

# 7) working with date values (formating)  ----------

df['date_of_joining'] = ['14-02-2022', '02-02-2021', '07-05-2024', '2025-09-24', '01-10-2019'] # create date column 
print(df)

df['date_of_joining'] = pd.to_datetime(df['date_of_joining'], format='mixed', dayfirst=True) # i have mix date type so i used 'format = mixed'
print(df)


# 8) handling missing values  ----------
print(df.isnull()) # checking null values but in bullean, False means no null value
print(df.isnull().sum()) # sum all null value

print(df.fillna(0)) # replace all null values with "0"

# 9) aggregation and groupby

emp_data = { 'id' : [101, 102, 103, 104, 105],
            'name' : ['rakesh', 'roshan', 'suraj', 'kunal', 'chirag'],
            'salary' : [15000, 25000, 65000, 32000, 20000],
            'department' : ['hr', 'it', 'it', 'finance', 'it']
}

employee = pd.DataFrame(emp_data)
print(employee)

print(employee.groupby('department')['salary'].sum()) # use groupby in department and sum for add to get sum of total salary by each department


# 10) concatenate and merge dataframe  ----------

data2 = {
    'name' : ["manav", "komal", "madhav", "reema"],
     'age' : [25, 23, 18, 15]
         }
df2 = pd.DataFrame(data2) # create 2nd database
print(df2)

#concatenate
print(pd.concat([df, df2], axis = 0)) # (axis = 0, row join), (axis = 1, column join), using for mix 2 database together

# merge (join)

print(pd.merge(df, df2, how = 'outer')) # merging two databse, we can use (ON = 'ID') for connecting two table i do not have one so i didn't use