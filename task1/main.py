from data import Data        
import json 
#import json module to convert data to json format.
#JSON is a syntax for storing and exchanging data.

data = Data()
data.input_people() #-> None

with open("people.json", "w") as f:
    json.dump(data.peoples, f)                       #covert data to json by using json.dump()
    print("data saved to people.json")
    
f = open("people.json", "r")
print(f.read())
f.close()

# Function is a reusable block of code that performs a specific task. It can take inputs, process them,
# and return the outputs. 
    
def avg_age(people, gender):    #-> float
    ages = [age for g, age in people if g == gender]
    return sum(ages)/len(ages) if ages else None

with open("people.json", "r") as f:
    people = json.load(f)

for gender in ["female", "male"]:
    avg = avg_age(people, gender)
    print(f"avg age of {gender}s: {avg}" if avg else f"no {gender} data available.")    
    
try:
    with open("people.json", "w") as f:
        people = json.load(f)
except ValueError:
    people = []
    #collecting the data.

# Append new data
people.extend(data.peoples)   # adds list of new people into existing

# Save back to file
with open("people.json", "w") as f:
    json.dump(people, f)  

print("Data appended to people.json")

# Show updated file
with open("people.json", "r") as f:
    print(f.read())
    


      
    
        