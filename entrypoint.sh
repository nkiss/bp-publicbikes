#!/bin/bash

APP="bp_publicbikes"
LOG_FILE="/var/log/${APP}_run.log"

touch "$LOG_FILE"
chmod 666 "$LOG_FILE"

echo "Run interval is set to ${RUN_INTERVAL}" | tee -a "$LOG_FILE"
echo "$(date) - Running ${APP}..." | tee -a "$LOG_FILE"

python -m $APP >> "$LOG_FILE" 2>&1
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo "$(date) - SUCCESS: ${APP} executed successfully." | tee -a "$LOG_FILE"
else
    echo "$(date) - ERROR: ${APP} failed with exit code $EXIT_CODE." | tee -a "$LOG_FILE"
fi

echo "$(date) - Wait $(($RUN_INTERVAL/60)) minutes for the next run" | tee -a "$LOG_FILE"
sleep $RUN_INTERVAL

exec "$0"  # Restart the script in a loop