#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import csv,os

csvFile = open('example.csv')
csvReader = csv.reader(csvFile)
csvData = list(csvReader)
print(csvData)

#第二次遍历csv文件，需要重新open和reader
csvFile2 = open('example.csv')
csvReader2 = csv.reader(csvFile2)
for row in csvReader2:
    print('Row # ' + str(csvReader2.line_num) + '' + str(row))

outFile=open('out.csv','w',newline='')
outWriter=csv.writer(outFile)
# outWriter=csv.writer(outFile,delimiter='\t',lineterminator='\n\n')
outWriter.writerow(['spam','egg','bacon','ham'])
outWriter.writerow(['hello world!','123556','yangyu','charlie'])
outFile.close()

