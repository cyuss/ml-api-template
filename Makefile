# Makefile

docker_image_name = "template"
docker_container_name = "api_template"
version = 0.1.0
port = 8000

start:
	poetry run uvicorn app.main:app --reload --workers 2
test:
	poetry run pytest
coverage:
	poetry run pytest --cov=./app
reqs:
	poetry export --without-hashes -f requirements.txt -o requirements.txt
build_docker:
	docker image build -t $(docker_image_name):$(version) .
run_docker:
	docker container run --name $(docker_container_name) -p $(port):$(port) $(docker_image_name):$(version)
clean_docker:
	docker container stop $(docker_container_name)
	docker rm -f $(docker_container_name)