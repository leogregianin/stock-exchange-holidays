lint:
	flake8 .

test:
	coverage run -m unittest && coverage report -m
