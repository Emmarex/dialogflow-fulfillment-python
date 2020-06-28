import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pydialogflow_fulfillment',  
    version='0.1.4',
    author="Tairu Oluwafemi Emmanuel",
    author_email="developer.emmarex@gmail.com",
    description="This Library makes creating fulfillment for Dialogflow v2 agents with Django or Flask easy and simple",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Emmarex/dialogflow-fulfillment-python",
    download_url="https://github.com/Emmarex/dialogflow-fulfillment-python/archive/0.1.4.tar.gz",
    keywords= ['Dialogflow', 'Dialogflow fulfillment', 'Dialogflow fulfillment v2', 'pydialogflow_fulfillment'],
    packages=setuptools.find_packages(),
    classifiers=[ 
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 6 - Mature",
        "Intended Audience :: Developers",
        "Framework :: Django",
        "Framework :: Flask"
    ],
 )