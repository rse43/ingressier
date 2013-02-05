#!/bin/python
# -*- coding:utf-8 -*-

import re
text = """shuo,<br/><br/>Your Link has been destroyed by Gore at 15:16 hrs. - <a href=3D"http://www.ingress.com/intel?latE6=3D-33888999&lngE6=3D151124356&z=3D19">View start location</a> - <a href=3D"http://www.ingress.com/intel?latE6=3D-33890388&lngE6=3D151125367&z=3D19">View end location</a><br/><br/><a hr=ef=3D"http://www.ingress.com/intel?latE6=3D-33888999&lngE6=3D151124356&z=3D=19"><img src=3D"http://lh3.ggpht.com/fVpIu7wi7X7dYL3qOx85zHoUWLZwLtYi09mVna=E_P865iL7Wi-z4outofPCH1tWs3xkLgomnxMm4zFSCeuQR1_Ho_tYx7prFXz4IQKeOaquoJWrF"=/></a>&nbsp;<a href=3D"http://www.ingress.com/intel?latE6=3D-33890388&lngE6=3D151125367&z=3D19"><img src=3D"http://lh4.ggpht.com/rM-jM5dLz7RlsueMxgLVr=UKaJWyYnTMjEydR3KN7aqI1dEJLMKgdb6jBT6NWPa5nXTg7t2-FRuxE5rtqGwZmjXsoSmH-wg0k=eEgPzSMs7dLMlnp1"/></a><br/><br/>Your Link has been destroyed by Gore at 15:16 hrs. - <a href=3D"http://www.ingress.com/intel?latE6=3D-33890388&lngE6=3D151125367&z=3D19">View start location</a> - <a href=3D"http://www.ingress.com/intel?latE6=3D-33889776&lngE6=3D151126108&z=3D19">View end location</a><br/><br/><a href=3D"http://www.ingress.com/intel?latE6=3D-33890388&lngE6=3D151125367&z=3D19"><img src=3D"http://lh4.ggpht.com/rM-jM5dLz7RlsueMxgLVr=UKaJWyYnTMjEydR3KN7aqI1dEJLMKgdb6jBT6NWPa5nXTg7t2-FRuxE5rtqGwZmjXsoSmH-wg0k=eEgPzSMs7dLMlnp1"/></a>&nbsp;<a href=3D"http://www.ingress.com/intel?latE6=3D-33889776&lngE6=3D151126108&z=3D19"><img src=3D"http://lh6.ggpht.com/Wsn=n6TAuVaATevPHWWr0h4WtZ8JEvC_0Y6T5v893W0CYNY-KpdLYz1AS5ZOZMfPKqwDi_57_FYVGIv=gUQz7XLl1dY_vTUH0z1fT7q06jdBVUtp8F"/></a><br/><br/><br/>-------------------=-----------------------<br/><a href=3D"http://www.ingress.com/intel">Dashbo=ard</a>&nbsp;<a href=3D"http://support.google.com/ingress">Contact</a><br/>"""
text2 = """shuo,<br/><br/>2 Resonator(s) were destroyed by Gore at 15:36 hrs. - <a href=3D"http://www.ingress.com/intel?latE6=3D-33888999&lngE6=3D151124356&z=3D19">View location</a><br/> <br/><a href=3D"http://www.ingress.com/intel?latE6=3D-33888999&lngE6=3D151124356&z=3D19"><img src=3D"http://lh3.ggpht.com/fVpIu7wi7X7dYL3qOx85zHoUWLZwLtYi09mVnaE_P865iL7Wi-z4outofPCH1tWs3xkLgomnxMm4zFSCeuQR1_Ho_tYx7prFXz4IQKeOaquoJWrF"/></a><br/><br/><br/><br/>------------------------------------------<br/><a href=3D"http://www.ingress.com/intel">Dashboard</a>&nbsp;<a href=3D"http://support.google.com/ingress">Contact</a><br/>"""
owner_regex = re.compile('^(.*),<br/><br/>')
match = owner_regex.match(text)
print match.group(1)

activity_regex = re.compile("Your (.*?) has been destroyed by (.*?) at (.*?) hrs. \- \<a href\=3D\"http:\/\/www\.ingress\.com\/intel\?latE6=3D(.*?)&lngE6=3D(.*?)\&z=3D19\">View start location\<\/a\> - <a href=3D\"http:\/\/www\.ingress\.com\/intel\?latE6=3D(.*?)&lngE6=3D(.*?)&z=3D19\">View end location<\/a>")
match = activity_regex.findall(text)
for group in match:
    print group

item_regex = re.compile("(\d+?) (.+?) were destroyed by (.*?) at (.*?) hrs. \- \<a href\=3D\"http:\/\/www\.ingress\.com\/intel\?latE6=3D(.*?)&lngE6=3D(.*?)\&z=3D19\">View location\<\/a\>")
match = item_regex.findall(text2)
for group in match:
    print group[0]