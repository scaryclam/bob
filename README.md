# Bob

Bob is a set of software for scheduling, managing and running jobs.

## Manager

The job manager is for keeping track of jobs. It is responsible for adding jobs
to the execution queue (were a worker picks jobs from), recieving updates,
making jobs that have not updated for a period of time as dead and for persisting
all of the data about jobs to a data store.

## Scheduler

The sceduler stores information about recurring or delayed jobs so that they
can be given to the job manager at predermined times.

## Viewer

This is a simple API that can provide information about the jobs that the jobs
manager is aware of.

## Runner

This is mostly included as an example and does not currently execute processes.
Job runners can and should be written for the task at hand. As they are not dependant
on using Python, just being able to pick jobs up from the execute queue, they
can be written in any language.