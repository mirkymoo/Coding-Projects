midterm1 = 0
midterm2 = 0
final = 0

file = open("StudentInfo.tsv",'r')
contents = file.read()
contents = contents.replace("\t", " ")
contents = contents.split("\n")

report = open("report.txt", 'w')

for i in range(len(contents)):
    contents[i] = contents[i].split(" ")
print(contents)
contents.remove([''])

for i in range(len(contents)):
    avgtestgrade = (int(contents[i][2]) + int(contents[i][3]) + int(contents[i][4]))/3
    if 100 >= avgtestgrade > 80:
        avgtestgrade = "A"
    elif 80 >= avgtestgrade > 70:
        avgtestgrade = "B"
    elif 70 >= avgtestgrade > 60:
        avgtestgrade = "C"
    elif 60 >= avgtestgrade > 50:
        avgtestgrade = "D"
    elif 50 >= avgtestgrade > 0:
        avgtestgrade = "F"
    print(avgtestgrade)
    contents[i].append(avgtestgrade)
    midterm1 += int(contents[i][2])
    midterm2 += int(contents[i][3])
    final += int(contents[i][4])
    #midterm1.append(int(contents[i][2])) 
    
midterm1 = midterm1/int(len(contents))
midterm2 = midterm2/int(len(contents))
final = final/int(len(contents))
print(midterm1, midterm2, final)
    
for i in range(len(contents)):
    for j in range(len(contents[i])):
        report.write(f"{contents[i][j]}\t")
    report.write("\n")
report.write(f"\nAverages: midterm1 {midterm1:.2f}, midterm2 {midterm2:.2f}, final {final:.2f}")