import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


homi=pd.read_csv("database.csv", low_memory=False)

#Question 1
solved = homi["Crime Solved"].value_counts().Yes
print solved

#Question 2
weapon_list = homi[homi['Weapon']!='Unknown']
weapon_count = weapon_list['Weapon'].value_counts()
print weapon_count[0:5]

#Question 3
