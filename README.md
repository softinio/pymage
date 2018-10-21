# pymagecli

## Overview

I needed a tool to resize images stored in a bucket on Amazon AWS S3 to make
them optimal for web pages.

There are two ways to use this tool:

- As a CLI tool to resize an image or bucket of images stored on S3
- As aws lambda function to resize an image upon upload to S3 (Experimental)

## Install

```
pip install pymagecli
```

## Usage

Use Python Version: 3.6.x (AWS Lambda does not support 3.7.x yet !)

### CLI

See help details:
```
pymagecli --help
```
or 
```
pymagecli <option> --help
```

### AWS Lambda

- For lambda function see handler: `pymagecli/handler.py`
- AWS Docs: [https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)

## Notes
- Before files are resized a copy of the original is made to archive directory
    of the bucket file is located in
- Contributions welcome
- Any questions or issues please open an issue here on Github
- Blog on how to use this pack coming soon follow me: [https://www.softinio.com](https://www.softinio.com)

## To Do
- Write automated tests using Pytest
- Document using lambda handler
- Add more image manipulation and resizing options
