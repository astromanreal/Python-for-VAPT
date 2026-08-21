import xml.etree.ElementTree as ET

tree=ET.parse("scan.xml")

root=tree.getroot()

for host in root.findall("host"):
    address=host.find("address").get("addr")
    print(f"\nHost: {address}")

    ports=host.find("ports")
    for port in ports.findall("port"):
        port_number=port.get("portid")
        service=port.find("service")
        service_name=service.get("name")
        product=service.get("product")
        version=service.get("version")

        print(f"Port: {port_number}")
        print(f"Service: {service_name}")
        print(f"Version: {product} {version}")
        print("-"*20)
