from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="pyzdsms",
      version="0.0.1",
      description="Libraria para el envio de SMS dentro de Cuba",
      author="Josué Carballo Baños",
      author_email='josuecb@yandex.com',
      license="GPL 3.0",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/MoonMagiCreation/pyzdsms",
      #packages=['enzona_api'],
      packages=find_packages(),
      install_requires=["requests>=2.23.0"],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
      ],
      python_requires='>=3.5',
)
