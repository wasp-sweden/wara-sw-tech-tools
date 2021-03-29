#!/bin/bash

function stop_benchmark() {
    echo [benchmark] stopping...
    sleep 2
    echo [benchmark] stopped
    exit 1
}

trap stop_benchmark term

UNIT=500

echo [benchmark] $$ running...
i=$(expr $UNIT \* 20)
while [ $i != 0 ]; do
    i=$(expr $i - 1)
    if [ $(expr $i % $UNIT) == 0 ]; then
        echo [benchmark] $i...
    fi
done
echo [benchmark] complete!
