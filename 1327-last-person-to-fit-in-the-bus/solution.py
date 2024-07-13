# sort the table by turn 
# loop through the the dataset
# keep always the last person that doesn't exceed and the total weight
# check the current if adding his weight make the total weight exceed, stop and return the last person


import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue.sort_values(by='turn', inplace=True)
    queue.reset_index(drop=True, inplace=True)
    #print(queue)
    cumul_weight = 0
    
    for i, row in queue.iterrows():
        cumul_weight += row['weight']
        #print(f"{i} --- {cumul_weight} --- {row['turn']}")
        if cumul_weight > 1000:
            return queue.iloc[[i-1]][['person_name']]
    
    return queue.iloc[[-1]][['person_name']]

    
