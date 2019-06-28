isort:
	sh -c "isort --skip-glob=.tox --recursive ./src/collective/frontpage/"

install:
	virtualenv --python=python2.7 .
	./bin/pip install -r requirements.txt

compile:
	lessc --compress ./src/collective/frontpage/browser/static/frontpage.less ./src/collective/frontpage/browser/static/frontpage-compiled-$(shell date --iso=date).css
