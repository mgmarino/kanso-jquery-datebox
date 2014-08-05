"""
Builds datebox into one file.  To build a new version, change the version
number and rerun.

M. Marino Apr 2014
"""

import urllib2 
import sys
import re
import os

base_url = "http://dev.jtsage.com/cdn/datebox"
version = "1.4.3"
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
  "durationbox",
  "slidebox",
]
  
total_url = "%(BASE)s/%(VERSION)s/jqm-datebox-%(VERSION)s" % { "BASE" : base_url, "VERSION" : version }

core_data = "" 
total_components = ["core"]
total_components.extend(["mode." + k for k in components])
for comp in total_components: 
    t = total_url + ".%s.js" % comp
    try:
        dat = urllib2.urlopen(t)
        core_data += dat.read().replace('( jQuery )', '( require("jquery") )') 
    except urllib2.URLError, e:
        print e, t
        print "Exiting..."
        sys.exit(1)

css = urllib2.urlopen(total_url + ".css").read()
comp = re.compile("""url\(['"](.*)['"]\)""")
match = comp.search(css)

total_url = "%(BASE)s/%(VERSION)s/" % { "BASE" : base_url, "VERSION" : version }
if match:
    for g in match.groups():
        print g
        dat = urllib2.urlopen(total_url + g).read()
        adir = os.path.dirname(g)
        if not os.path.exists(adir):
            os.makedirs(adir)
        open(g, "w").write(dat)
        
open(module_name + ".js", "w").write(core_data)
open(module_name + ".css", "w").write(css)
open("kanso.json", "w").write(json_file)
