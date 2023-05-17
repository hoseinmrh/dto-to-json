file_data = []
# Put your file here
file = open("file.txt" , "r")
lines = file.readlines()
# Reading data
for line in lines:
    if("//" in line  or "@" in line or len(line) == 0): #Ignoring comments and Decorators and new lines
        continue
    if("exoprt class" in line or "{" in line or "}" in line): #Ignoring class name
        continue

    file_data.append(line.strip().split())


for i in range(len(file_data)):
    data = file_data[i]
    if (len(data) > 0):
        string = data[0]
        string = string[:len(string) - 1]
        if(i == (len(file_data) - 1)):
            print("\"%s\""% string, ":")
        else:
            print("\"%s\""% string, ":", ",")