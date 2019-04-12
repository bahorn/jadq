# JadQ

This is a tool to run docker images with arguments provided by `faktory`
queue.

This is mostly based on the example code provided here [1]

## Usage

Make sure you have a faktory instance running somewhere. Check the installation
instructions available here. [2]

Install the python dependencies for these script with:

```
virtualenv -p python3 .venv
. .venv/bin/activate
pip install -r requirements.txt
```

Now you can use the `client/client.py` to add jobs.

Keep `worker/worker.py` running and all your tasks should be executed. By
default, it will run as jobs as there are cores on the machine you are using.

Don't expect any output from your container.

## Context

I had to process a large number of satellite images cheaply, so I decided
the best approach was to rent high spec preemptible instances.

This was written to ensure they could be ran and be recovered from if my
machines where to be killed.

## License

MIT.

## References

* [1] https://www.mikeperham.com/2019/01/08/using-faktory-with-python/
* [2] https://github.com/contribsys/faktory/wiki/Installation
