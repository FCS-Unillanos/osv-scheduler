run-local:
	sudo docker-compose -f docker-compose.local.yml up -d --build

stop-local:
	sudo docker-compose -f docker-compose.local.yml stop

remove-local:
	sudo docker-compose -f docker-compose.local.yml down -v

# example: make create-topic topic=default_topic
create-topic:
	sudo docker-compose exec kafka kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic $topic