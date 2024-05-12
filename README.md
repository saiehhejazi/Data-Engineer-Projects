The aim of this project is to capture every change (insert, and update) from the Mysql table and sync it with Clickhouse.
Transactional Databases like MySQL and PostgreSQL routinely process hundreds of thousands of transactions per second on busy web properties. 
For analyzing those transactions in real-time an analytic database like ClickHouse is a perfect fit as it provides a lot of benefits like columnar storage, efficient data compression and parallel query processing. These benefits translate to cost savings and performance improvements for the end-user.

A lot of organizations need to be able to analyze and visualize the metrics in near real-time on a dashboard. A traditional ETL process runs overnight after the end of the business day and transfers the data from Transactional databases to Analytical Databases. Then aggregation is performed so that the metrics can be visualized in BI tools like Superset, Tableau, and others.
The major drawback with this approach is that decision-makers like C-level executives are not able to visualize metrics in real-time. 

There are several solutions that have been implemented in the real world to solve this problem. I decided to re-implement one of these solutions.
!()

