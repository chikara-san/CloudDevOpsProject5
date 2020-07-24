lint:
	# This is linter for Dockerfiles
	hadolint Dockerfile
	# This should be run from inside a virtualenv
	pylint --disable=R,C,W1203,W1282 src/app.py

