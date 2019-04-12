# JadQ

This is a tool to run docker images with arguments provided by `faktory`
queue.

This is mostly based on the example code provided here [1]

## Context

I had to process a large number of satellite images cheaply, so I decided
the best approach was to rent high spec preemptible instances.

This was written to ensure they could be ran and be recovered from if my
machines where to be killed.

## License

MIT.

## References

* [1] https://www.mikeperham.com/2019/01/08/using-faktory-with-python/
