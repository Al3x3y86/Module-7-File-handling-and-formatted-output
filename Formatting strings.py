team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

challenge_result = 'Победа команды Волшебники данных!'

result = ""
if score1 > score2 or score1 == score2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    result = 'Победа команды Волшебники данных!'
else:
    result = 'Ничья!'

# Использование %
team1_info = "В команде Мастера кода участников: %d!" % team1_num
team2_info = "Итого сегодня в командах участников: %d и %d!" % (team1_num, team2_num)

# Использование format()
team2_score_info = "Команда Волшебники данных решила задач: {}!".format(score2)
team2_time_info = "Волшебники данных решили задачи за {} сек!".format(team2_time)

# Использование f-строк
teams_scores_info = f"Команды решили {score1} и {score2} задач."
challenge_result_info = f"Результат битвы: {result}!"
tasks_avg_info = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунд на задачу."

print(team1_info)
print(team2_info)
print(team2_score_info)
print(team2_time_info)
print(teams_scores_info)
print(challenge_result_info)
print(tasks_avg_info)