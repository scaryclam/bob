#!/usr/bin/env python

from job_runner.runner import Runner


def run():
    runner = Runner()
    runner.start()


if __name__ == '__main__':
    run()
