import csv

age_count = [0] * 51
tds_count = [0] * 51
average_tds = [0] * 51

try:
    with open("RB_stats.csv", mode="r") as file:
        reader = csv.reader(file)
        next(reader) 
        
        for row in reader:
            age = int(row[3])
            tds = int(row[9])
            
            age_count[age] += 1
            tds_count[age] += tds

    max_tds = 0
    max_age = 0

    for age in range(51):
        if age_count[age] > 0:
            avg = tds_count[age] / age_count[age]
            average_tds[age] = avg
            
            print(f"Age = {age}, Count = {age_count[age]}, Total TDs = {tds_count[age]}, Avg TDs = {avg:.2f}")
            
            if avg > max_tds:
                max_tds = avg
                max_age = age

    
    print(f"The Max Avg TDs = {max_tds:.2f} at Age = {max_age}")

except FileNotFoundError:
    print("File not found. Make sure 'RB_stats.csv' is in the same directory as this script.")
except Exception as e:
    print(f"An error occurred: {e}")
