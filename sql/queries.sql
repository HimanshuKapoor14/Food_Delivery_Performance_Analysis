SELECT AVG(`Time_taken (min)`) AS Avg_Delivery_Time
FROM food_delivery;

SELECT City, AVG(`Time_taken (min)`) AS Avg_Time
FROM food_delivery
GROUP BY City;

SELECT Weather_conditions, AVG(`Time_taken (min)`) AS Avg_Time
FROM food_delivery
GROUP BY Weather_conditions;

SELECT Road_traffic_density, AVG(`Time_taken (min)`) AS Avg_Time
FROM food_delivery
GROUP BY Road_traffic_density;

SELECT AVG(Delivery_person_Ratings) AS Avg_Rating
FROM food_delivery;