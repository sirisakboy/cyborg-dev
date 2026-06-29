#!/bin/bash

# Load environment variables
set -a
source /home/boy/.pool/.env
set +a

# Run the server
python3 /home/boy/.pool/deploy/main.py