import csv
import pandas as pd
from collections import Counter

with open("hieght.csv", newline="") as f:
    reader = csv.reader(f)
    fileData = list(reader)
fileData.pop(0)
newData = []
for i in range(len(fileData)):
    num = fileData[i][1]
    newData.append(float(num))

# getting the mean

n = len(newData)
newData.sort()
total = 0

for x in newData:
    total = total+x

mean = total/n

print("mean/average is:"+str(mean))

# calculating the median

if (n % 2 == 0):
    # getting the first number
    median1 = float(newData[n//2])
#  getting the second number
    median2 = float(newData[n//2-1])
    median = (median1+median2)/2
else:
    median = newData[n//2]

print("median is:"+str(median))

# calculating the mode
data = Counter(newData)
modeDataForRange = {
    "50-60": 0, "60-70": 0, "70-80": 0
}
for height, occurence in data.items():
    if (50 < float(height) < 60):
        modeDataForRange["50-60"] += occurence
    elif (60 < float(height) < 70):
        modeDataForRange["60-70"] += occurence
    elif (70 < float(height) < 80):
        modeDataForRange["70-80"] += occurence
modeRange, modeOcc = 0, 0

for range, occurence in modeDataForRange.items():
    if (occurence > modeOcc):
        modeRange, modeOcc = [int(range.split("-")[0]),
                              int(range.split("-")[1])], occurence

mode = float((modeRange[0]+modeRange[1])/2)

print("mode is:", mode)
