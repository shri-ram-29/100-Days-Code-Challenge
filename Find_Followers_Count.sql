SELECT user_id,
       (SELECT COUNT(*) FROM Followers AS f2 WHERE f2.user_id = f1.user_id) AS followers_count
FROM (SELECT DISTINCT user_id FROM Followers) AS f1
ORDER BY user_id;