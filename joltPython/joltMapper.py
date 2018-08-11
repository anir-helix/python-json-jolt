import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import json
import joltHelper

class JoltMapper:
    def __init__(self, joltFileDirPath, joltFileName):
        self.joltFilePathAbs = os.path.join(joltFileDirPath, joltFileName)

# =============================================================================
# This fucntion will transform a Array List of String values into a different 
# Array List of String based on the Mapper
#
# @parameter: inputList- List to be transfrom
# @return : listData - Transformed list Data
# =============================================================================
    def transformList(self, inputList):
        with open(self.joltFilePathAbs) as joltFile:
            joltMap = json.load(joltFile)
        
        listData=[]
        for item in inputList:
            replaced = False
            for key, val in joltMap.items():
                if(item==key):
                    replaced = True
                    transItem = item.replace(key, val)
                    listData.append(transItem)
                    break
            if not replaced:
                listData.append(item)
                
        return listData
            
# =============================================================================
# This fucntion will reverse transformation a Json Array KEYS into a different 
# Json Array based on the Mapper
#
# @parameter: inputJsonArray- List to be transfrom
# @return : resultJA - Transformed Json Array Data
# =============================================================================     
    def reverseTransformJsonArray(self, inputJsonArray):
        with open(self.joltFilePathAbs) as joltFile:
            joltMap = json.load(joltFile)
            
        resultJA=[]
       
        for item in inputJsonArray:  
            resultantObj= joltHelper.reverseProcessJsonObject(item, joltMap)
            if(resultantObj):
                resultJA.append(resultantObj)
        
        return resultJA
    
# =============================================================================
# This fucntion will reverse transformation a Json Object KEYS into a different 
# Json Object based on the Mapper
#
# @parameter: inputJsonArray- List to be transfrom
# @return : resultJA - Transformed Json Object Data
# =============================================================================     
    def reverseTransformJsonObject(self, inputJsonObj):
        with open(self.joltFilePathAbs) as joltFile:
            joltMap = json.load(joltFile)
        
        return joltHelper.reverseProcessJsonObject(inputJsonObj, joltMap)
      
        
