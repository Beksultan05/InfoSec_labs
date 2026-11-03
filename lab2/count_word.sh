
#!/bin/bash

count=$(grep -ow "$2" "$1" | wc -l)

echo "Word '$2' appears $count times."
