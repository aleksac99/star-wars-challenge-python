# Star Wars Challenge

This repository contains code for a Star Wars Challenge app.

This Python app wraps around [Star Wars API](https://swapi.dev/), and its goal is to find people associated with the Star Wars related search term provided by the user.

# Prerequisites

* Python 3.x (Tested using Python 3.12.4)

# Dependencies

* [aiohttp](https://docs.aiohttp.org/en/stable/)

## Dev Dependencies

* [pytest](https://docs.pytest.org/en/stable/)
* [tox](https://tox.wiki/en/4.23.2/)

# Getting Started

1. Clone the repo

```shell
git clone https://github.com/aleksac99/star-wars-challenge-python.git
cd star-wars-challenge
```

(Optional) Create and activate a Virtual Environment

```shell
python -m venv venv
activate
```

2. Install dependencies

```shell
pip install -r requirements/requirements.txt
```

# Running the app

To run the CLI, use:

```shell
python -m sw_challenge
```

# Tests

To run tests, first install dev requirements

```shell
pip install -r requirements/dev.txt
```

The project uses `tox` for test automation. To run test, use the following command:

```shell
tox
```

# Usage

1. Enter a Star Wars-related search term.
2. The CLI displays name, type, and related people of each resource containing the entered term.
3. Enter another term or `q` to close the app.

# High volume environment implementation

The main problem with current solution is high number of SWAPI calls. It's possible to perform the search using SWAPI's `search` parameter, but only one type of resource at the time. To mitigate this, I'd do the following:

1. If I was the service maintainer, I would make it possible to search all resources using a keyword. I would also make it possible to focus on special resource type, using a parameter.
2. I'd implement some sort of result caching on the client side. Current implementation supports caching during app execution, but the data is lost upon exiting.

Additionally, the current app fetches only the first page of each resource. If I required all terms which can be linked to a keyword, I'd have to iterate over all resources.