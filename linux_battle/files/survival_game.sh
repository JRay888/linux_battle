#!/bin/bash

SERVER_NAME=$(hostname)
LOG_FILE="/var/log/linux_battle.log"
LEADERBOARD_SCRIPT="/usr/local/bin/leaderboard.py"

# System Metrics
UPTIME=$(awk '{print $1}' /proc/uptime)
CPU_LOAD=$(awk '{print $1}' < /proc/loadavg)
MEMORY_FREE=$(free -m | awk '/Mem:/ {print $4}')

# Random Events
EVENTS=(
    "Nothing happened, you're safe!"
    "A wild memory leak appeared! -10% memory"
    "CPU is overheating! Load +20%"
    "Disk errors detected! System is slowing down..."
)

RANDOM_EVENT=${EVENTS[$RANDOM % ${#EVENTS[@]}]}

# Apply event effects
if [[ "$RANDOM_EVENT" == *"memory"* ]]; then
    MEMORY_FREE=$((MEMORY_FREE - (MEMORY_FREE / 10)))
elif [[ "$RANDOM_EVENT" == *"CPU"* ]]; then
    CPU_LOAD=$(echo "$CPU_LOAD + 0.2" | bc)
fi

# Log Results
echo "$(date) | $SERVER_NAME | Uptime: $UPTIME sec | CPU Load: $CPU_LOAD | Free Memory: $MEMORY_FREE MB | Event: $RANDOM_EVENT" >> "$LOG_FILE"

# Update Leaderboard
python3 "$LEADERBOARD_SCRIPT"
