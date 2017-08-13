export HOMEBREW_NO_AUTO_UPDATE=1 
set -e
brew install python
bash -c "python -m ensurepip"
if [ -z "$GO_PIPELINE_NAME" ]; then
	pip install virtualenv
	virtualenv .
	pushd bin
	source activate
	popd
fi
pip install petl
pip install numpy
pushd src

if [ -z "$1" ]; then
	python -m unittest pareto_etl_test
else
	python $1.py $2
fi
popd