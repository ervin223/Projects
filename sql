

--Страны, названия которых начинаются на букву “К” (5 записей);
    
SELECT * from country
WHERE Name LIKE 'K%';

Страны, получившие независимость в 19-м веке (27 записей)

SELECT Name, IndepYear
FROM country
WHERE Indepyear between 1800 and 1899;
    
--Страны ближнего востока (Middle East) (18 записей)

SELECT Name, Region
FROM country
WHERE Region LIKE "Middle East";
    
--Европейские страны, которые образовались в 19 веке (7 записей)

SELECT Name, IndepYear, Region
FROM country
WHERE IndepYear BETWEEN (1800 AND 1899) AND Continent LIKE "Europe%";
  
  Страны, в названиях которых содержат слог “ра”  (9 записей)

SELECT Name
FROM Country
WHERE Name LIKE '%pa%';

    Страны, названия которых начинаются на гласную букву  (A, E, I, O, U, Y) (42 записи);

SELECT Name
FROM country
WHERE Name LIKE 'A%' OR Name LIKE 'E%' Name LIKE 'I%' OR Name LIKE '0%' Name LIKE 'U%' OR Name LIKE 'Y%';
    
Страны, названия которых начинаются и заканчиваются на одну и ту же букву. (20 записей)

SELECT name 
FROM country
where LEFT(Name,1) = RIGHT(Name,1);
    
Государства, формой правления которых является различной формы монархия (43 записи)

SELECT name 
FROM country
WHERE GovernmentForm LIKE 'Monarchy';

Страны, население которых меньше 1 млн. (85 записей)

SELECT name
FROM country
WHERE Population < 1000000;

Самое древнее государство (China)

SELECT name, Indepear
FROM country
ORDER BY indepyear LIMIT 1;

    Страны, год обретения независимости которыми не определен (47 записей)
    Страны, год обретения независимости которыми или столица которых и  не определены (47 записей)
    Самое маленькое по площади государство (Holy See (Vatican City State))
SELECT name, SurfaceArea
FROM country
ORDER BY SurfaceArea LIMIT 1;
    
Первую десятку наиболее населенных государств мира

SELECT name, population
FROM country
ORDER BY population DESC LIMIT 10;
    
Первую десятку наиболее населенных государств Европы

SELECT name, population
FROM country
WHERE continent LIKE 'Europe'
ORDER BY population DESC LIMIT 10;
    
Cуммарное число жителей стран Европы и суммарную площадь её государств (730 074 600, 23 049 133.9)

SELECT SUM (Population)
SUM (SurfaceArea) AS 'kokku_indala'
FROM country;
     
Число стран, расположенных не в Антарктике (234 записи)

SELECT COUNT(Name)
FROM country
WHERE continent not in LIKE '%antarctica';
    
Число стран, где главой правительства является Елизавета II (Elisabeth II), суммарное число жителей этих стран.  (35 стран, 122 872 550 человек)
     
SELECT SUM(Population)
FROM country
WHERE HeadOfState LIKE 'Elisabeth II'

Число стран, наибольшее и наименьшее число жителей стран Полинезии (Polynesia) (10 стран, 235 000 человек, 50 человек)

SELECT COUNT(*), MIN(Population), MAX(Population)
FROM country
WHERE Continent LIKE 'Polynesia';
    
Первые 5% списка стран мира наименьшей площади

1)
SELECT countryName, population
FROM city
WHERE population < 100000
ORDER BY population DESC
LIMIT 5;

2) 
SELECT countryName, population
FROM city
WHERE countryName LIKE 'H%'

3)
UPDATE city
SET countryName = LEFT(countryName, LENGTH(countryName) - 1) || 'B'
WHERE countryName LIKE 'M%';

SELECT countryName
FROM city
WHERE countryName LIKE 'M%'

4)
CREATE TABLE tri_bukvi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    short_name VARCHAR(3)
);

INSERT INTO tri_bukvi (short_name)
SELECT LEFT(countryName, 3) AS short_name
FROM city;

SELECT short_Name
from tri_bukvi




