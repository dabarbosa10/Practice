SELECT * FROM movies 
WHERE year BETWEEN 1970 AND 1979
  AND imdb_rating >8;

SELECT * FROM movies 
WHERE year < 1985
  AND genre IS 'horror';

SELECT * FROM movies WHERE genre='romance' OR genre='comedy'

SELECT name, year FROM movies ORDER BY name;

SELECT name, year, imdb_rating FROM movies ORDER BY imdb_rating DESC;

SELECT * FROM movies ORDER BY imdb_rating DESC LIMIT 3;

