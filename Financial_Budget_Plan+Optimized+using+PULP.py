
# coding: utf-8

# In[1]:

from pulp import *
import numpy as np
import pandas as pd
import re 
import matplotlib.pyplot as plt
from IPython.display import Image
get_ipython().magic('matplotlib inline')


# In[2]:

data= pd.read_excel("newp.xlsx")
data[0:]


# In[3]:

fig, axs = plt.subplots(1,2)
my_plot = data[['Product_Name', ' Price']].plot(kind='bar', title="Products by Price", ax=axs[0])
my_plot = data[['Product_Name', 'Storage']].plot(kind='bar', title="Destination by Duration", ax=axs[1])


# In[4]:

prob = pulp.LpProblem('FinancingMonthlyBudget', pulp.LpMinimize)


# In[5]:

decision_variables = []
for rownum, row in data.iterrows():
    variable = str('x' + str(rownum))
    variable = pulp.LpVariable(str(variable), lowBound = 0, upBound= None, cat = 'Integer')
    decision_variables.append(variable)

print("Total number of Decision Varibales:" + str(len(decision_variables)))
print("Array of Decision Variables:" + str(decision_variables))


# In[6]:

total_money = ""
for rownum, row in data.iterrows():
    for i, money in enumerate(decision_variables):
        if rownum == i:
            formula = row[' Price']*money
            total_money += formula
prob += total_money
print("Function to be optimized : " + str(total_money))


# In[7]:

aval_space = 10
total_packages = ""
for rownum, row in data.iterrows():
    for i, place in enumerate(decision_variables):
        if rownum == i:
            formula = row['Storage']*place
            total_packages += formula
prob += (total_packages==aval_space)
print("Constraint:" + str(total_packages))


# In[8]:

print(prob)
prob.writeLP("FinancingMonthlyBudget.lp")


# In[9]:

optimization_result = prob.solve()

assert optimization_result == pulp.LpStatusOptimal
print("Status:", LpStatus[prob.status])
print("Optimal Solution to the Problem:", value(prob.objective))
print("Individual decision_variables:")
for v in prob.variables():
    print(v.name, "=", v.value)


# In[10]:

variable_name = []
variable_value = []

for v in prob.variables():
    variable_name.append(v.name)
    variable_value.append(v.varValue)

df = pd.DataFrame({'variable': variable_name, 'value': variable_value})
for rownum, row in df.iterrows():
    value = re.findall(r'(\d+)', row['variable'])
    df.loc[rownum, 'variable'] = int(value[0])

df = df.sort_values(by='variable')


for rownum, row in data.iterrows():
    for results_rownum, results_row in df.iterrows():
        if rownum == results_row['variable']:
            data.loc[rownum, 'decision'] = results_row['value']
data[0:]


# In[ ]:



