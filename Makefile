.PHONY: clean
clean:
	find . -iname '*.pyc' -delete
	find . -iname '__pycache__' -delete

.PHONY: test
test:
	nosetests
