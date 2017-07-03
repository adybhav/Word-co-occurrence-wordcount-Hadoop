import csv
with open('nasdaq2.csv', 'r') as csvfile:
 spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
 counter=0
 c='",'
 d='"'
 with open('op1.csv', 'w', newline='') as csvfile:
     spamwriter = csv.writer(csvfile, delimiter=' ')
     for row in spamreader:
        temp=', '.join(row)
        if counter%2==0:
            if("\t" in temp):
                a=temp.index("\t")
                temp=temp[:a]+c+temp[a:]
            elif(" " in temp):
                a=temp.index(" ")
                temp=temp[:a]+c+temp[a:]
            elif("," in temp):
                a=temp.index(",")
                temp=d+temp[:a]+d+temp[a:]
            spamwriter.writerow(temp)
        else:
            if('"' not in temp):
                a=temp.index(",")
                temp=d+temp[:a]+d+temp[a:]
                spamwriter.writerow(temp)
     #           print(temp)
    #        temp=d+temp;
    #        print(temp)
        counter+=1

