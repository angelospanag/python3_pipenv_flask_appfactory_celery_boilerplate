.PHONY: run

run:
	@honcho start -f Procfile

lint:
	flake8 app --max-complexity 10
