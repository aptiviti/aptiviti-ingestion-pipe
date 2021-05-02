# aptiviti_ingestor

[![Build Status](https://travis-ci.org/aptiviti/aptiviti-ingestion-pipe.svg?branch=main)](https://travis-ci.org/aptiviti/aptiviti-ingestion-pipe)

[![codecov](https://codecov.io/gh/aptiviti/aptiviti-ingestion-pipe/branch/main/graph/badge.svg?token=UFVsUnyfTG)](https://codecov.io/gh/aptiviti/aptiviti-ingestion-pipe)

Library to wrap managed provider with Aptiviti tracking functions to ingest data into data lake. Target OS: Windows 10

## Install as module

`python3 -m pip install aptiviti-ingestion-pipe`

Then you can

`from aptiviti_ingestor import aptiviti_data_ingestor`

## Dependencies

First run

`python3 -m pip install requirements.txt`

before developing locally.

## configuration.py

Create a configuration.py with a single variable containing the workspace write key from Segment.io.

    SEGMENT_WRITE_KEY='yourkeyhere'

Check your password manager for the key.

## Build

Delete the `dist` folder if it already exists.
Don't forget to increment the version number in `setup.py `prior to building.
`python3 .\setup.py bdist_wheel` to create the `dist` folder containing the package build.

## Deploy to pypi

TravisCI is configured to automatically deploy to PyPi when pushing a tag on the Main branch.

Increment the version number `setup.py`.
run `python3 -m twine upload .\dist\*` to upload to pypi. Currently this package is deployed to the `etrintel` pypi account.

You might run into the following error:

    HTTPError: 400 Client Error: File already exists. See https://pypi.org/help/#file-name-reuse for url: https://upload.pypi.org/legacy/

If that happens to you, check up on 2 things:

* Make sure you updated the version number in both files
* Delete the old version files from your dist/ directory