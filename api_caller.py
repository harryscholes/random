import requests
import pandas as pd
import os
import json
import multiprocessing


def apiCall():
    url = ""
    params = {
                "ontology": ontology,
                "input": "".join((protein for protein in cluster)),
                "species": "HUMAN",
                "correction": "bonferroni",
                "format": "plain"
    }
    r = requests.get(url, params=params)
    with open("out.json", "w") as f:
        json.dump(r.json(), f)
    return r


def runAll():
    p = multiprocessing.Pool(17)
    p.map(apiCall, (os.path.join("../clustering/clusters_t0/", f) for f in os.listdir("../clustering/clusters_t0/")))
