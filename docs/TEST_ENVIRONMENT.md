# Test Environment

The docker compose environment creates 3 containers for generating simple HTTP traffic on a user-defined bridge network.

```bash
docker compose up -d
sudo python3 ./manta_net/main.py
./scripts/generate-traffic.sh
docker compose down
```

This will generate a pcap file in the outputs directory. The pcap file can be opened in wireshark to view the traffic.
