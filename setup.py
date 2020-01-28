import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Image-To_Text", # Replace with your own username
    version="0.0.1",
    author="Rajmeet Singh",
    author_email="rajmeetchandok@gmail.com",
    description="Converts Image to Speech",
    url="https://github.com/Rajmeet/Image-to-Speech",
    packages=setuptools.find_packages(),
    keywords = ['cool','OMR Reading', 'Python3'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
      'gtts',
      'pytesseract',
      'open-cv',
  ],
)

