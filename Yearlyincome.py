income = input('How much does the job pay hourly or yearly? $')

# yearly and hourly evaluate what math should be completed.
yearly = 4 <= len(income)
hourly = 2 >= len(income)

if yearly:
    per_month = round(int(income) / 12, 2)
    per_week = int(per_month) / 4
    per_hour = int(per_week) / 40
    print(f'Pay per month:${per_month} \nPay per week: ${per_week} \nPay per hour: ${per_hour} (Assuming 40 hours)')

elif hourly:
    hours = float(input('How many hours per week? '))
    per_hour = int(income)
    per_week = int(per_hour) * int(hours)
    per_month = int(per_week) * 4
    per_year = int(per_month) * 12
    print(f"Pay per hour: $", per_hour , "\nPay per week: $", per_week, f"(At {hours} hours)", "\nPay per month: $",
          per_month, "\nPay per year $", per_year)

