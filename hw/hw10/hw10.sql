CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs, sizes WHERE height > min AND height <= max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT a.name FROM parents, dogs as a, dogs as b WHERE child = a.name AND parent = b.name ORDER BY -b.height;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT "";

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT a.name || " and " || b.name || " are " || size || " siblings" FROM dogs AS a, dogs AS b, parents AS c, parents AS d, sizes WHERE a.name < b.name AND c.child = a.name AND d.child = b.name AND c.parent = d.parent AND a.height > min AND a.height <= max AND b.height > min AND b.height <= max;


CREATE TABLE stacks AS
  SELECT a.name || ", " || b.name || ", " || c.name || ", " || d.name, a.height + c.height + b.height + d.height
  FROM dogs AS a, dogs AS b, dogs AS c, dogs AS d
  WHERE a.height + c.height + b.height + d.height >= 170 AND a.name != b.name AND a.name != c.name AND a.name != d.name AND b.name != c.name AND c.name != d.name AND a.height < b.height AND b.height < c.height AND c.height < d.height
  ORDER BY a.height + c.height + b.height + d.height;
