from setuptools import find_packages, setup


setup(
    name="aiohttp_metrics",
    version="0.1.2",
    packages=find_packages(),
    url="https://github.com/clayman74/aiohttp-metrics",
    licence="MIT",
    author="Kirill Sumorokov",
    author_email="sumorokov.k@gmail.com",
    description="Prometheus metrics for aiohttp-based microservices.",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: AsyncIO",
    ],
    keywords="aiohttp-metrics",
    install_requires=["aiohttp", "prometheus_client"],
    extras_require={
        "lint": [
            "flake8",
            "flake8-bugbear",
            "flake8-builtins-unleashed",
            "flake8-comprehensions",
            "flake8-import-order",
            "flake8-pytest",
            "flake8-print",
            "mypy",
            "black",
        ],
        "test": ["coverage", "faker", "pytest", "pytest-aiohttp"],
    },
)
