create table pizzas as
  select "Pizzahhh" as name, 12 as open, 15 as close union
  select "La Val's"        , 11        , 22          union
  select "Sliver"          , 11        , 20          union
  select "Cheeseboard"     , 16        , 23          union
  select "Emilia's"        , 13        , 18;

create table meals as
  select "breakfast" as meal, 11 as time union
  select "lunch"            , 13         union
  select "dinner"           , 19         union
  select "snack"            , 22;


-- Pizza places that open before 1pm in alphabetical order
create table opening as
SELECT pizzas.name AS name FROM pizzas
WHERE pizzas.open < 13
ORDER BY -pizzas.name;


-- Two meals at the same place
create table double as
SELECT m1.meal AS meal1, m2.meal AS meal2, pizzas.name AS name 
FROM meals AS m1, meals AS m2, pizzas
WHERE m2.time > m1.time + 6
AND pizzas.open <= m1.time
AND pizzas.close >= m2.time;

