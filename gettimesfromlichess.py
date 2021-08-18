#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import requests
import sys

bearertoken = sys.argv[1]

f = open(sys.argv[2],"r")
lines = f.readlines()

for line in lines:
    lichessgameid = line[:-1]

    url = "https://lichess.org/game/export/%s" %lichessgameid

    querystring = {
        "pgnInJson":"false",
        "moves":"false",
        "evals":"false",
        "opening":"false"
        }

    payload = ""
    headers = {
        'Accept': "application/json",
        'Authorization': "Bearer %s" %bearertoken
        }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    game = json.loads(response.text)

    if game["speed"] != "correspondence":
        print("%s,%s,%s,%s,%s,%s,%s" %(lichessgameid,
            game["createdAt"],
            game["lastMoveAt"],
            game["clock"]["initial"],
            game["clock"]["increment"],
            game["variant"],
            game["speed"]
            )
        )
