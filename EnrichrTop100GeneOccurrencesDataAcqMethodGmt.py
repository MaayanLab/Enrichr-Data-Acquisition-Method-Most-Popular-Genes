#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 12:24:54 2018

@author: maayanlab
"""

# delete .DS_Store files, obtain list of file names to be read in folder
import os
os.system('find . -name ".DS_Store" -print -delete')
os.system('find . -name ".project" -print -delete')
os.system('find . -name ".pydevproject" -print -delete')
listOfFiles = os.listdir("/Users/maayanlab/Desktop/Megan/top100GenesForEachDataAcquisitionMethod")
listOfFiles.remove("top100GenesDataAcqMethod.py")
listOfFiles.remove("libraryCategories-AMcopy.csv")

resultsFile = open("top100GenesDataAcqMethod.txt", "w")
for file in listOfFiles:
    if not file.endswith(".py"):
        if not file.endswith("top100GenesDataAcqMethod.txt"):
            genelist = list()
            openFile = open(file, "r")
            filefields= file.split("_t")
            method=filefields[0]
            for line in openFile.readlines():
                newLine = line.rstrip()
                fields = newLine.split("\t")
                genes = fields[0]
                genelist.append(genes)
            resultsFile.write(method +'\t'+'\t'.join(genelist)+"\n")
            



# close all opened files 
openFile.close()
resultsFile.close()