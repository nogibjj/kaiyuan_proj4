install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C *.py

deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 387493768903.dkr.ecr.us-east-1.amazonaws.com
	docker build -t deploy-fastapi .
	docker tag deploy-fastapi:latest 387493768903.dkr.ecr.us-east-1.amazonaws.com/deploy-fastapi:latest
	docker push 387493768903.dkr.ecr.us-east-1.amazonaws.com/deploy-fastapi:latest

all: install format lint deploy