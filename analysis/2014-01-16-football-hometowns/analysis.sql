# School diversity

SELECT z.school,
       SUM(z.power) AS concentration_score
  FROM (
SELECT a.school,
       (a.county_players*1.0/a.all_players) *
       (a.county_players*1.0/a.all_players) AS power
  FROM (
SELECT p.school,
       p.state,
       c.players AS all_players,
       COUNT(*) AS county_players
  FROM players_all p
  JOIN (SELECT c.school,
               COUNT(*) AS players
          FROM players_all c
         WHERE c.county_code != 0
         GROUP BY 1
       ) c
    ON c.school = p.school
 WHERE p.county_code != 0
 GROUP BY 1,2,3
       ) a
       ) z 
 GROUP BY 1













