#!/bin/bash

# This script generates traffic to the specified URL.

EXISTING_FILE="existing.txt"
NONEXISTING_FILE="nonexisting.txt"

# Create the file in the container.
docker exec -it hgfs-py-alpine-1 /bin/sh -c "echo 'hello world' > /$EXISTING_FILE.txt"
docker exec -it hgfs-py-alpine-2 /bin/sh -c "echo 'hello world' > /$EXISTING_FILE.txt"
docker exec -it hgfs-py-alpine-3 /bin/sh -c "echo 'hello world' > /$EXISTING_FILE.txt"

# Generate HTTP traffic to the existing file.
docker exec -it hgfs-py-alpine-1 /bin/sh -c "wget http://hgfs-py-alpine-2:8000/$EXISTING_FILE.txt"
docker exec -it hgfs-py-alpine-1 /bin/sh -c "wget http://hgfs-py-alpine-3:8000/$EXISTING_FILE.txt"
docker exec -it hgfs-py-alpine-2 /bin/sh -c "wget http://hgfs-py-alpine-3:8000/$EXISTING_FILE.txt"
docker exec -it hgfs-py-alpine-2 /bin/sh -c "wget http://hgfs-py-alpine-1:8000/$EXISTING_FILE.txt"
docker exec -it hgfs-py-alpine-3 /bin/sh -c "wget http://hgfs-py-alpine-1:8000/$EXISTING_FILE.txt"
docker exec -it hgfs-py-alpine-3 /bin/sh -c "wget http://hgfs-py-alpine-2:8000/$EXISTING_FILE.txt"

# Generate HTTP traffic to the non-existing file.
docker exec -it hgfs-py-alpine-1 /bin/sh -c "wget http://hgfs-py-alpine-2:8000/$NONEXISTING_FILE.txt"
docker exec -it hgfs-py-alpine-1 /bin/sh -c "wget http://hgfs-py-alpine-3:8000/$NONEXISTING_FILE.txt"
docker exec -it hgfs-py-alpine-2 /bin/sh -c "wget http://hgfs-py-alpine-3:8000/$NONEXISTING_FILE.txt"
docker exec -it hgfs-py-alpine-2 /bin/sh -c "wget http://hgfs-py-alpine-1:8000/$NONEXISTING_FILE.txt"
docker exec -it hgfs-py-alpine-3 /bin/sh -c "wget http://hgfs-py-alpine-1:8000/$NONEXISTING_FILE.txt"
docker exec -it hgfs-py-alpine-3 /bin/sh -c "wget http://hgfs-py-alpine-2:8000/$NONEXISTING_FILE.txt"
