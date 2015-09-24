"""
Builds datebox into one file.  To build a new version, change the version
number and rerun.

M. Marino Apr 2014
"""

import requests 
import sys
import re
import os
import logging
# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig() 
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

version = "1.4.5"
base_url = "http://dev.jtsage.com/jQM-DateBox/builder/make.php"
cdn_url = "http://cdn.jtsage.com/datebox/{version}/jqm-datebox-{version}.css".format(version=version)
module_name = "jquery-mobile-datebox"
json_file = """
{
    "name": "%(NAME)s",
    "version": "%(VERSION)s-kanso.2",
    "categories": ["utils"],
    "maintainers": [
        {
            "name": "Michael Marino",
            "url": "https://github.com/mgmarino"
        }
    ],
    "url": "%(URL)s",
    "modules": "%(NAME)s.js",
    "modules_attachment": false,
    "attachments" : ["css"],
    "dependencies": {
        "modules": ">=0.0.8",
        "attachments": null,
        "jquery": ">=1.9.1-kanso.2",
        "jquery-mobile": ">=1.4.2-kanso.1"
    },
    "description": "A Date and Time Picker plugin for jQueryMobile 1.2.0+.  This provides version %(VERSION)s."
}
""" % { 
        "NAME" : module_name, "VERSION" : version,
        "URL" : "http://dev.jtsage.com/jQM-DateBox/"
      }

components = [
  "calbox",
  "datebox",
  "flipbox",
  "slidebox",
  "durationbox",
  "durationflipbox",
  "customflip",
]
  
payload = {
  "langs" : ["en"],
  "ver" : version, 
  "amd" : "no", 
}

payload.update(dict([("comp-" + k, "true") for k in components]))

core_data = requests.post(base_url, data=payload).text
core_data = core_data.replace('( jQuery )', '( require("jquery") )') 
#core_data = requests.post("http://httpbin.org/post", data=payload).text
css = requests.get(cdn_url).text
       
open(module_name + ".js", "w").write(core_data)
open(module_name + ".css", "w").write(css)
open("kanso.json", "w").write(json_file)
