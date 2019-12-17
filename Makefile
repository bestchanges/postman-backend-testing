venv:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
	echo "Run command '. ./venv/bin/activate' to activate virtualenv"

deploy-qa:
	(cd backend && make deploy-qa || exit 1)

deploy-stage:
	(cd backend && make deploy-stage || exit 1)

undeploy-qa:
	(cd backend && make undeploy-qa || exit 1)

undeploy-stage:
	(cd backend && make undeploy-stage || exit 1)

integration-tests-qa:
	(cd tests-postman && make test-qa || exit 1)

pipeline: deploy-qa integration-tests-qa undeploy-qa
