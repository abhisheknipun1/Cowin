import requests
import datetime
import json

# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=512&date=31-03-2021', headers=headers)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# To find the district codes - https://cdn-api.co-vin.in/api/v2/admin/location/districts/{1-40}
# {1-40} - This is state and union territory codes (1 to 40)


def vaccine_availabily_for_5_days():
    districtid = [97,86,95]
    current_date = datetime.date.today()
    for dist in districtid:
        parameter(current_date.strftime("%d-%m-%Y"),dist)
    for i in (1,2,3,4):
        newdate = current_date + datetime.timedelta(days=i)
        for dist in districtid:
            parameter(newdate.strftime("%d-%m-%Y"),dist)


def parameter(current_date,districtid):
    params = (
        ('district_id', districtid),
        ('date', current_date),
    )
    response(params)


def response(params):
    resp = requests.get(
        'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict', headers=headers, params=params)
    resp = resp.json()
    # debug
    #print(type(resp))
    #print(resp)
    vaccine_available_for_min_18_years_old(resp)
    #vaccine_available_for_min_45_years_old(resp)



def vaccine_available_for_min_18_years_old(resp):
    for data in resp["sessions"]:
        if data["min_age_limit"] == 18:
            if data["available_capacity_dose1"] > 0 or data["available_capacity_dose2"] > 0:
                print()
                print("district_name = {}".format(data["district_name"]))
                print("date = {}".format(data["date"]))
                print("min_age_limit = {}".format(data["min_age_limit"]))
                print("Centre name = {}".format(data["name"]))
                print("block_name = {}".format(data["block_name"]))
                print("vaccine = {}".format(data["vaccine"]))
            if data["available_capacity_dose1"] > 0:
                print("available_capacity_dose1 = {}".format(data["available_capacity_dose1"]))
            if data["available_capacity_dose2"] > 0:
                print("available_capacity_dose2 = {}".format(data["available_capacity_dose2"]))


def vaccine_available_for_min_45_years_old(resp):
    for data in resp["sessions"]:
        if data["min_age_limit"] == 45:
            if data["available_capacity_dose1"] > 0 or data["available_capacity_dose2"] > 0:
                print()
                print("district_name = {}".format(data["district_name"]))
                print("date = {}".format(data["date"]))
                print("min_age_limit = {}".format(data["min_age_limit"]))
                print("Centre name = {}".format(data["name"]))
                print("block_name = {}".format(data["block_name"]))
                print("vaccine = {}".format(data["vaccine"]))
            if data["available_capacity_dose1"] > 0:
                print("available_capacity_dose1 = {}".format(data["available_capacity_dose1"]))
            if data["available_capacity_dose2"] > 0:
                print("available_capacity_dose2 = {}".format(data["available_capacity_dose2"]))



vaccine_availabily_for_5_days()
