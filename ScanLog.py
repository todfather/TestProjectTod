import os
for root, dirs, files in os.walk("C:\\Users\\todfa\\OneDrive\\Desktop\\AE\\AE\\"):
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
        tree = ET.parse(xml)
        #root = tree.getroot()
        print(root)
        print("----------------------------------------------------")
        fo.close()
        

      


