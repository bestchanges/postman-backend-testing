pipeline: deploy-local integration-tests-local undeploy-local

venv:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
	echo "Run command '. ./venv/bin/activate' to activate virtualenv"

deploy-local:
	test ! -f local.pid
	python app.py & echo $$! > qa.pid
	sleep 1

undeploy-local:
	kill `cat local.pid` ; rm local.pid

deploy-qa:
	test ! -f qa.pid
	python app.py --port=8810 & echo $$! > qa.pid
	sleep 1

undeploy-qa:
	kill `cat qa.pid` ; rm qa.pid

integration-tests-local:
	(cd tests-postman && make test-local || exit 1)

integration-tests-qa:
	(cd tests-postman && make test-qa || exit 1)

