# Question 1 

Run docker with the python:3.13 image. Use an entrypoint bash to interact with the container.
What's the version of pip in the image?

- The Answer is 25.3

### Commands:
- docker run -it --rm --entrypoint=bash python:3.13
- pip --version to see the version of pip

# Question 2

Given the following docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?

The Answers are:
- db:5432
- postgres:5432

# Question 3

For the trips in November 2025 (lpep_pickup_datetime between '2025-11-01' and '2025-12-01', exclusive of the upper bound), how many trips had a trip_distance of less than or equal to 1 mile?

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

Which was the pick up day with the longest trip distance? Only consider trips with trip_distance less than 100 miles (to exclude data errors).

- Answer 2025-11-14
```
SELECT lpep_pickup_datetime, trip_distance 
FROM public."green_tripdata_2025-11"
WHERE trip_distance < 100
ORDER BY trip_distance DESC
;
```
# QUESTION 5

Which was the pickup zone with the largest total_amount (sum of all trips) on November 18th, 2025?

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

# Question 6

For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip?

- Answer Yorkville West
```
SELECT 
	do1."Zone" AS pickup_zone,
	do2."Zone" AS dropoff_zone,
	tip_amount
FROM public."green_tripdata_2025-11"
INNER JOIN public.taxi_zone_lookup AS do1
	ON public."green_tripdata_2025-11"."PULocationID"
		= do1."LocationID"
INNER JOIN public.taxi_zone_lookup AS do2
	ON public."green_tripdata_2025-11"."DOLocationID" 
		= do2."LocationID"
WHERE do1."Zone" LIKE 'East Harlem North'
ORDER BY tip_amount DESC
;
```

# Question 7

Which of the following sequences, respectively, describes the workflow for:

Downloading the provider plugins and setting up backend,
Generating proposed changes and auto-executing the plan
Remove all resources managed by terraform`
Answers:

terraform import, terraform apply -y, terraform destroy
teraform init, terraform plan -auto-apply, terraform rm
terraform init, terraform run -auto-approve, terraform destroy
terraform init, terraform apply -auto-approve, terraform destroy
terraform import, terraform apply -y, terraform rm

The Answer it is:
terraform init, terraform apply -auto-approve, terraform destroy


