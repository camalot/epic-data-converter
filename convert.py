import sys
import json
import os
import re
import random
import datetime
import glob
import time
import shutil
import tempfile
import click


@click.command()
@click.argument('infile', default=None)
@click.argument('outfile', default=None)
def main(infile, outfile):
    epicData = list()
    with open(infile) as json_in_file:
        data = json.load(json_in_file)
        for d in data['data']:
            group = data['data'][d]
            link = None
            if group['link'] is None:
                link = "https://store.epicgames.com/{{CREATORCODE}}/" + d
            else:
                link = group['link'].replace("/darthminos/", "/{{CREATORCODE}}/")
            name = group['name'].replace("\u00c2\u00ae", "").replace("\u00e2\u201e\u00a2", "")
            icon = group['icon']
            epicData.append({
                "link": link,
                "name": name,
                "icon": icon
            })
    with open(outfile, 'w') as out_file:
        json.dump(epicData, out_file)

if __name__ == "__main__":
    main()
