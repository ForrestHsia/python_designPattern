import xml.etree.ElementTree as etree, json

class JSONConnector:
    def __init__(self, filePath):
        self.data = dict()
        with open(filePath, mode="r", encoding="utf-8") as f:
            self.data = json.load(f)
        
    @property
    def parsed_data(self):
        return self.data
    
class XMLConnector:
    def __init__(self, filePath):
        self.tree = etree.parse(filePath)

    @property
    def parsed_data(self):
        return self.tree

def connection_factory(filePath):
    if filePath.endswith('json'):
        connector = JSONConnector
    elif filePath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError("Connection failed: {}".format(filePath))
    return connector(filePath)

def connect_to(filePath):
    factory = None
    try:
        factory = connection_factory(filePath)
    except ValueError as ve:
        print("ErrorMsg:", ve)
    
    return factory

def main():
    sq3_factory = connect_to("../testData/test.sq3")
    xml_factory = connect_to("../testData/test.sq3.xml")
    json_factory = connect_to("../testData/players.json")
    
    xml_data = xml_factory.parsed_data
    print(xml_data)
    
    json_data = json_factory.parsed_data
    print('found: {} Lamigo players'.format(len(json_data)))
    for players in json_data:
        
    

main()