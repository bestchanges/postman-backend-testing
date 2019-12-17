deploy-qa:
	test ! -f qa.pid
	python app.py --port=8810 & echo $$! > qa.pid
	sleep 2

deploy-stage:
	test ! -f stage.pid
	python app.py --port=8820 & echo $$! > stage.pid
	sleep 2

undeploy-qa:
	kill `cat qa.pid` ; rm qa.pid

undeploy-stage:
	kill `cat stage.pid` ; rm stage.pid

