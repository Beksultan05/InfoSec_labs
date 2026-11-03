
#!/bin/bash

hour=$(date +%H)
minute=$(date +%M)

current=$((10#$hour * 60 + 10#$minute))
remaining=$((18 * 60 - current))

echo "Current time: $(date +%H:%M)"

if [ $remaining -gt 0 ]; then
    echo "Work day ends after $((remaining / 60)) hours and $((remaining % 60)) minutes."
else
    echo "Work day has ended."
fi
