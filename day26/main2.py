import pandas

data = pandas.read_csv("file1.txt",header=None)
data2 = pandas.read_csv("file2.txt",header=None)
df = pandas.DataFrame(data)
df2 = pandas.DataFrame(data2)
file1 = df[df.columns[0]].values.tolist()
file2 = df2[df2.columns[0]].values.tolist()
result = [number for number in file1 if number in file2]
# result = []
# for number in file1:
#     if number in file2:
#         result.append(number)

print(result)