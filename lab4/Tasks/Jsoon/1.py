import json
with open("/Users/ruslanmyrzabaev/Desktop/py/lab4/Tasks/Jsoon/sample_data.json","r") as file:
    data  = json.load(file)
    
print("Interface Status ")
print("="*80)

DN = "DN"
Description = "Description"
Speed = "Speed"
MTU = "MTU"

print(f"{DN:50} {Description:20} {Speed:7} {MTU:7}")
print("-" * 84)

for item in data["imdata"]:
    attr = item["l1PhysIf"]["attributes"]
    dn = attr.get("dn")
    descr = attr.get("speed")
    mtu = attr.get("mtu")
    print(f"{dn:50} {descr:20} {Speed:7} {mtu:7}")