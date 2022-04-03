counties=["Arapahoe","Denver","Jefferson"]
voting_data=[]
voting_data.append({"county":"Arapanhoe","registered_voters":422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})
for county in counties:
    print(county)
counties_dict={'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
for counties in counties_dict:
    print(counties)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county,voters in counties_dict.items():
    print(county,voters)
for county,voters in counties_dict.items():
    print(str(county)+" county has "+ str(voters) + " registered voters")
for count_dic in voting_data:
    print(count_dic)

for county_dict in voting_data:
    for value in county_dict.values():
        print (value)
for county,value in counties_dict.items():
    message=(
        f"{county} county has {value:,} registered voters")
    print(message)