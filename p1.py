import pandas as pd
pd.set_option('precision', 5)

df= pd.read_csv('/Users/unknown1/Desktop/Gyro3.csv')

first_six =[]
for x in range(3):
    first_six += ( df.iloc[0:6, x].values.tolist())

final_df = pd.DataFrame(first_six).transpose()

final_df.to_csv('firstSix.csv',float_format='%.5f', header = False, index = False)