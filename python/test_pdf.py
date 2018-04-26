#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import PyPDF2

# pdfFileObj = open('JavaEE.pdf', 'rb')      存图片的pdf，无法获取文本
# 读取pdf
pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# pdfReader.decrypt('password')
print(pdfReader.numPages)
pageObj = pdfReader.getPage(3)
print(pageObj.extractText())

# 写PDF
pdfWriter = PyPDF2.PdfFileWriter()
# pdfWriter.encrypt('password')
for pageNum in range(0, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open('out_pdf.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
