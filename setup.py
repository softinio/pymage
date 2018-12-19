from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pymagecli",
    version="0.0.7",
    python_requires=">=3.6.*, <=3.7.*",
    author="Salar Rahmanian",
    author_email="code@softinio.com",
    description="A CLI tool and an AWS Lambda handler to resize images on S3",
    long_description="""\
    A CLI tool and an AWS Lambda handler to resize images stored on AWS S3""",
    long_description_content_type="text/markdown",
    url="https://github.com/softinio/pymagecli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Click", "pillow"],
    entry_points="""
        [console_scripts]
        pymagecli=pymagecli.pymagecli:cli
    """,
)
