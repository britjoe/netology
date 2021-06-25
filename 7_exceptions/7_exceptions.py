from datetime import datetime, timedelta

moscow_times = 'Wednesday, October 2, 2002'
guardian = 'Friday, 11.10.13'
daily_news = 'Thursday, 18 August 1977'
moscow_times = datetime.strptime(moscow_times, '%A, %B %d, %Y')
guardian = datetime.strptime(guardian, '%A, %d.%m.%y')
daily_news = datetime.strptime(daily_news, '%A, %d %B %Y')
print(moscow_times, guardian, daily_news)

stream = ['2018-04-02', '2018-02-29', '2018-19-02']


def check_date(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d')
        return True
    except:
        return False


for i in stream:
    print(check_date(i))


def date_range(start_date, end_date):
    date_list = []
    if check_date(start_date) and check_date(end_date):
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        cnt_days = (end_date - start_date).days
        if cnt_days <= 0:
            return date_list
        for i in range(cnt_days - 1):  ## - 1 для невключения последней даты
            new_date = start_date + timedelta(days=i + 1)  ## + 1 для невключения первой даты
            date_list.append(datetime.strftime(new_date, '%Y-%m-%d'))
        return date_list
    else:
        return date_list


start_date = '2017-12-30'
end_date = '2018-02-01'

print(date_range(start_date, end_date))
