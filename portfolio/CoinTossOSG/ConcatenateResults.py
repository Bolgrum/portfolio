number = 500
with open('CompleteResults.txt', 'w') as outfile:
        for i in range (number):
            stringName = "results" + str(i) + ".txt"
            print(stringName)
            with open (stringName) as infile:
                outfile.write(infile.read())