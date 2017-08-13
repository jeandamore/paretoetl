export HOMEBREW_NO_AUTO_UPDATE=1 
set -e
brew install python
bash -c "python -m ensurepip"
bash -c "pip install virtualenv"
bash -c "virtualenv ."
pushd bin
source activate
popd
bash -c "pip install petl"
bash -c "pip install numpy"
pushd src
bash -c "python -m unittest pareto_etl_test"
bash -c "python $1.py $2"
popd