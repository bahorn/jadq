from faktory import Worker

import time
import logging
import docker
import multiprocessing

logging.basicConfig(level=logging.INFO)

time.sleep(1)

def docker_runner(image, arguments):
    logging.info("starting {} with {}".format(image, arguments))
    client = docker.from_env()
    client.containers.run(image, arguments)
    print('done')


def main(faktory_url='tcp://localhost:7419', queues=['default'], concurrency=1):
    logging.info('STARTED')
    w = Worker(
        faktory=faktory_url,
        queues=queues,
        concurrency=concurrency
    )
    w.register('docker', docker_runner)
    w.run()

if __name__ == "__main__":
    cores = multiprocessing.cpu_count()
    main(faktory_url='tcp://:some_password@localhost:7419', concurrency=cores)
