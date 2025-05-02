# Import necessary libraries
import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StringType, TimestampType


# Initialize SparkSession
spark = SparkSession.builder \
    .appName("RealTimeEcommerceEvents") \
    .config("spark.jars", "C:\jars\Sparkpostgresql-42.7.5.jar")  \
    .getOrCreate()


# Define the schema for the incoming data
schema = StructType() \
    .add("event_id", StringType()) \
    .add("user_id", StringType()) \
    .add("product_id", StringType()) \
    .add("product_name", StringType()) \
    .add("event_type", StringType()) \
    .add("event_time", TimestampType())

# Read streaming data
input_path = "../data/steam_data/" # Path to the CSV files
streaming_df = spark.readStream \
    .schema(schema) \
    .option("header", "true") \
    .csv(input_path)

# PostgreSQL connection properties
postgres_url = "jdbc:postgresql://localhost:5432/ecommerce_db"  # Replace with your PostgreSQL URL
postgres_property = {
    "user": "postgres",  # PostgreSQL username
    "password": "password",  # PostgreSQL password
    "driver": "org.postgresql.Driver"
}

# Function to write each micro-batch into PostgreSQL
def write_to_postgres(batch_df, batch_id):
    batch_df.write \
        .jdbc(url=postgres_url, table="ecommerce_events", mode="append", properties=postgres_property)

# Start the streaming query
query = streaming_df.writeStream \
    .foreachBatch(write_to_postgres) \
    .outputMode("append") \
    .option("checkpointLocation", "data/checkpoint/") \
    .start()

query.awaitTermination()
