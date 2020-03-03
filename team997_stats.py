import tbapy
import json
from datetime import datetime


# this is my TBA api read key...
tba = tbapy.TBA('WgsfK1zC2r0o7RCsjjfCT4w51QDBcxzrU8xcOFXlLrBnN890zY7a6c1HuNn3qv2c')

#print (tba.status())

#print(json.dumps(tba.district_rankings('2019pnw')[0], sort_keys=True, indent=4))

teams = tba.district_teams('2020pnw', simple=True)

events = tba.district_events('2020pnw', simple=True)

today=datetime.date(datetime.now())

i=0
for event in events:
    if event.event_type == 2:
        continue

    event_start = datetime.strptime(event.start_date, '%Y-%m-%d').date()

    if event_start > today:
        print ("Event ",event.name," has not started")
        continue

    print ("Getting data for ", event.name)

    continue

    i=1
    print("Event : ",event.name)
    key=str(year)+"pnw"
    district=tba.district_rankings(key)
    print(year, " PNW District Team Count: ", len(district))

    dkey=str(year)+"pncmp"
    dcmp_count = len(tba.event_teams(dkey))
    print(year," District Championship Teams:",dcmp_count)

    #print(json.dumps(tba.event_teams('2019pncmp'), sort_keys=True, indent=4))

    for team in district:
        if team.rank <= 5:
            print(team.rank,": ",team.team_key)
        if team.team_key == 'frc997':
            count = len(team.event_points)
            dc = chk_dcmp(team)
            print (i,": Team:",team.team_key,", Rank:",team.rank,", Total Points:",team.point_total, ", Event Count:",count, ", Dcmp: ",dc)
            i=i+1

    print("")

