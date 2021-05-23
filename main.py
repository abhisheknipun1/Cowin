import requests
import json


# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=512&date=31-03-2021', headers=headers)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

params = (
    ('district_id', '97'),
    ('date', '24-05-2021'),
)

response = requests.get(
    'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict', headers=headers, params=params)
resp = response.json()

# debug
# print(type(resp))
# print(resp)


def vaccine_available_for_min_18_years_old():
    count = 0
    for data in resp["sessions"]:
        count = count + 1
        if count == 1:
            print(data["district_name"])
        if data["min_age_limit"] == 18:
            if data["available_capacity_dose1"] > 0 or data["available_capacity_dose2"] > 0:
                print()
                print("min_age_limit = {}".format(data["min_age_limit"]))
                print("Centre name = {}".format(data["name"]))
                print("block_name = {}".format(data["block_name"]))
                print("vaccine = {}".format(data["vaccine"]))
            if data["available_capacity_dose1"] > 0:
                print("available_capacity_dose1 = {}".format(data["available_capacity_dose1"]))
            if data["available_capacity_dose2"] > 0:
                print("available_capacity_dose2 = {}".format(data["available_capacity_dose2"]))


def vaccine_available_for_min_45_years_old():
    count = 0
    for data in resp["sessions"]:
        count = count + 1
        if count == 1:
            print(data["district_name"])
        if data["min_age_limit"] == 45:
            if data["available_capacity_dose1"] > 0 or data["available_capacity_dose2"] > 0:
                print()
                print("min_age_limit = {}".format(data["min_age_limit"]))
                print("Centre name = {}".format(data["name"]))
                print("block_name = {}".format(data["block_name"]))
                print("vaccine = {}".format(data["vaccine"]))
            if data["available_capacity_dose1"] > 0:
                print("available_capacity_dose1 = {}".format(data["available_capacity_dose1"]))
            if data["available_capacity_dose2"] > 0:
                print("available_capacity_dose2 = {}".format(data["available_capacity_dose2"]))


vaccine_available_for_min_18_years_old()
#vaccine_available_for_min_45_years_old()
