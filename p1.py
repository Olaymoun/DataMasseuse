import pandas as pd
pd.set_option('precision', 5)

df= pd.read_csv('/Users/unknown1/Desktop/Gyro3.csv')

final_df = pd.DataFrame()
i = 0
end = len(df)

while i < end:
    
    first_six = []
    # loop through all three columns of subset of six rows
    for x in range(3):
        first_six += ( df.iloc[i:i+6, x].values.tolist())
    # append each dataframe of six rows to the final dataframe
    final_df = final_df.append(pd.DataFrame(first_six).transpose())
    i += 6

# output to csv file
final_df.to_csv('out.csv',float_format='%.5f', header = False, index = False)








#
#first_six =[]
#for x in range(3):
#    first_six += ( df.iloc[0:6, x].values.tolist())
#
#print(pd.DataFrame(first_six).transpose())