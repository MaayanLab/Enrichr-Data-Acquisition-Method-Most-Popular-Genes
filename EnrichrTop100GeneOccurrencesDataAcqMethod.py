#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 12:01:08 2018

@author: maayanlab
"""
# get list of files in working directory 
import os
import numpy as np
listOfFiles = os.listdir("/Users/maayanlab/Desktop/Megan/top100GenesForEachDataAcquisitionMethod")
listOfFiles.remove("libraryCategories-AMcopy.csv")
#listOfFiles.remove(".DS_Store")
#listOfFiles.remove(".Rhistory")

#  create dictionary with library name as key and category as value
libraryCategoriesFileOpen = open("libraryCategories-AMcopy.csv", "r", encoding="utf-8")
libraryCategoriesFileLines = libraryCategoriesFileOpen.readlines()
libraryNameCategoryDictionary={}
for line in libraryCategoriesFileLines:
    line = line.rstrip()
    fields = line.split(",")
    libraryName = fields[0]
    category = fields[2]
    libraryNameCategoryDictionary[libraryName]=category
libraryCategoriesFileOpen.close()

# create a list of data acquisition methods
methods = list(np.unique(list(libraryNameCategoryDictionary.values())))
methods.remove('Meta-analysis')
# for each method, create a file with ~top 100 genes and their counts
# for each method, open up corresponding library ~100 top gene count files
# make a dictionary with all genes and their counts
# add counts for genes that occur in more than 1 library 
# sort dictionary and write to file top 100 genes and their corresponding counts for that data acquisiton method
for method in methods:
    methodGeneCountsLibrary={}
    for library, correspondingMethod in libraryNameCategoryDictionary.items():
        if correspondingMethod == method:
            libraryFileName= library+"_results.txt"
            if libraryFileName in listOfFiles:
                resultsFileOpen=open(libraryFileName, "r")
                resultsFileOpenLines=resultsFileOpen.readlines()
                for line in resultsFileOpenLines:
                    line=line.rstrip()
                    fields = line.split("\t")
                    gene = fields[0]
                    count=int(fields[1])
                    if gene in methodGeneCountsLibrary.keys():
                        methodGeneCountsLibrary[gene] += count
                    else:
                        methodGeneCountsLibrary[gene] = int(count)
    if len(methodGeneCountsLibrary) >0:
        highestToLowestGenes = sorted(methodGeneCountsLibrary, key=methodGeneCountsLibrary.get,reverse=True)
        top20genes= highestToLowestGenes[0:100]
        lastFreq= methodGeneCountsLibrary[top20genes[len(top20genes)-1]]
        for x,y in methodGeneCountsLibrary.items():
            if lastFreq==y:
                top20genes.append(x)
        outputFileName= method + "_top_100_genes_.txt"
        outputFileOpen = open(outputFileName,"w")
        print(len(top20genes))
        for gene2 in top20genes:
            outputFileOpen.write(gene2 + "\t" + str(methodGeneCountsLibrary[gene2])+"\n")
    
             
libraryCategoriesFileOpen.close()   
outputFileOpen.close()
