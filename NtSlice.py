import requests

# Create a new network slice
# network slice named "my-network-slice" with two VNFs: "vnf1" and "vnf2
url = "http://onap:8080/api/v1/networkSlices"
payload = {
    "name": "my-network-slice",
    "description": "sample network slice",
    "sliceType": "BASIC",
    "lifecycleState": "ACTIVE",
    "vnfs": [
        {
            "name": "vnf1",
            "vnfType": "NFV_TYPE_VM",
            "vnfVendor": "ACME",
            "vnfVersion": "1.0"
        },
        {
            "name": "vnf2",
            "vnfType": "NFV_TYPE_CaaS",
            "vnfVendor": "XYZ",
            "vnfVersion": "2.0"
        }
    ]
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    print("Network slice created successfully")
else:
    print("Error creating network slice:", response.status_code)
