#!/usr/bin/env python3
import json
import os

LOG_FILE = "/var/log/linux_battle.log"
LEADERBOARD_FILE = "/var/log/leaderboard.json"

servers = {}

# Read logs
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r") as f:
        for line in f:
            parts = line.split(" | ")
            if len(parts) < 5:
                continue
            
            server_name = parts[1]
            uptime = float(parts[2].split(": ")[1].split()[0])
            
            if server_name in servers:
                servers[server_name] = max(servers[server_name], uptime)
            else:
                servers[server_name] = uptime

# Sort leaderboard
sorted_servers = sorted(servers.items(), key=lambda x: x[1], reverse=True)

# Save leaderboard
with open(LEADERBOARD_FILE, "w") as f:
    json.dump(sorted_servers, f, indent=4)

print(f"Leaderboard updated! Check {LEADERBOARD_FILE}")
