import xml.etree.ElementTree as ET
import shutil
import os

origem = 'C:/Users/Lucas Morita/Desktop/SAT/SAT'
destino = 'C:/Users/Lucas Morita/Desktop/lixo'
for arquivo in os.listdir(origem):
    if not arquivo.endswith('.xml'): continue
    fullname = os.path.join(origem, arquivo)
    try:
        xmldoc = ET.parse(fullname).getroot()
        for child in xmldoc:
            print(child.tag, child.attrib)
    except ET.ParseError:
        print("erro")
        shutil.move(fullname, destino)