#Collecting data from people to calculate average age of men and women
# By using class object and methods
# Class is creating objects, It defines attributes and methods.

class Data :           
    peoples = []          
    
    def __init__(self, gender:str = None):       #Class method to assign values to object values.
        self.gender = gender
    
    def input_people(self):
        print("Enter people's gender and age. Type 'q' to quit.")
        while True:
            gender = input("Enter the gender (male/female) or 'q' to quit: ").strip().lower()
            if gender == 'q':
                break
            if gender not in ['male', 'female']:
                print("Error: Please enter 'male' or 'female'.")
                continue
            while True:
                age_input = input("Enter the age: ").strip()
                try:
                    age = int(age_input)
                    if age > 0:
                        Data.peoples.append((gender, age))
                        print(f"Added: {gender}, {age}")
                        break
                    else:
                        print("Error: Age must be a positive number.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                
        # ...existing code...

if __name__ == "__main__":
    data = Data()
    data.input_people()
    print("Collected Data:", Data.peoples)
    
   
    
       


        
     
      
    
        
    
