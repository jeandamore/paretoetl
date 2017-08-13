export HOMEBREW_NO_AUTO_UPDATE=1 
set -e
brew install python
pip install virtualenv
virtualenv .
pushd bin
source activate
popd
pip install petl
pip install numpy
pushd src
python -m unittest pareto_etl_test
python $1.py $2
popd