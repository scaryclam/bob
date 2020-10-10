#!/usr/bin/env python

from job_manager.bob import Bob


def run():
    bob = Bob()
    bob.start()


if __name__ == '__main__':
    run()
