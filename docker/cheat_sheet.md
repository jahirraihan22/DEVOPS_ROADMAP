
## removing cache docker compose

    docker-compose -f docker-compose.yml build --force-rm --no-cache && docker-compose -f docker-compose.yml up
