Orchestration: Apache Airflow with Celery Executor and Redis as the message broker.

Data Source: Reddit API via PRAW (Python Reddit API Wrapper).

Data Processing: Python, Pandas, and NumPy for data transformation.

Storage: Amazon S3 for storing processed CSV files.

Containerization: Docker Compose for managing Airflow, Redis, and PostgreSQL services.

Extraction: Fetches the top 100 daily posts from a specified subreddit using Reddit's API.

Transformation: Processes the data by normalizing fields, converting timestamps, and handling missing values.

Loading: Saves the cleaned data as CSV files and uploads them to an S3 bucket.

Orchestration: Airflow DAGs manage task scheduling, dependencies, and execution.

Apache Airflow: Workflow orchestration and scheduling.

PRAW: Interacting with Reddit's API.

Pandas & NumPy: Data manipulation and transformation.

s3fs: Interfacing with Amazon S3.

Docker & Docker Compose: Containerizing and managing services.

Redis: Message broker for Celery Executor.

PostgreSQL: Metadata database for Airflow
