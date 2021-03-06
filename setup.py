from setuptools import setup

setup(
    name='django-redshift',
    version='0.2',
    description='Amazon Redshift Django Backend',
    long_description=open("README.rst").read(),
    author='Matt George',
    author_email='mgeorge@gmail.com',
    license="MIT",
    url='https://github.com/binarydud/django-redshift',
    packages=['django-redshift'],
    install_requires=['psycopg2==2.6.1'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ]
)

