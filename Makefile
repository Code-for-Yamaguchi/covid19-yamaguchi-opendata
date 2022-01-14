.PHONY: upd
upd:
	docker compose up -d --build

.PHONY: exec
exec:
	docker compose run --rm python3 python main.py

.PHONY: sh
sh:
	docker-compose run --rm python3 sh
