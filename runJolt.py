import decimal
import json

from joltPython.joltMapper import JoltMapper

joltMap = JoltMapper("E:\codeBuilds\GitHubRepo\python-json-jolt", 'mapper.json')

with open("sample.json") as json_file:
    sample = json.load(json_file, parse_float = decimal.Decimal)
    print("Sample Data: ",sample)
    
    transData= joltMap.reverseTransformJsonObject(sample)
    print("RESPONSE_LOG: ", transData)
                 
 # Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)
 
