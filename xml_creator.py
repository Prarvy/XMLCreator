# Designed by Prakash Srinivasan ( prarvy@gmail.com )
# Project Name: XML Creator
# Version: 1.0: Base version by author

import xml.etree.ElementTree as Et
file_name = 'shop.xml'


root = Et.Element("shop")

category = Et.SubElement(root, "category")
category.set("name", "Vegan Products")

product1 = Et.SubElement(category, "product")
product1.set("name", "Good Morning Sunshine")
type1 = Et.SubElement(product1, "type")
type1.text = "cereals"
producer1 = Et.SubElement(product1, "producer")
producer1.text = "OpenEDG Testing Service"
price1 = Et.SubElement(product1, "price")
price1.text = "9.90"
currency1 = Et.SubElement(product1, "currency")
currency1.text = "USD"

product2 = Et.SubElement(category, "product")
product2.set("name", "Spaghetti Veganietto")
type2 = Et.SubElement(product2, "type")
type2.text = "pasta"
producer2 = Et.SubElement(product2, "producer")
producer2.text = "Programmers Eat Pasta"
price2 = Et.SubElement(product2, "price")
price2.text = "15.49"
currency2 = Et.SubElement(product2, "currency")
currency2.text = "EUR"

product3 = Et.SubElement(category, "product")
product3.set("name", "Fantastic Almond Milk")
type3 = Et.SubElement(product3, "type")
type3.text = "beverages"
producer3 = Et.SubElement(product3, "producer")
producer3.text = "Drinks4Coders Inc."
price3 = Et.SubElement(product3, "price")
price3.text = "19.75"
currency3 = Et.SubElement(product3, "currency")
currency3.text = "USD"

tree = Et.ElementTree(root)
tree.write(file_name, encoding="UTF-8", xml_declaration=True)
print('Created XML file successfully. File Name:', file_name)
