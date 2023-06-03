# Test Environment

## Setting Up Bridge Network

```bash
docker network create test-net
docker run -d -t --name py-alpine1 --network test-net python:alpine /bin/sh
docker run -d -t --name py-alpine2 --network test-net python:alpine /bin/sh
docker run -d -t --name py-alpine3 --network test-net python:alpine /bin/sh
tcpdump -i <br-interface>
docker exec -it py-alpine3 /bin/sh
/ # nc -lvp 4444

docker exec -it py-alpine1 /bin/sh
/ # nc 172.18.0.4 4444
test
```

Network information

```json
[
    {
        "Name": "test-net",
        "Id": "05de8ac7bd6309c98787aa788d43e8f72d2f32b2aa79bb983a8c096800887da4",
        "Created": "2023-06-03T09:11:36.091099209-04:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.18.0.0/16",
                    "Gateway": "172.18.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "d03bf1ab006425e0b542a71d33920f4cd5c6066bbe9eb408253c3ac8b997cdd9": {
                "Name": "py-alpine1",
                "EndpointID": "553ad938fd7237b40e0d86ef41ea02a9a648ff4799d81f4d9926065e63af34bc",
                "MacAddress": "02:42:ac:12:00:02",
                "IPv4Address": "172.18.0.2/16",
                "IPv6Address": ""
            },
            "d7d1105004a2c19a6d53466560ce3985477b35d7ee6983e82253f98deac05c5e": {
                "Name": "py-alpine2",
                "EndpointID": "947509a7b040c5e76fecb903178ba9dd8e5433bdf2678fc9c6cb745864226c06",
                "MacAddress": "02:42:ac:12:00:03",
                "IPv4Address": "172.18.0.3/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {}
    }
]
```
