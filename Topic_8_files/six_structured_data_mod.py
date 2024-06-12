str_intf = """Port      Name  Status       Vlan  Duplex Speed Type 
Gi0/1/0         connected   1     auto   auto  10/100/1000BaseTX
Gi0/1/1         connected   1     half-duplex   100  10/100/1000BaseTX
Gi0/1/2         notconnect   1     full-duplex   1000  10/100/1000BaseTX
Gi0/1/3         notconnect   1     auto   auto  10/100/1000BaseTX"""

list_intf = ["Gi0/1/0", "Gi0/1/1", "Gi0/1/2", "Gi0/1/3"]

dict_intf = {
    "Gi0/1/0": "connected",
    "Gi0/1/1": "connected",
    "Gi0/1/2": "notconnect",
    "Gi0/1/3": "notconnect",
}

list_of_lists = [
    ["PORT_NAME", "STATUS", "VLAN", "DUPLEX", "SPEED", "TYPE"],
    ["Gi0/1/0", "connected", "1", "auto", "auto", "10/100/1000BaseTX"],
    ["Gi0/1/1", "connected", "1", "half-duplex", "100", "10/100/1000BaseTX"],
    ["Gi0/1/2", "notconnect", "1", "full-duplex", "1000", "10/100/1000BaseTX"],
    ["Gi0/1/3", "notconnect", "1", "auto", "auto", "10/100/1000BaseTX"],
]

dict_of_lists = {
    "Gi0/1/0": ["connected", "1", "auto", "auto", "10/100/1000BaseTX"],
    "Gi0/1/1": ["connected", "1", "half-duplex", "100", "10/100/1000BaseTX"],
    "Gi0/1/2": ["notconnect", "1", "full-duplex", "1000", "10/100/1000BaseTX"],
    "Gi0/1/3": ["notconnect", "1", "auto", "auto", "10/100/1000BaseTX"],
}

dict_of_dicts = {
    "Gi0/1/0": {
        "STATUS": "connected",
        "VLAN": "1",
        "DUPLEX": "auto",
        "SPEED": "auto",
        "TYPE": "10/100/1000BaseTX",
    },
    "Gi0/1/1": {
        "STATUS": "connected",
        "VLAN": "1",
        "DUPLEX": "half-duplex",
        "SPEED": "100",
        "TYPE": "10/100/1000BaseTX",
    },
    "Gi0/1/2": {
        "STATUS": "notconnect",
        "VLAN": "1",
        "DUPLEX": "full-duplex",
        "SPEED": "1000",
        "TYPE": "10/100/1000BaseTX",
    },
    "Gi0/1/3": {
        "STATUS": "notconnect",
        "VLAN": "1",
        "DUPLEX": "auto",
        "SPEED": "auto",
        "TYPE": "10/100/1000BaseTX",
    },
}
