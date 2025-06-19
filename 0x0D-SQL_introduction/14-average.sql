-- gets the average and add i into another column
UPDATE second_table
SET average = (
  SELECT avg_score
  FROM (SELECT AVG(score) AS avg_score FROM second_table) AS temp
);
