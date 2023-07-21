
file1 = open("sample.txt","r")
lines = file1.readlines()

print(lines)

dict1 = {}


for line in lines:
    if line not in dict1:
        dict1[line] = 1
    else:
        dict1[line] = dict1[line] +1

print(dict1)


# it creates questions in new file

def question_generator(dict1):

    f = open("newfile","a")

    for each in dict1:
        #print(each)
        f.write(each)
    f.close()

question_generator(dict1)
