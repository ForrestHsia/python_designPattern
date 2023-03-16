import xml.etree.ElementTree as etree, json, os


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

def check_path(filePath):
    if os.path.exists(filePath):
        return filePath
    else:
        return "File Path Not Exist"
    
# 透過介面產生工廠
def main():
    sq3_factory = connect_to(check_path("./testData/test.sq3"))
    print()
    
    xml_factory = connect_to(check_path("./testData/test.sq3.xml"))
    json_factory = connect_to(check_path("./testData/players.json"))
    
    xml_data = xml_factory.parsed_data
    print(xml_data)
    
    json_data = json_factory.parsed_data
    print('found: {} players'.format(len(json_data)))


# 直接手動產生工廠
testJson = JSONConnector("./testData/players.json")
testJsonData = testJson.parsed_data
print(testJsonData)