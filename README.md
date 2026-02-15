# Question 1 

- The Answer is 25.3

### Commands:
- docker run -it --rm --entrypoint=bash python:3.13
- pip --version to see the version of pip

# Question 2

The Answers are:
- db:5432
- postgres:5432

# Question 3

- Answer 8007
```
SELECT COUNT(*)
FROM public."green_tripdata_2025-11" 
WHERE
	lpep_pickup_datetime >= '2025-11-01'
	AND lpep_pickup_datetime < '2025-12-01'
	AND trip_distance <= 1
;
```

# Question 4
- Answer 2025-11-14
```
SELECT lpep_pickup_datetime, trip_distance 
FROM public."green_tripdata_2025-11"
WHERE trip_distance < 100
ORDER BY trip_distance DESC
;
```
# QUESTION 5
- Answer East Harlem North
```
SELECT "PULocationID",
	SUM(total_amount) AS total_revenue,
	public.taxi_zone_lookup."Zone"
FROM public."green_tripdata_2025-11"
INNER JOIN public.taxi_zone_lookup
	ON public."green_tripdata_2025-11"."PULocationID" = public.taxi_zone_lookup."LocationID"
WHERE 
	lpep_pickup_datetime >= '2025-11-18' 
	AND lpep_pickup_datetime < '2025-11-19'
GROUP BY 
	"PULocationID",
	public.taxi_zone_lookup."Zone"
ORDER BY total_revenue DESC
;
```



