from faktory import Worker

import time
import logging
import docker
import multiprocessing
import argparse

logging.basicConfig(level=logging.INFO)

time.sleep(1)

def docker_runner(image, arguments):
    logging.info("starting {} with {}".format(image, arguments))
    client = docker.from_env()
    client.containers.run(image, arguments, auto_remove=True)

def main(faktory_url='tcp://localhost:7419', queues=['default'], concurrency=1):
    logging.info('Faktory Instance: {}'.format(faktory_url))
    logging.info('Concurrency: {}'.format(concurrency))
    logging.info('Queues: {}'.format(queues))
    w = Worker(
        faktory=faktory_url,
        queues=queues,
        concurrency=concurrency
    )
    w.register('docker', docker_runner)
    w.run()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Docker job runner')
    parser.add_argument(
        '--url',
        nargs='?',
        default='tcp://localhost:7419',
        help='Faktory Instance to connect to'
    )
    parser.add_argument(
        '--cores',
        nargs='?',
        type=int,
        default=multiprocessing.cpu_count(),
        help='How many instances to run in parallel [default is cpu cores]')
    args = parser.parse_args()
    main(
        faktory_url=args.url,
        concurrency=args.cores
    )
