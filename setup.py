from setuptools import setup, find_packages

setup(
    name="shamsi_datetime",
    version="0.1.0", 
    description="A Shamsi (Jalali) datetime class for NumPy integration",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ali Razmjooei",
    author_email="your.email@example.com",
    license="MIT",
    packages=find_packages(),
    install_requires=["numpy", "jdatetime"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)