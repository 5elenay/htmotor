from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='htmotor',
    version='1.0.0',
    description='✈️ HTML Template engine for python!',
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    url='https://github.com/5elenay/htmotor/',
    author='5elenay',
    author_email='',
    license='MIT',
    project_urls={
        "Bug Tracker": "https://github.com/5elenay/htmotor/issues",
    },
    classifiers=classifiers,
    keywords=["template", "html", "engine", "template-engine", "view-engine"],
    packages=find_packages(),
    install_requires=[]
)
