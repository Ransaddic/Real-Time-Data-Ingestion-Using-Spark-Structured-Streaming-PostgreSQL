
# 📦 Real-Time Data Ingestion Using Spark Structured Streaming & PostgreSQL

## Overview

This project simulates a real-time e-commerce user activity tracking system. It demonstrates how to ingest, process, and store continuously arriving data using a robust streaming pipeline built with Apache Spark and PostgreSQL.

---

## 🧱 System Components

### 1. **Data Generator (`data_generator.py`)**
- Simulates fake user events such as product views, clicks, cart additions, and purchases.
- Writes these events to CSV files in a designated folder at regular intervals.
- Helps simulate real-time event streams by generating a new file every few seconds.

### 2. **Spark Structured Streaming Job (`spark_streaming_to_postgres.py`)**
- Monitors the folder for new CSV files using Spark’s Structured Streaming engine.
- Applies a predefined schema and reads the event data as a stream.
- Optionally transforms or validates the data before writing it to the target database.

### 3. **PostgreSQL Database**
- Stores the ingested event data in a relational format.
- Enables querying and analysis of the streamed events using SQL.
- Acts as the sink in the data pipeline.

---

## 🔁 Data Flow

```
[Data Generator] → CSV Files → [Spark Structured Streaming] → [PostgreSQL]
```

1. `data_generator.py` continuously creates event files (e.g., `steam_data_*.csv`).
2. Spark detects and processes these files in near real time using a defined schema.
3. Cleaned and structured data is appended to the `ecommerce_events` table in PostgreSQL.

---

## 🎯 Key Features

- Real-time file-based streaming using Spark.
- Modular Python-based data simulation.
- JDBC-based streaming writes to PostgreSQL.
- Configurable components and schema validation.
- Simple architecture, easy to extend or deploy.

---

## 📌 Use Cases

- Real-time analytics on e-commerce user behavior.
- Prototyping stream processing architectures.
- Learning or teaching streaming ETL with open-source tools.
