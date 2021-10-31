#!/usr/bin/env python

import os
import importlib

from schedular import Schedular


def run():
    schedular = Schedular()
    schedular.start()


if __name__ == '__main__':
    run()

