--PSQL------------------------
-- upload csv to table
-- put csv in C:\tmp folder
copy public.tablename from 'C:\tmp\upload.csv' delimiter ',' csv header;



--SYSTEM----------------------
--check list of tables in database
SELECT * FROM information_schema.tables 
--check version of database
select version();
--check index tables
SELECT * FROM pg_indexes 
WHERE schemaname = 'public' and tablename = 'mytable';


--change password
ALTER user postgres
with password 'newpassword';
--change validity period
ALTER USER techonthenet
  VALID UNTIL 'Jan 1, 2015';
--change username
ALTER USER user_name
  RENAME TO new_name;
--create user
CREATE USER techonthenet
  WITH PASSWORD 'fantastic'
  VALID UNTIL 'Jan 1, 2015';


--grant privileges
-- https://www.techonthenet.com/postgresql/grant_revoke.php
GRANT SELECT, INSERT, UPDATE, DELETE ON table_name TO username;
GRANT ALL ON table_name TO username;
REVOKE privilege_types ON table_name FROM username;


--EXECUTION PLAN----------------------
--prints the time started for query to execute
explain analyze 
select query

--use this awesome visualizer to view the plan
--http://tatiyants.com


--VACUUM----------------------
--clean up junk in table that can affect performance
vacuum analzye table_name


--NEW TABLE----------------------
--time series
SELECT date_trunc('day', dd)::date
FROM generate_series
        ('2007-02-01'::timestamp, 
         '2008-04-01'::timestamp,
         '1 day'::interval) dd

--numbers
select generate_series(1,4)


--CROSS JOIN----------------------
select date, count from
--table 1
(SELECT date_trunc('day', dd)::date as date
 FROM generate_series ('2017-01-01'::timestamp, 
	               '2017-02-28'::timestamp, 
                       '1 day'::interval) dd) a
cross join
--table 2
(select generate_series(1,4) count) b


--HISTOGRAM BINNING----------------------
--width_bucket(column_name, start_range, end_range, no_of_bins)
--note, any values that fall out of start or end range will be classified into another bin
select width_bucket(columName, 0, 0.25, 10) as output_bin_no, 
	count(*), 
	min(columName),
	max(columName),
from tablename
group by 1
order by 1


--DATES-----------------------------

--get year
extract(year from to_timestamp(starttime))
date_part('year', to_timestamp(starttime))

--get month
extract(month from to_timestamp(starttime))
date_part('month', to_timestamp(starttime))

--get week no. of month
select ((date_part('day', now()::date)::integer-1)/7)+1
to_char(to_timestamp(starttime), 'W')

--add substrate dates
select date + interval '40 day' --also can use hour etc.
from tablename


--TRANSPOSE-----------------------------
--installation of extension is needed
CREATE EXTENSION tablefunc;

SELECT *
FROM crosstab(
      'SELECT section, status, ct
       FROM   t
       ORDER  BY 1,2')  -- needs to be "ORDER BY 1,2" here
AS ct ("Section" text, "Active" int, "Inactive" int); --enter all column names to be input as ct in the crosstab function

--REVERSE TRANSPOSE (UNNEST)-----------------------------
select scanid, 
	unnest(array[column1, column2, column3]) 
from s188


--POSTGIS-----------------------------
--http://www.bostongis.com/PrinterFriendly.aspx?content_name=postgis_tut01
--use Stack Builder (preinstalled with PostGres) to install PostGIS

--PostGIS version
SELECT PostGIS_full_version();

--Convert SHP to POSTGIS
-- Get the GUI Tool from the path below in windows
-- C:\Program Files\PostgreSQL\9.6\bin\postgisgui



--RESOURCES-----------------------------
-- https://gist.github.com/clhenrick/ebc8dc779fb6f5ee6a88