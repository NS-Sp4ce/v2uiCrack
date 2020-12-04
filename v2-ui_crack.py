"""
Author         : Sp4ce
Date           : 2020-12-03 16:33:13
LastEditors    : Sp4ce
LastEditTime   : 2020-12-03 16:55:06
Description    : Challenge Everything.
"""
import requests
import argparse
import sys
import os
import json

"""
POST /login HTTP/1.1

username=admin&password=admin
"""


def login(URL):
    urls = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
    }
    data = {"username": "admin", "password": "admin"}
    if os.path.isfile(URL):
        with open(URL) as target:
            urls = target.read().splitlines()
    else:
        urls = URL.split()
    for url in urls:
        loginUrl = url + "/login"
        try:
            response = requests.post(loginUrl, data=data, timeout=10, headers=headers)
            resText = json.loads(response.text)
            if resText["success"] == False:
                pass
            else:
                print(url + " Login Success")
                with open("success.txt", "a+") as f:
                    f.write(url + "\n")
        except:
            print(url + " Login Failed")



def run():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-target", "--targetFile", type=str, help="Load targets file or single target."
    )

    args = parser.parse_args()
    if len(sys.argv) < 2:
        parser.print_help()
    else:
        login(args.targetFile)


if __name__ == "__main__":
    run()