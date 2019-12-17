deploy-qa:
	(cd backend && make deploy-qa)

deploy-stage:
	(cd backend && make deploy-stage)

undeploy-qa:
	(cd backend && make undeploy-qa)

undeploy-stage:
	(cd backend && make undeploy-stage)

integration-tests-qa:
	(cd tests-postman && make test-qa)

pipeline: deploy-qa integration-tests-qa undeploy-qa deploy-stage
