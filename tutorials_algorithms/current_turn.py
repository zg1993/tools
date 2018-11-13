# coding: utf8

from datetime import datetime, timedelta
import time
from decorator import time_diff
options = "%Y-%m-%dT%H:%M:%S.%fZ"

@time_diff
def cur_turn_start(turns, timezone, timestamp):
    suffix = ':00.000000Z'
    factory_datetime = datetime.utcfromtimestamp(timestamp) + timedelta(hours=timezone)
    factory_str = factory_datetime.strftime('%Y-%m-%d %H:%M')
    year, hour = factory_str.split()
    current_turn = None
    for turn in turns:
        start_time = turn['start_time']
        end_time = turn['end_time']
        if start_time >= end_time:
            if hour < end_time or hour >= start_time:
                current_turn = turn
        else:

            if start_time <= hour < end_time:
                current_turn = turn
    if current_turn:
        update_time = year + 'T' + current_turn['start_time'] + suffix
        return update_time


@time_diff
def get_current_turn(turns, timezone, time_stamp, update_time=False, need_turn=False):
    if isinstance(time_stamp, datetime):
        factory_time = time_stamp + timedelta(hours=timezone)
    else:
        factory_time = datetime.fromtimestamp(time_stamp + timezone * 3600)
    factory_hours = datetime.strptime(factory_time.strftime('%H:%M'), '%H:%M')

    def str2dt(d):
        transfrom = ['start_time', 'end_time']
        for k, v in d.items():
            d[k] = datetime.strptime(v, '%H:%M') if k in transfrom else v

    map(str2dt, turns)
    current_turn = None
    for turn in turns:
        if turn.get('start_time') >= turn.get('end_time'):
            if factory_hours < turn.get('end_time') \
                    or factory_hours >= turn.get('start_time'):
                current_turn = turn
        else:
            if turn.get('start_time') <= factory_hours < turn.get('end_time'):
                current_turn = turn
    if update_time:
        update_time = ''
        if current_turn:
            start_time = current_turn.get('start_time')
            end_time = current_turn.get('end_time')
            turn_start = datetime(year=factory_time.year,
                                  month=factory_time.month,
                                  day=factory_time.day, 
                                  hour=start_time.hour, 
                                  minute=start_time.minute) \
                         - timedelta(hours=timezone)
            if start_time > end_time:
                
                if factory_hours < start_time:
                    turn_start -= timedelta(days=1)
            if need_turn:
                return (current_turn, turn_start)
            else:
                update_time = turn_start.strftime(options)
        else:
            if need_turn:
                factory_day_start = datetime(year=factory_time.year,
                                             month=factory_time.month,
                                             day=factory_time.day) \
                                    - timedelta(hours=timezone)
                return (current_turn, factory_day_start)
        return update_time
    else:
        return current_turn


if __name__ == '__main__':
    turns = [{
                "valid_time": "12.0",
                "start_time": "08:00",
                "name": "早班",
                "check_period_list": [
                    "08:00",
                    "12:00",
                    "16:00",
                    "20:00"
                ],
                "end_time": "20:00"
            },
            {
                "valid_time": "12.0",
                "start_time": "20:00",
                "name": "晚班",
                "end_time": "08:00"
            }
        ]
    timezone = 8
    timestamp = time.time() - 3600*8
    # timestamp = datetime.utcnow()
    print cur_turn(turns, timezone, time.time()+3600*5)
    print get_current_turn(turns, timezone, timestamp)
