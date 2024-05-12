The aim of this project is to capture every change (insert, and update) from the Mysql table and sync it with Clickhouse.
Transactional Databases like MySQL and PostgreSQL routinely process hundreds of thousands of transactions per second on busy web properties. 
For analyzing those transactions in real-time an analytic database like ClickHouse is a perfect fit as it provides a lot of benefits like columnar storage, efficient data compression and parallel query processing. These benefits translate to cost savings and performance improvements for the end-user.

A lot of organizations need to be able to analyze and visualize the metrics in near real-time on a dashboard. A traditional ETL process runs overnight after the end of the business day and transfers the data from Transactional databases to Analytical Databases. Then aggregation is performed so that the metrics can be visualized in BI tools like Superset, Tableau, and others.
The major drawback with this approach is that decision-makers like C-level executives are not able to visualize metrics in real-time. 

There are several solutions that have been implemented in the real world to solve this problem. I decided to re-implement one of these solutions.

![cdc_with_click_House_Kafka_21a14264f0](https://github.com/saiehhejazi/Data-Engineer-Projects/assets/166489248/c3cc90a7-394f-41ad-803e-cb68d984d6f0)

**Debezium:** (CDC) Change Data Capture is a well established technique to read row-level changes from the database (MySQL). It is usually performed by reading the binary logs which record all the operations and transactions performed in the database. Debezium MySQL source connector can connect to MySQL (primary or secondary) and consume the changes. These changes are then converted to Avro and stored in Kafka.

**Kafka Connect:** Kafka connect framework is an extension of Kafka which provides a good abstraction layer for the data that is received from the source database. With the built-in converter functionality, the source connectors convert the data received from the source database to a unified Kafka connect data schema. This makes it easier to develop the sink connector as the sink only needs to transform the Kafka connect data schema to the destination sink data type.

**ClickHouse** is a high-performance, column-oriented SQL database management system (DBMS) for online analytical processing (OLAP). It is available as both an open-source software and a cloud offering.
