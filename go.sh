brew install python
pip install virtualenv
virtualenv .
pushd bin
source activate
popd
pip install petl
pushd src
python -m unittest paretoetl_test
python test.py
popd
