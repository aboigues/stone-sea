-- % réponses sourcées par lot
SELECT lot, AVG(reponses_ssourcees_pct) AS pct
FROM metrics
GROUP BY lot
ORDER BY pct DESC;

-- Incidents critiques par semaine
SELECT semaine, SUM(incidents_critique_nb) AS incidents
FROM metrics
GROUP BY semaine
ORDER BY semaine;
