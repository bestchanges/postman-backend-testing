venv:
	python3 -m venv .venv
	./venv/bin/pip install -r requirements.txt

deploy-qa: venv
	test ! -f qa.pid
	./venv/bin/python app.py --port=8810 & echo $$! > qa.pid
	sleep 2

deploy-stage: venv
	test ! -f stage.pid
	./venv/bin/python app.py --port=8820 & echo $$! > stage.pid
	sleep 2

undeploy-qa:
	kill `cat qa.pid` && rm qa.pid

undeploy-stage:
	kill `cat stage.pid` && rm stage.pid

