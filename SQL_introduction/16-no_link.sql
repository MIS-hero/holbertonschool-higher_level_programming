-- display the score and the name by descending score
SELECT score, name FROM second_table WHERE name IS  NOT NULL ORDER BY score DESC;
