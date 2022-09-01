<h1 align="center">
   Rank seller - Basic app to add register sales 
</h1>

## :page_with_curl: About
This repository contains an automation environment, written in python, being responsible for receiving message schedules and saving them in a database.

***Python***: The choice was made because it is a simple language and present on any platform. 

***Folder Structure***: The choice for this folder structure was mainly due to the scalability of the system! Trying to modularize the system so that in the future it can integrate more services.

## :scroll: Project Decisions

This project is built to adapt to future projects, such as transforming it into an api or running it in Docker containers using an image that already has python, to facilitate the use of some dependencies.

***The project***: The use of a python one plus make makes the project easier to run.

## :books: Requirements
- Have [**Git**](https://git-scm.com/) to clone the project.
- Have [**Python 3.8**]() to clone the project.

## Environment creation

The Program automatically creates the tables and the database if they do not exist.
For that you only have to inform the data of the database at the beginning of the execution.

## :gear: Installation requirements

To run first we will create a virtual environment to better manage the dependencies.
To do this, just type:
``` bash
   $ make install
```
That way you can create and install the dependencies.
To enter the virtual environment just type:
``` bash
   $ source venv/bin/activate
```

## Run project
``` bash
   # To run the app just type:
   $ make run-worker
```
At the end you will have a service running on terminal.

## Tests

This APP has some unit tests implemented in order to assess possible problems.

To run this test you can run the command below:

```
make coverage
```
<h1></h1>

<p align="center">Rubio Viana</p>