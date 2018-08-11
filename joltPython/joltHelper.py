
# =============================================================================
# This fucntion will process and reverse transformation a Json object KEYS into a  
# different Json obect based on the Mapper
#
# @parameter: inputJson- json to be transfrom
# @parameter: joltMap- ref of mapper file
# @return : resultJsonObject - Transformed Json Object Data
# =============================================================================      
def reverseProcessJsonObject(inputJson, joltMap):
    resultantItem = {}    
    flattenJson = flattenDict(inputJson)
    
    for jsondictKey, jsondictVal in flattenJson.items():
        replaced = False
        for k, v in joltMap.items():
            if(jsondictKey==v):
                replaced = True
                resultantItem[k] = jsondictVal
                break
            
        if not replaced:
            resultantItem[jsondictKey] = jsondictVal
            
    return resultantItem

# =============================================================================================
# This python recursive function flattens a JSON file or a dictionary with nested
# lists and/or dictionaries. The output is a flattened dictionary that use dot-chained 
# names for keys, based on the dictionary structure. This allows for reconstructing 
# the JSON structure or converting it to other formats without loosing any structural 
# information.
# 
# @parameter: jsonDict- json to be flatten
# @parameter: result- OPTIONAL, the resultant param if we want to join 2 dict
# @return : resultJA - Transformed flatten Json Object Data with dot-chained names for keys
# =============================================================================================

def flattenDict(jsonDict, result=None):
    if result is None:
        result = {}
        
    for key in jsonDict:
        value = jsonDict[key]
        
        if isinstance(value, dict):
            nestedDict = {}
            for keyIn in value:
#               create newkey by- ".".join([key,keyIn])
                nestedDict[".".join([key,keyIn])]=value[keyIn]
            flattenDict(nestedDict, result)
        elif isinstance(value, (list, tuple)):   
            for indexB, element in enumerate(value):
                if isinstance(element, dict):
                    nestedSet = {}
                    index = 0
                    for keyIn in element:
                        keyIndex = ".[" + str(index) + "]."
                        nestedSet[keyIndex.join([key,keyIn])]=value[indexB][keyIn]
                        index += 1
                    for keyA in nestedSet:
                        flattenDict(nestedSet, result)   
        else:
            result[key]=value
    return result
