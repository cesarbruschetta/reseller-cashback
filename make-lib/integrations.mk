
integration-pipeline-local: poetry-check checks-nosave tests ## Runs all steps for integrating locally or Bitbucket CI

integration-pipeline-docker: poetry-check checks-nosave docker-up ## Runs all steps for integrating in docker
	@sleep 20
	@make tests
	@make docker-down
	@poetry run docker-compose run coverage

poetry-check: safety ## Runs poetry check
	@poetry check

safety:
	@poetry run safety check --full-report -i 37894

docker-up: ## Starts all services on docker-compose as daemon
	@poetry run docker-compose up -d --force-recreate --build

docker-down: ## Stops all services on docker-compose
	@poetry run docker-compose down

docker-up-log: ## Starts all services on docker-compose as foreground
	@poetry run docker-compose up --force-recreate --build

docker-postgres: ## Starts postgres DB docker
	@poetry run docker-compose up -d --force-recreate --build postgres

docker-dependencies: docker-postgres ## Starts All docker dependencies

docker-apps-recreate:
	$(eval $(call check-var,APPS))
	@poetry run docker-compose up --force-recreate --build $(APPS)

wait:
	@sleep 20
