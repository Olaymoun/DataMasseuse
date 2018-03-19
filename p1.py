import pandas as pd
pd.set_option('precision', 5)

df= pd.read_csv('/Users/unknown1/Desktop/Gyro3.csv', chunksize=6)

final_df = pd.DataFrame()

# each chunk is a (6,3) dataframe
for chunk in df:
    
    first_six = pd.Series()
    # loop through all three columns of subset of six rows
    for x in range(3):
        first_six = first_six.append(chunk.iloc[:, x], ignore_index=True)
    
    # convert appended series to dataframe and transpose into a dataframe row
    six_df = pd.DataFrame(first_six)
    six_row = six_df.transpose()

    # append each new row to the final dataframe
    final_df = final_df.append(six_row)
    
final_df.to_csv('new_out.csv',float_format='%.5f', header = False, index = False)