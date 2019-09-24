import datetime

current_weight = 100
target_weight = 80
avg_weight_week = 1.5

start_date = datetime.date.today()
end_date = start_date

while current_weight > target_weight:
    end_date += datetime.timedelta(days=7)
    current_weight -= avg_weight_week

print("Goal Achieved by", end_date)
print(f"Goal reached in {(end_date-start_date).days//7} weeks")
