import findspark #pyspark can't be detected if file is at other folders than where it is installed
findspark.init('/home/jake/spark/spark-2.2.0-bin-hadoop2.7')

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Basics").getOrCreate() #appName can be anything

## READING
#----------------------------
df = spark.read.json('people.json')
df = spark.read.csv('appl_stock.csv', inferSchema=True, header=True)
df.show()

df.head() #shows a list of row objects
# [Row(age=None, name='Michael'), Row(age=30, name='Andy')]


## BASICS
#--------------------------------------------------------
df[:10].collect() #collect the result instead of showing
row.asDict() #produce as dictionary


## SCHEMA
#--------------------------------------------------------
#changing the schema
from pyspark.sql.types import StructField,StringType,IntegerType,StructType
data_schema = [StructField("age", IntegerType(), True),StructField("name", StringType(), True)]
final_struc = StructType(fields=data_schema)
df = spark.read.json('people.json', schema=final_struc)

df.printSchema()

# FORMAT DECIMAL PLACES
sales_std.select(format_number('std',2)).show()



## EXPLORATORY
#--------------------------------------------------------
df.describe() #show datatypes
df.describe().show() #show max, min, stdev


## COLUMNS
#--------------------------------------------------------
df.columns #show column names
df.select('age').show() #have to use select to choose entire column
df.select(['age','name']).show() #multiple columns


# NEW COLUMNS
# Adding a new column with a simple copy
df.withColumn('newage',df['age']).show()
df.withColumn('add_one_age',df['age']+1).show() #with calculation


# RENAME COLUMN
df.withColumnRenamed('age','supernewage').show()



## SQL
#--------------------------------------------------------
# Register the DataFrame as a SQL temporary view
df.createOrReplaceTempView("people")
spark.sql("SELECT * FROM people WHERE age=30").show()


# ORDER BY
df.orderBy("Sales").show() #ascending
df.orderBy(df["Sales"].desc()).show() #descending


## NULL VALUES
#--------------------------------------------------------
# DROP NAN
# Drop any row that contains missing data
df.na.drop().show()
# Has to have at least 2 NON-null values in a row
df.na.drop(thresh=2).show()
# rows in Sales that have null
df.na.drop(subset=["Sales"]).show()
# rows that have any nulls
df.na.drop(how='any').show()
# rows that have all nulls
df.na.drop(how='all').show()


# FILL NAN
# Spark is actually smart enough to match up & fill the data types.
# only fill in strings
df.na.fill('NEW VALUE').show()
# only fill in numeric
df.na.fill(0).show()
# fill in specific column
df.na.fill('No Name',subset=['Name']).show()


# fill in values with mean
df.na.fill(df.select(mean(df['Sales'])).collect()[0][0],['Sales']).show()


## FILTERING
#--------------------------------------------------------
df.filter("Close < 500").show() #SQL synatx
df.filter(df["Close"] < 500).show() #Python synatx

df.filter("Close<500").select(['Open','Close']).show()

#Multiple conditions
df.filter( (df["Close"] < 200) & (df['Open'] > 200) ).show() #AND &
df.filter( (df["Close"] < 200) | (df['Open'] > 200) ).show() #OR |
df.filter( (df["Close"] < 200) & ~(df['Open'] < 200) ).show() #NOT ~

df.filter(df["Low"] == 197.16).show()


## AGGREGATE
#--------------------------------------------------------
df.groupBy("Company").mean().show() #Mean
df.groupBy("Company").count().show() #Count
df.groupBy("Company").max().show() #Max
df.groupBy("Company").min().show() #Min
df.groupBy("Company").sum().show() #Sum


df.agg({'Sales':'max'}).show() #aggregate across all rows to get one result


from pyspark.sql.functions import countDistinct, avg, stddev
df.select(countDistinct("Sales")).show() #count distinct
df.select(countDistinct("Sales").alias("Distinct Sales")).show() #change alias name
df.select(avg('Sales')).show() #average
df.select(stddev("Sales")).show() #stdev


## DATETIME
#--------------------------------------------------------
from pyspark.sql.functions import (format_number, dayofmonth, hour, 
                                    dayofyear, month, year, 
                                    weekofyear, date_format)

df.select(dayofmonth(df['Date'])).show() #date of month
df.select(hour(df['Date'])).show() #hour
df.select(dayofyear(df['Date'])).show() #day of year
df.select(month(df['Date'])).show() #month
df.select(year(df['Date'])).show() #year








#--------------
# set configuration & spark context object
conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
conf = SparkConf().setMaster("local[*]").setAppName("MovieSimilarities") #[*] use all cores in local computer
sc = SparkContext(conf = conf)


#--------------
# call the data from file and create RDD (Resilient Distributed Dataset)
lines = sc.textFile("file:///Users/Spark/1800.csv")


#--------------
### RDD MAPPING
parsedLines = lines.map(parseLine)  #use map function, output has same number of entries, just that it can be transformed.
words = input.flatMap(lambda x: x.split())  #use flat map function, output has more entries than input
# difference illustrated here: https://www.linkedin.com/pulse/difference-between-map-flatmap-transformations-spark-pyspark-pandey


#--------------
### RDD REDUCE
# key/value functions
  # reduce by key, x & y represent values of same key
total = parsedLines.reduceByKey(lambda x, y: x + y)
totalsByAge = rdd.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
  # swap key with value; and sort result by key
swap = total.map(lambda x: (x[1],x[0])).sortByKey() #or .sortByKey(ascending = False)

# top N results
.take(10)

# look up from another RDD
mostPopularName = namesRdd.lookup(mostPopular[1])[0]

#--------------
# collect the results
results = words.collect()

#--------------
# broadcasting; send data to every node ahead of time
nameDict = sc.broadcast(loadMovieNames())

#--------------
# partition; spark does not distribute on its own
  # for reduceByKey(), join(), lookup(), groupByKey(), etc.
.partitionBy(100)



#--------------
# SUBMIT IN CMD TO RUN SCRIPT
spark-submit script_name.py
spark-submit --executor-memory 1g MovieSimilarities1M.py 260  #change executor memory from default 512Mb to 1G
spark-submit --version #check spark version

# troubleshooting UI
# type localhost:4040 in browser when script is running. Open troubleshooting UI



