SELECT u.username, count(solve_id)
FROM "user" u
    LEFT JOIN solve s on s.user_id = u.user_id
GROUP BY u.username;


SELECT u.username, count(comment_id)
FROM "user" u
    LEFT JOIN comment c on c.user_id = u.user_id
GROUP BY u.username;


SELECT time
FROM "user" u
    JOIN solve s on s.user_id = u.user_id
    JOIN discipline d on d.discipline_id = s.discipline_id
WHERE username = 'Cubewars' AND discipline_name = 'CUBE_3X3'