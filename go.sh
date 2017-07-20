brew install python
pip install virtualenv
virtualenv .
pushd bin
source activate
popd
pip install petl
python src/test.py