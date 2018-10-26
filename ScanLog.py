
import os
import json
counts = dict()

for root, dirs, files in os.walk("C:\\Users\\Test\\OneDrive\\Desktop\\AE\\AE\\"):
    i = 0
    listOfTags = []
    for file in files:
        if file.startswith("JobInformation"):
            print(os.path.join(root, file))
            filepath = os.path.join(root, file)
            fo = open(filepath, "r")
            xml = ""
            for line in fo.readlines():
                if "<" in line:
                    xml = xml + line
            import xml.etree.ElementTree as ET
            tree = ET.fromstring(xml)

            f = open(
                "C:\\Users\\Test\\OneDrive\\Desktop\\AE\\AE\\file" + str(i) + ".txt", "w")
            for elem in tree.iter():
                if elem.tag not in listOfTags:
                	if elem.tag in counts:
                		counts[elem.tag] += 1
                	else:
                		counts[elem.tag] = 1
            f.close()
            fo.close()

    print(json.dumps(sorted(counts), indent =2))
