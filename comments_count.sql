SELECT u.username, count(comment_id)
FROM "user" u
    LEFT JOIN comment c on c.user_id = u.user_id
GROUP BY u.username;