import faktory
import argparse


def main(container, arguments, faktory_url='tcp://localhost:7419'):
    with faktory.connection(faktory=faktory_url) as client:
        client.queue('docker', args=(container, arguments))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Docker job client')
    parser.add_argument(
        '--url',
        nargs='?',
        default='tcp://localhost:7419',
        help='Faktory Instance to connect to'
    )

    parser.add_argument(
        'container',
        help='Container to execute'
    )

    parser.add_argument(
        'arguments',
        nargs='+',
        help='arguments to pass container'
    )


    args=parser.parse_args()

    main(
        args.container,
        args.arguments,
        faktory_url=args.url
    )
