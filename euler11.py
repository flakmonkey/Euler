import csv

file_data = csv.reader(open('data11', 'rb'), delimiter=' ')

data = []
for row in file_data:
	data.append(row)

data = [map(int,row) for row in data]

def max_horizontal(data):
        max_h = 0
        for row in data:
                for i in range(0,16):
                        temp = row[i]*row[i+1]*row[i+2]*row[i+3]
                        max_h = temp if temp > max_h else max_h
        return max_h

def max_vertical(data):
        max_v = 0
        for i in range(0,16):
                for j in range(0,20):
                        temp = 1
                        for k in range(0,4):
                                temp *= data[i+k][j]
                        if temp > max_v:
                                max_v = temp
        return max_v

def max_diagonal(data):
        max_d = 0
        for i in range(0,16):
                for j in range(0, 16):
                        temp = diag(data,i,j)
                        max_d = temp if temp > max_d else max_d
        return max_d

def vertical(data,i,j):
        temp = 1
        for k in range(0,4):
                temp *= data[i+k][j]
        return temp

def diag(data,i,j):
        temp = 1
        for k in range(0,4):
                temp *= data[i+k][j+k]
        return temp

def diag_r(data,i,j):
        temp = 1
        for k in range(0,4):
                temp *= data[i-k][j-k]
        return temp

def horizontal(data,i,j):
        temp = 1
        for k in range(0,4):
                temp *= data[i][j+k]
        return temp


