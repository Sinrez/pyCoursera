import xml.etree.ElementTree as ET

tree = ET.parse("bill.xml")
root = tree.getroot()

s = 0
for tag in root.findall('products/product'):
    h_value = tag.get('price')
    h_count = tag.get('count')
    total = []
    if h_value is not None:
        total.append(float(h_value)*int(h_count))

    for t in total:
        s += t

print("{0:.2f}".format(s))
