n = int(input())
logs = []
for i in range(n):
    day, hour, minute, id, status = input().split()
    time = int(day) * 24 * 60 + int(hour) * 60 + int(minute)
    logs.append([time, int(id), status])
logs = sorted(logs, key=lambda x: x[0])
# print(logs)
rocket_movement = {}
for log in logs:
    if log[2] == 'A':
        if log[1] not in rocket_movement:
            rocket_movement[log[1]] = {'start': log[0], 'end': 0, 'total': 0}
        else:
            rocket_movement[log[1]]['start'] = log[0]
            rocket_movement[log[1]]['end'] = 0
            rocket_movement[log[1]]['total'] += 0
    elif log[2] == 'B':
        rocket_movement[log[1]]['end'] = log[0]
        rocket_movement[log[1]]['total'] += rocket_movement[log[1]]['end'] - rocket_movement[log[1]]['start']
        rocket_movement[log[1]]['start'] = log[0]
    elif log[2] == 'C' or log[2] == 'S':
        rocket_movement[log[1]]['end'] = log[0]
        rocket_movement[log[1]]['total'] += rocket_movement[log[1]]['end'] - rocket_movement[log[1]]['start']
        rocket_movement[log[1]]['start'] = 0
    else:
        continue
sorted_r_movement = dict(sorted(rocket_movement.items()))
# print(sorted_r_movement)
for k, v in sorted_r_movement.items():
    print(v['total'], end=' ')
