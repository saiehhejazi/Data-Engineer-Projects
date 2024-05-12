FROM confluentinc/cp-kafka-connect:7.1.0-1-ubi8
ENV CONNECT_PLUGIN_PATH: "/usr/share/java,/usr/share/confluent-hub-components"
RUN confluent-hub install debezium/debezium-connector-mysql:latest --no-prompt

