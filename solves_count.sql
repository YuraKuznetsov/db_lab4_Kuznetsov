SELECT u.username, count(solve_id)
FROM "user" u
    LEFT JOIN solve s on s.user_id = u.user_id
GROUP BY u.username;