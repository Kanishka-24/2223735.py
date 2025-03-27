import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel("C:/Users/S516-01/Documents/bajabdata.xlsx")  

data['attendance_date'] = pd.to_datetime(data['attendance_date'])

data = data.sort_values(by=['student_id', 'attendance_date'])

results = []


for student_id, group in data.groupby('student_id'):

    absence_start = None
    absence_count = 0

    for index, row in group.iterrows():
        if row['status'] == 0:  
            if absence_start is None:
                absence_start = row['attendance_date']
            absence_count += 1
        else:
            if absence_count > 3:  
                results.append({
                    'student_id': student_id,
                    'absence_start_date': absence_start,
                    'absence_end_date': row['attendance_date'] - pd.Timedelta(days=1)
                })
         
            absence_start = None
            absence_count = 0

    if absence_count > 3:
        results.append({
            'student_id': student_id,
            'absence_start_date': absence_start,
            'absence_end_date': group['attendance_date'].iloc[-1]
        })

results_df = pd.DataFrame(results)

print(results_df)