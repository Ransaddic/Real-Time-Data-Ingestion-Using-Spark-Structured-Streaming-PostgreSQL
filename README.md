
# 📦 Real-Time Data Ingestion Using Spark Structured Streaming & PostgreSQL

This project demonstrates a real-time data pipeline that simulates e-commerce user activity, streams it using Apache Spark Structured Streaming, and ingests the processed data into a PostgreSQL database.

---

## 🚀 Features

- Simulates real-time e-commerce events (e.g., views, clicks, purchases)
- Processes data using Spark Structured Streaming
- Writes transformed data to PostgreSQL in real time
- Includes performance metrics, test cases, and system architecture documentation

---

## 🗂️ Project Structure

```
project-root/
│
├── data/
│   ├── steam_data/             # Contains generated CSV event files
│   └── checkpoint/             # Spark Structured Streaming checkpointing
│
├── scripts/
│   ├── data_generator.py       # Generates fake e-commerce events as CSV files
│   └── spark_streaming_to_postgres.py  # Spark job to stream and insert data into PostgreSQL
|   |__ postgres_setup.sql      # Postgres setup
|
|
│
├── docs/
│   ├── project_overview.md     # Overview of system architecture and components
│   ├── user_guide.md           # Step-by-step execution instructions
│   ├── test_cases.md           # Manual test plan
│   ├── performance_metrics.md  # Performance report (latency, throughput, etc.)
│   ├── system_architecture.png # Visual diagram of the data pipeline
│   └── postgres_connection_details.txt  # PostgreSQL DB credentials
│
└── README.md                   # This file
```

---

## 🛠️ Setup Instructions

### 1. **Install Requirements**

Ensure the following are installed:
- Python 3.7+
- Apache Spark 3.x
- PostgreSQL 13+
- Java (JDK 8+)
- Required Python packages: `pyspark`, `findspark`, `psycopg2`
- PostgreSQL JDBC driver

### 2. **Configure PostgreSQL**

Run the provided SQL script to create the database and table.

```bash
psql -U postgres -f docs/postgres_setup.sql
```

Update `docs/postgres_connection_details.txt` with your DB credentials.

### 3. **Start Data Generator**

```bash
python scripts/data_generator.py
```

Generates a new CSV file every 5 seconds in `data/steam_data/`.

### 4. **Run Spark Streaming Job**

```bash
spark-submit --jars path/to/Sparkpostgresql-42.7.5.jar scripts/spark_streaming_to_postgres.py
```

Spark monitors the folder and writes new events to PostgreSQL.

---

## ✅ Verification

Check data in PostgreSQL:

```sql
SELECT * FROM ecommerce_events LIMIT 10;
```

Use Spark UI (`http://localhost:4040`) to monitor the job.

---

## 📄 Documentation

All documentation is located in the `docs/` folder:

- System overview and architecture
- Usage guide and setup instructions
- Test plans and performance metrics

---

## 📌 Notes

- Data is checkpointed for fault tolerance in `data/checkpoint/`.
- Adjust data generation frequency and batch size as needed.
- Make sure the JDBC driver path is correct.

