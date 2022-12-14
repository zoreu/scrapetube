try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
from scrapetube import __version__
version = __version__
    
with open("README.md") as f:
    readme = f.read()

with open("requirements.txt") as f:
    requirements = [r.strip() for r in f]


scrapetube_classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
]

setup(name="scrapetube",
    version=version,
    packages=["scrapetube"],
    include_package_data=True,
    author="Cheskel Twersky",
    author_email="twerskycheskel@gmail.com",
    url="https://github.com/zoreu/scrapetube",
    description="Scrape youtube without the official youtube api and without selenium.",
    long_description=readme,
    license="MIT",
    classifiers=scrapetube_classifiers,
    install_requires=requirements,
    python_requires=">=2.7",
    )
