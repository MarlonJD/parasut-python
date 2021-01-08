import setuptools
from parasut.version import Version

setuptools.setup(name='parasut-python',
                 version=Version('0.0.56').number,
                 description='Parasut API Python Wrapper',
                 long_description=open('README.md').read().strip(),
                 long_description_content_type="text/markdown",
                 author='Burak Karahan',
                 author_email='burak.karahan@mail.ru',
                 url='https://github.com/marlonjd/parasut-python',
                 packages=setuptools.find_packages(include=['parasut']),
                 zip_safe=False,
                 keywords='parasut python api',
                 install_requires=[
                     'pytest>=6.2.1', 'pytest-cov>=2.10.1', 'requests_oauthlib>=1.3.0'
                 ],
                 classifiers=[
                     "Programming Language :: Python :: 3",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                 ],
                 python_requires='>=3.6')
