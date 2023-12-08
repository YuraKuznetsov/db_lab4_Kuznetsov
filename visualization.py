import matplotlib.pyplot as plt
from main import PostgresDB, solves_count_sql, comments_count_sql, user_solves_sql

database = PostgresDB(dbname='lab3', username='postgres', password='1000dollars')
database.connect()

# Cтовпчикова діаграма
database.execute_query(solves_count_sql)
usernames, solve_counts = zip(*database.fetch_all())

plt.bar(usernames, solve_counts, color='orange')
plt.xlabel('Usernames')
plt.ylabel('Solve Counts')
plt.title('Solve Counts for Users')
plt.show()


# Кругова діаграма
database.execute_query(comments_count_sql)
usernames, comment_counts = zip(*database.fetch_all())

plt.pie(comment_counts, labels=usernames, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Comments percentage for users')
plt.show()


# Графік  залежності
database.execute_query(user_solves_sql)

times = [time[0] for time in database.fetch_all()]
solves = range(1, len(times) + 1)

time_in_seconds = []
for time in times:
    minutes, seconds = map(float, time.split(':'))
    total_seconds = minutes * 60 + seconds
    time_in_seconds.append(total_seconds)

plt.plot(solves, time_in_seconds, marker='o', linestyle='-')
plt.xlabel('Solves')
plt.ylabel('Time (seconds)')
plt.title('Time of User Solves')
plt.show()


database.close_connection()
