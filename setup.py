import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dialogflow_fulfillment',  
    version='0.0.1',
    author="Tairu Oluwafemi Emmanuel",
    author_email="developer.emmarex@gmail.com",
    description="This Libray makes creating fulfillment for Dialogflow v2 agents with Django or Flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Emmarex/dialogflow-fulfillment-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha"
        "Operating System :: OS Independent",
     ],
 )