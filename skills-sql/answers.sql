1

-----

Select all fields for all brands in the brands table.

The result set for this query should be every record in the brands table.

-----


SELECT * FROM brands
;


==========
2

-----

Select all fields for all car models made by Pontiac in the 
models table. 

The result set should be:
  id   | year  | brand_name |    name
-------+-------+------------+------------
    25 |  1961 | Pontiac    | Tempest
    27 |  1962 | Pontiac    | Grand Prix
    36 |  1963 | Pontiac    | Grand Prix
    42 |  1964 | Pontiac    | GTO
    43 |  1964 | Pontiac    | LeMans
    44 |  1964 | Pontiac    | Bonneville
    45 |  1964 | Pontiac    | Grand Prix
(7 rows)


-----


SELECT * FROM models WHERE brand_name='Pontiac';


==========
3

-----

Select the brand name and model name for all models made in 
1964 from the models table. 

The result set should be:
 brand_name |    name
------------+-------------
 Chevrolet  | Corvette
 Ford       | Mustang
 Ford       | Galaxie
 Pontiac    | GTO
 Pontiac    | LeMans
 Pontiac    | Bonneville
 Pontiac    | Grand Prix
 Plymouth   | Fury
 Studebaker | Avanti
 Austin     | Mini Cooper
 (10 rows)
 

-----


SELECT brand_name, name FROM models WHERE year='1964';


==========
4

-----

Select the model name, brand name, and headquarters for 
the Ford Mustang from the models and brands tables.

The result set should be:
  name   | brand_name | headquarters
---------+------------+--------------
 Mustang | Ford       | Dearborn, MI
 (1 rows)


-----


SELECT models.name, brand_name, headquarters
FROM models
JOIN brands ON brand_name=brands.name
WHERE models.name='Mustang';


==========
5

-----

Select all rows for the three oldest brands from the brands
table.

The result set should be:
  id   |    name    | founded |    headquarters     | discontinued
-------+------------+---------+---------------------+--------------
    10 | Studebaker |    1852 | South Bend, Indiana |         1967
    13 | Rambler    |    1901 | Kenosha, Washington |         1969
     6 | Cadillac   |    1902 | New York City, NY   |
(3 rows)


-----


SELECT id, name, founded, headquarters, discontinued
FROM brands
ORDER BY founded
LIMIT 3;


==========
6

-----

Count the Ford models in the database The output should be a 
number.

The result set should be:
   count
------------
          6
(1 rows)


-----


SELECT COUNT(brand_name) FROM models
WHERE brand_name='Ford';


==========
7

-----

Select the name of any and all car brands that are not 
discontinued.

The result set should be:
   name
-----------
 Ford
 Chrysler
 Chevrolet
 Cadillac
 BMW
 Buick
 Tesla
(7 rows)


-----


SELECT name FROM brands WHERE discontinued IS NULL;


==========
8

-----

Select everything from rows 15-24 of the models table in 
alphabetical order by name. The result set should have 10 records.

The result set should be:
  id   | year  | brand_name |   name
-------+-------+------------+----------
    38 |  1963 | Chevrolet  | Corvette
    11 |  1957 | Chevrolet  | Corvette
    20 |  1960 | Chevrolet  | Corvette
     5 |  1953 | Chevrolet  | Corvette
    13 |  1958 | Chevrolet  | Corvette
    10 |  1956 | Chevrolet  | Corvette
    17 |  1959 | Chevrolet  | Corvette
    26 |  1961 | Chevrolet  | Corvette
     8 |  1955 | Chevrolet  | Corvette
    28 |  1962 | Chevrolet  | Corvette
(10 rows)


-----


SELECT id, year, brand_name, name FROM models ORDER BY name OFFSET 14 LIMIT 10;


==========
9

-----

Select the brand, name, and year the model's brand was 
founded for all of the models from 1960. Include row(s)
for model(s) even if their brand(s) are not in the brands table.

Note that in the result set, the year the brand was founded should be NULL if
the brand is not in the brands table.

So, the result set should be:
   name   | brand_name | founded
----------+------------+---------
 Corvette | Chevrolet  |    1911
 Corvair  | Chevrolet  |    1911
 Rockette | Fairthorpe |    1954
 Fillmore | Fillmore   |
(4 rows)


-----


SELECT models.name, brand_name, founded
FROM models
FULL OUTER JOIN brands ON brand_name=brands.name
WHERE year=1960;


==========
10

-----

Modify the query so that it shows all brands that are 
not discontinued regardless of whether they have any models in the models table.
The correct output should not include records for Fillmore and Outback, but should
show information about Tesla, a brand with no models in the models table.

-----


SELECT b.name, b.founded, m.name
FROM models AS m
RIGHT JOIN brands AS b ON b.name = m.brand_name
WHERE b.discontinued IS NULL;


==========
11

-----

Modify the query so it only selects models whose brands ARE in the brands table.
So, we shouldn't see models who brands aren't in the brands table (a.k.a. Fillmore,
Outback) nor should we see information about brands who don't have any models in 
the models table (a.k.a. Tesla).

-----


SELECT m.name, m.brand_name, b.founded
FROM models AS m
INNER JOIN brands AS b
ON b.name = m.brand_name;