import faktory
import random
import time

time.sleep(1)

with faktory.connection(faktory='tcp://:some_password@localhost:7419') as client:
    while True:
        client.queue('docker', args=('ubuntu:latest', 'echo "hello world"'))
        time.sleep(1)
