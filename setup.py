__version__ = '0.1.0'

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="cdisc_library_client",
    version=__version__,
    author="CDISC",
    author_email="nhaydel@cdisc.org",
    description="A CDISC Library client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(include=["cdisc_library_client, cdisc_library_client.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.22.0",
    ],
    include_package_data=True,
)