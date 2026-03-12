


# student_id , student_name, course_name,course_duration,total_fees isme 10 rows tk ka data
#  dataframe mai convert krna hai or uske baad us data
# ko csv and  excel mai export krna hai than these two data sets you have to create a new repo (data_students) and upload 2 datasets
# into github repo

import pandas as pd
data = {
    "student_id": [1,2,3,4,5,6,7,8,9,10],
    "student_name": ["Akanksha", "Priya", "Rahul", "Sonia", "Vikas", "Anjali","Abhishek","Riya","Gungun","Bhavna"],
    "course_name": ["Data Science", "Python", "Web Dev", "Data Science", "AI", "Python", "ML", "Web Dev", "AI", "Data Science"],
    "course_duration": ["6 Months", "3 Months", "4 Months", "6 Months", "8 Months", "3 Months", "7 Months", "4 Months", "8 Months", "6 Months"],
    "total_fees": [50000, 25000, 35000, 50000, 65000, 25000, 60000, 35000, 65000, 50000]
}
df = pd.DataFrame(data)
df

df.to_csv("Student_data.csv")

df.to_excel("New_student_data.xlsx")

# go to browser search best hotels in a masoorie use instant data scrapper create data using pandas

import pandas as pd

Trip = pd.read_excel("/content/tripadvisor (2).xlsx")
Trip