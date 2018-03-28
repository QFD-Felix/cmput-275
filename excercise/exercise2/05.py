with open('edmonton_map.csv','r')as f: #f = open('Some.csv')
    reader = csv.reader(f,delimiter=',')
    for row in reader: # reaads a line, or "row"
        print(row)
