.read data.sql


CREATE TABLE bluedog AS
  SELECT students.color AS color, students.pet AS pet FROM students 
  WHERE students.color = 'blue'
  AND students.pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT students.color AS color, students.pet AS pet, students.song AS song FROM students 
  WHERE students.color = 'blue'
  AND students.pet = 'dog';


CREATE TABLE smallest_int_having AS
  SELECT students.time AS time, students.smallest AS smallest FROM students
  GROUP BY students.smallest
  HAVING count(*) = 1;


CREATE TABLE matchmaker AS
  SELECT s1.pet AS pet, s1.song AS song, s1.color AS color1, s2.color AS color2
  FROM students AS s1, students AS s2
  WHERE s1.pet = s2.pet
  AND s1.song = s2.song
  AND s1.time < s2.time;


CREATE TABLE sevens AS
  SELECT students.seven AS seven FROM students, numbers
  WHERE students.time = numbers.time
  AND students.number = 7
  AND numbers."7" = "True";


CREATE TABLE avg_difference AS
  SELECT round(avg(abs(students.number - students.smallest))) FROM students;

