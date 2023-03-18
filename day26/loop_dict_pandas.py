import pandas

student_dict = {
    "student": ["Ncool","Dred","Princessa"],
    "score": [45,55,78]
}
student_dict_Dframe = pandas.DataFrame(student_dict)
for (index, data_in_row) in student_dict_Dframe.iterrows():
    if data_in_row.student == "Ncool":
        print(data_in_row.score)
