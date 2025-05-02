
# ✅ Manual Test Plan: Real-Time Data Ingestion Using Spark Structured Streaming & PostgreSQL

This document outlines manual test cases to verify each component of the system. For each test, record the actual outcome and compare it with the expected result.

---

## 🧪 Test Cases

### 1. **Test Data Generation**

| Test ID | Description                              | Expected Outcome                                    | Actual Outcome |
|---------|------------------------------------------|----------------------------------------------------|----------------|
| T1      | Run `data_generator.py`                  | A new CSV file is generated every 5 seconds        |                |
| T2      | Check CSV file content                   | CSV file contains 50 well-formatted event records  |                |

---

### 2. **Test Spark Streaming File Detection**

| Test ID | Description                              | Expected Outcome                                  | Actual Outcome |
|---------|------------------------------------------|--------------------------------------------------|----------------|
| T3      | Run `spark_streaming_to_postgres.py`     | Spark detects new CSV files in the input folder  |                |
| T4      | Submit a new CSV manually                | File is picked up and processed by Spark         |                |

---

### 3. **Test Data Transformation and Schema**

| Test ID | Description                              | Expected Outcome                                  | Actual Outcome |
|---------|------------------------------------------|--------------------------------------------------|----------------|
| T5      | Check schema mapping                     | All fields have correct data types in Spark      |                |
| T6      | Missing column in CSV                    | Spark throws a schema mismatch error             |                |

---

### 4. **Test PostgreSQL Integration**

| Test ID | Description                              | Expected Outcome                                        | Actual Outcome |
|---------|------------------------------------------|--------------------------------------------------------|----------------|
| T7      | Check DB insert                          | Events from CSV are inserted into `ecommerce_events`   |                |
| T8      | Insert duplicate `event_id`              | Duplicate is inserted or error (depends on schema)     |                |

---

### 5. **Test End-to-End Functionality**

| Test ID | Description                              | Expected Outcome                                  | Actual Outcome |
|---------|------------------------------------------|--------------------------------------------------|----------------|
| T9      | Run entire pipeline                      | All components interact seamlessly               |                |
| T10     | Query PostgreSQL                         | Real-time records are visible in the database     |                |

---

## 📌 Notes

- Fill in the **Actual Outcome** column during testing.
- Use the Spark UI to monitor job activity and verify micro-batch execution.
- For better reproducibility, keep logs or screenshots of test results.

