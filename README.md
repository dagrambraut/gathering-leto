[![GitHub Actions](https://github.com/equinor/gathering-leto/workflows/python_code_style/badge.svg)](https://github.com/features/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)

# The Gathering of Leto

Part of the team challenges during SI Gathering 2020. A wonderful demonstration of an app that explores Github issues and just might work perfectly for someone out there, somewhere.

## Table of contents

- [Technologies](#technologies)
- [Components](#components)
- [Security](#security)
- [Development](#development)
- [Feedback](#feedback)
- [Team Members](#team-members)

## Technologies

- [dash](https://plotly.com/dash/)  
  Dash empowers teams to build data science and ML apps that put the power of Python, R, and Julia in the hands of business users. Full-stack apps that would typically require a front end, back end, and DevOps team can now be built and deployed in hours by data scientists with Dash.

- [Docker](https://www.docker.com/)  
  For hosting the web app anywhere and to run local development environments. To quickly get up to speed with docker then run through the [Learn Docker & Containers using Interactive Browser-Based Scenarios](https://www.katacoda.com/courses/docker) at katacoda.  

- [Omnia Radix](https://www.radix.equinor.com/)  
  CICD and hosting of apps in docker containers.


### CICD

- [Docker](https://www.docker.com/)  
  We use multistage dockerfiles to build the images.
  `docker-compose` is used for development purposes only.

- [Omnia Radix](https://www.radix.equinor.com/)  
  CICD and hosting in the [playground](https://console.playground.radix.equinor.com/applications/gathering-leto) environment.
  Radix configuration is mainly handled in [`radixconfig.yaml`](./radixconfig.yaml)


## Components

### server 
A Dash app, which is a form of web server.


## Security

- **Network**
  - _What:_ https
  - _Where:_
    - Internet facing app use TLS cert managed by Radix
    - Local dev app has no certs (http)

- **CICD**
  - _What:_ Radix Playground
  - _Where:_ https://console.playground.radix.equinor.com/applications/gathering-leto
  - _Who:_ AZ AD group [`Radix Playground Users (`4b8ec60e-714c-4a9d-8e0a-3e4cfb3c3d31`)](https://portal.azure.com/#blade/Microsoft_AAD_IAM/GroupDetailsMenuBlade/Overview/groupId/4b8ec60e-714c-4a9d-8e0a-3e4cfb3c3d31/adminUnitObjectId/)

- **Hosting**
  - _What:_ Radix Playground
  - _Where:_
    - [Production](https://gathering-leto.app.playground.radix.equinor.com/), (git branch `release`)
    - [Development](https://server-gathering-leto-development.playground.radix.equinor.com/), (git branch `master`)
  - _Who:_ See "CICD/Who"

- **Docker**
  - _What:_  Release image does not have root privilieges
  - _Where:_ 
    - [Dockerfile](./Dockerfile) , release image


## Development

### How we work

Trunk based development and a [Kanban board](https://github.com/equinor/gathering-leto/projects/2), peer programming, mob rebasing and code review. 

1. Pick an issue/feature
1. Create a feature branch and start hacking
1. When done hacking, run pull request and code review
1. If review ok then merge into master, this will kick off CICD for development in Radix

## Feedback
Did you spot a bug?
Do you want to suggest a new feature?
Do you have a question?

Feel free to create a new issue under [`Issues`](https://github.com/equinor/gathering-leto/issues)!

Try to describe the best you can the issue that arose.
Remember that we always need your help in order to reproduce bugs!

## Contributing guidelines

First of all, thank you for even considering contributing to this
repository! We are honored :tada: Below, you can find some advide and hints
regarding the expectations towards pull requests.

##### Communicate intent early

To align and discuss your ideas we encourage you to communicate your intent as
early as possible. Both in the format of an issue describing what you would
like to solve, but also by creating early pull requests where on can discuss an
implementation.

##### Git usage

We strive to keep a consistent and clean git history and in general:
- all tests should pass on all commits,
- a commit should do one atomic change on the repository and
- the commit message should be descriptive.

For more on commit messages, read [this](https://chris.beams.io/posts/git-commit/).

##### Code formatting

We use [black](https://black.readthedocs.io/en/stable/), the uncompromising
Python code formatter, to format our code. In particular it runs as part of our
code style CI. It can be installed locally by `pip install black`. For an
updated instruction on how to run black we refer you to the `black` section of
our [code style workflow](.github/worflows/code_style.yml)

###### Code validation

We use [flake8](https://flake8.pycqa.org/en/latest/) as a code style tool in
our CI pipeline. It can be installed locally by `pip install flake8`. For an
updated instruction on how to run black we refer you to the `flake8` section of
our [code style workflow](.github/worflows/code_style.yml)


## Build and run release image

The [`./Dockerfile`](./Dockerfile) is a multistage build that will produce a minimal release image.


```sh
docker build -t gathering-leto-release .
docker run -it --rm -p 8000:8000 --name gathering-leto-release gathering-leto-release

# You should now be able to access the web app from the host computer at http://localhost:8000/
# Note that https is not available as there is no tls cert. Cert termination will be handled automatically by the host loadbalancer, in our case Radix.

# Inspect contents
docker exec -it gathering-leto-release sh
```


## Team Members
* Alena Chaikouskaya
* Anette Uttisrud
* Dag Rambraut
* Jonas Peter Sørensen
* Julius Parulek
* Markus Fanebust Dregi
