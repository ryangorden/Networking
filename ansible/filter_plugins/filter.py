import json
import xmltodict

class FilterModule:
    '''
    This class is to convert xml to json
    '''
    def filters(self):
        return {
                'convertXml': FilterModule.convertXml
               }
    
    @staticmethod
    def convertXml(xmlString):
        '''
        takes in an xml string and converts it to a json output
        and use the json module to clean up the spacing
        '''
        jsonString = json.dumps(xmltodict.parse(xmlString),indent= 2)
        return jsonString