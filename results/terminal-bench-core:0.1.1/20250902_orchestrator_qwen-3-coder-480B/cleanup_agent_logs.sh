#!/bin/bash

# Script to delete all files except conversation_log.json from agent-logs directories

echo "Starting cleanup of agent-logs directories..."

# Find all agent-logs directories and process them
for dir in */*/agent-logs; do
  if [ -d "$dir" ]; then
    echo "Processing $dir"
    find "$dir" -type f ! -name 'conversation_log.json' -delete
  fi
done

echo "Cleanup complete!"