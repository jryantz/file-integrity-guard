# File Integrity Guard

[![build & test](https://github.com/jryantz/file-integrity-guard/actions/workflows/python-app.yml/badge.svg)](https://github.com/jryantz/file-integrity-guard/actions/workflows/python-app.yml)
[![](https://img.shields.io/github/repo-size/jryantz/file-integrity-guard)](https://github.com/jryantz/file-integrity-guard)
[![](https://img.shields.io/github/license/jryantz/file-integrity-guard)](https://github.com/jryantz/file-integrity-guard/blob/main/LICENSE)

## Requirements

File Integrity Guard requires Python 3.10.

Python package requirements are documented in [`requirements.txt`](/requirements.txt).

## Installation

### Windows

1. Create a virtual environment: `python -m venv env`
1. Activate the environment: `env/Scripts/activate`
1. Install requirements: `pip install -r requirements.txt`

### Mac

1. Create a virtual environment: `python3 -m venv env`
1. Activate the environment: `source env/bin/activate`
1. Install requirements: `pip install -r requirements.txt`

## Usage

### Windows

Execute the following command from the folder containing the application.

```
$ python -m guardian
```

### Mac

Execute the following command from the directory containing the application.

```
$ python3 -m guardian
```
