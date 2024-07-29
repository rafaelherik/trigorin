#Create the package
cd src
python ./setup.py sdist bdist_wheel

# Install the package
cd ..
pip install src/
