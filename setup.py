from setuptools import setup, find_packages

setup(
    name="shamsi_datetime",
    version="0.1.0",
    description="A Shamsi (Jalali) datetime class for NumPy integration",
    author="Ali Razmjooei",
    author_email="alirazmjooei.webdeveloper@gmail.com",
    packages=find_packages(),
    license="MIT",
    install_requires=["numpy", "jdatetime"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
