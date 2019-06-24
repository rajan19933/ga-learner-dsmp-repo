# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
#Code starts here 
data['Gender'] = data['Gender'].replace('-','Agender')
#print(data['Gender'])
gender_count = data['Gender'].value_counts()
#print(gender_count)
gender_count.plot.bar()


# --------------
#Code starts here
import matplotlib.pyplot as plt

alignment = data['Alignment'].value_counts()
plt.pie(alignment)


# --------------
#Code starts here
sc_df = data[['Strength','Combat']]
sc_covariance = sc_df.cov().iloc[0,1]
sc_strength = sc_df['Strength'].std()
sc_combat =  sc_df['Combat'].std()
sc_pearson = sc_covariance/(sc_strength*sc_combat)
print('Pearson\'s correlation coefficient between Strength & Combat is: ',sc_pearson)
ic_df = data[['Intelligence','Combat']]
ic_covariance = ic_df.cov().iloc[0,1]
ic_intelligence = ic_df['Intelligence'].std()
ic_combat =  ic_df['Combat'].std()
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)
print('Pearson\'s correlation coefficient between Intelligence & Comba is: ',ic_pearson)


# --------------
#Code starts here
total_high = round(data['Total'].quantile([.99]).values[0],2)
print('Total High: ',total_high)
print(type(total_high))
#print(total_high.values)
super_best = data[data['Total'].values>total_high]
print(type(super_best))
super_best_names = super_best['Name'].values.tolist()
print(super_best_names)



# --------------
#Code starts here
'''
ax_1 = plt.figure().add_subplot(111)
ax_2 = plt.figure().add_subplot(111)
ax_3 = plt.figure().add_subplot(111)

ax1.boxplot(super_best)
ax2.boxplot(super_best)
ax3.boxplot(super_best)

ax1.set_title('Intelligence')
ax2.set_title('Speed')
ax3.set_title('Power')

plt.show()
'''
#Setting up the subplots
fig, (ax_1, ax_2,ax_3) = plt.subplots(1,3, figsize=(20,8))

#Plotting box plot
ax_1.boxplot(super_best['Intelligence'])

#Setting the subplot axis title
ax_1.set(title='Intelligence')


#Plotting box plot
ax_2.boxplot(super_best['Speed'])

#Setting the subplot axis title
ax_2.set(title='Speed')


#Plotting box plot
ax_3.boxplot(super_best['Power'])

#Setting the subplot axis title
ax_3.set(title='Power')

#Code ends here   


