
# 🛠️ User Guide: Real-Time Data Ingestion Using Spark Structured Streaming & PostgreSQL

This guide provides step-by-step instructions for running the real-time data ingestion pipeline.

---

## ✅ Prerequisites

Ensure the following are installed and configured on your system:

- Python 3.7+
- Apache Spark 3.x
- PostgreSQL database
- Java (JDK 8 or later)
- PostgreSQL JDBC driver (e.g., `Sparkpostgresql-42.7.5.jar`)
- pip packages: `pyspark`, `findspark`, `psycopg2`, `faker` (optional)

---

## 📁 Project Structure

```
project/
│
├── data_generator.py
├── spark_streaming_to_postgres.py
├── postgres_setup.sql
├── postgres_connection_details.txt
├── project_overview.md
├── user_guide.md
├── performance_metrics.md
├── test_cases.md
├── system_architecture.png
└── data/
    └── steam_data/             # CSV event files will be saved here
```

---

## 🧰 Step-by-Step Instructions

### 1. **Set Up PostgreSQL**

1. Start PostgreSQL server.
2. Run the SQL script to create the database and table:
   ```bash
   psql -U postgres -f postgres_setup.sql
   ```

---

### 2. **Configure Connection Details**

Update `postgres_connection_details.txt` with your DB credentials:
```
host=localhost
port=5432
user=postgres
password=password
```

---

### 3. **Start the Data Generator**

Run the script to simulate and generate event data:
```bash
python data_generator.py
```
- This creates a new CSV file every 5 seconds in the `data/steam_data/` folder.

---

### 4. **Run the Spark Streaming Job**

Run the Spark job that reads and processes the CSV files:
```bash
spark-submit --jars C:/jars/Sparkpostgresql-42.7.5.jar spark_streaming_to_postgres.py
```
- Spark will continuously monitor the folder and insert records into PostgreSQL.

---

### 5. **Verify the Data**

Connect to your PostgreSQL DB and query the table:
```sql
SELECT * FROM ecommerce_events LIMIT 10;
```

---

## 🧼 Stopping the Pipeline

- Use `Ctrl+C` to stop both the generator and Spark streaming job.
- Clean up temporary data if needed (`data/steam_data`, `data/checkpoint/`).

---

## ✅ Tips

- Use the Spark UI (usually at `http://localhost:4040`) to monitor job progress.
- Ensure the JDBC JAR is accessible and compatible with your Spark version.

