__version__ = '0.1.6'

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
    url="https://github.com/cdisc-org/cdisc-library-client",
    packages=["cdisc_library_client"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests>=2.22.0",
    ],
    include_package_data=True,
)
