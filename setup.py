import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-logs",
    version="2.0.1",
    author="Krypton",
    author_email="kkrypt0nn@national.shitposting.agency",
    description="PyLogs is a easy to use python library to let everyone add logs into their python programs easily.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkrypt0nn/PyLogs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    keywords = [
        'pylogs',
        'python logging',
        'logging',
        'python logs'
    ],
    install_requires=[
        'enum'
    ]
)