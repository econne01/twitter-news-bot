# Serverless Deploy
Follow [hackernoon
tutorial](https://hackernoon.com/creating-serverless-functions-with-python-and-aws-lambda-901d202d45dc)

## Setup
Deploying a python package with serverless can be done with a plugin, but it requires Docker.
[install Docker](https://docs.docker.com/install/)

## Credentials
Some of my computers have a file at `~/.aws/credentials`. To use the named profile for serverless execute
commands with the `AWS_PROFILE` flag like

  AWS_PROFILE=personal-serverless serverless {command}

or

  export AWS_PROFILE=personal-serverless


