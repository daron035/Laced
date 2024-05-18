up:
	docker compose -f docker-compose.yaml up -d --build
down:
	docker compose -f docker-compose.yaml down && docker network prune --force
stop:
	docker compose -f docker-compose.yaml stop
test:
	docker compose -f docker-compose.yaml exec web pytest .
