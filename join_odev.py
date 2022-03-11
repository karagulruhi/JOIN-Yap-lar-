#ödev 9


soru 1

SELECT city, country 
FROM city 
INNER JOIN country 
ON city.country_id=country.country_id;

soru 2


SELECT payment_id, first_name, last_name
FROM customer
INNER JOIN payment
ON customer.customer_id = payment.customer_id;


soru 3 


SELECT rental_id, first_name, last_name
FROM customer
INNER JOIN rental
ON customer.customer_id=rental.customer_id


#ödev 10

soru 1 

SELECT city, country
FROM city
LEFT JOIN country
ON city.country_id = country.country_id


soru 2 

SELECT city, country
FROM city
LEFT JOIN country
ON city.country_id = country.country_id

soru 3 

SELECT rental_id, first_name, last_name
FROM customer
FULL JOIN rental
ON customer.customer_id = rental.customer_id



