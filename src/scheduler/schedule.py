#!/usr/bin/env python

import os
import importlib

from schedular.schedular import Schedular
import settings


def run():
    schedular = Schedular()
    schedule = settings.SAMPLE_SCHEDULE
    schedular.start(schedule)


if __name__ == '__main__':
    run()

