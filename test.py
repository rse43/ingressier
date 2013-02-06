#!/bin/python
# -*- coding:utf-8 -*-

import re
import datetime
text = """shuo,<br/><br/>Your Link has been destroyed by Gore at 15:16 hrs. - <a href=3D"http://www.ingress.com/intel?latE6=3D-33888999&lngE6=3D151124356&z=3D19">View start location</a> - <a href=3D"http://www.ingress.com/intel?latE6=3D-33890388&lngE6=3D151125367&z=3D19">View end location</a><br/><br/><a hr=ef=3D"http://www.ingress.com/intel?latE6=3D-33888999&lngE6=3D151124356&z=3D=19"><img src=3D"http://lh3.ggpht.com/fVpIu7wi7X7dYL3qOx85zHoUWLZwLtYi09mVna=E_P865iL7Wi-z4outofPCH1tWs3xkLgomnxMm4zFSCeuQR1_Ho_tYx7prFXz4IQKeOaquoJWrF"=/></a>&nbsp;<a href=3D"http://www.ingress.com/intel?latE6=3D-33890388&lngE6=3D151125367&z=3D19"><img src=3D"http://lh4.ggpht.com/rM-jM5dLz7RlsueMxgLVr=UKaJWyYnTMjEydR3KN7aqI1dEJLMKgdb6jBT6NWPa5nXTg7t2-FRuxE5rtqGwZmjXsoSmH-wg0k=eEgPzSMs7dLMlnp1"/></a><br/><br/>Your Link has been destroyed by Gore at 15:16 hrs. - <a href=3D"http://www.ingress.com/intel?latE6=3D-33890388&lngE6=3D151125367&z=3D19">View start location</a> - <a href=3D"http://www.ingress.com/intel?latE6=3D-33889776&lngE6=3D151126108&z=3D19">View end location</a><br/><br/><a href=3D"http://www.ingress.com/intel?latE6=3D-33890388&lngE6=3D151125367&z=3D19"><img src=3D"http://lh4.ggpht.com/rM-jM5dLz7RlsueMxgLVr=UKaJWyYnTMjEydR3KN7aqI1dEJLMKgdb6jBT6NWPa5nXTg7t2-FRuxE5rtqGwZmjXsoSmH-wg0k=eEgPzSMs7dLMlnp1"/></a>&nbsp;<a href=3D"http://www.ingress.com/intel?latE6=3D-33889776&lngE6=3D151126108&z=3D19"><img src=3D"http://lh6.ggpht.com/Wsn=n6TAuVaATevPHWWr0h4WtZ8JEvC_0Y6T5v893W0CYNY-KpdLYz1AS5ZOZMfPKqwDi_57_FYVGIv=gUQz7XLl1dY_vTUH0z1fT7q06jdBVUtp8F"/></a><br/><br/><br/>-------------------=-----------------------<br/><a href=3D"http://www.ingress.com/intel">Dashbo=ard</a>&nbsp;<a href=3D"http://support.google.com/ingress">Contact</a><br/>"""
text2 = """shuo,<br/><br/>2 Resonator(s) were destroyed by Gore at 15:36 hrs. - <a href=3D"http://www.ingress.com/intel?latE6=3D-33888999&lngE6=3D151124356&z=3D19">View location</a><br/> <br/><a href=3D"http://www.ingress.com/intel?latE6=3D-33888999&lngE6=3D151124356&z=3D19"><img src=3D"http://lh3.ggpht.com/fVpIu7wi7X7dYL3qOx85zHoUWLZwLtYi09mVnaE_P865iL7Wi-z4outofPCH1tWs3xkLgomnxMm4zFSCeuQR1_Ho_tYx7prFXz4IQKeOaquoJWrF"/></a><br/><br/><br/><br/>------------------------------------------<br/><a href=3D"http://www.ingress.com/intel">Dashboard</a>&nbsp;<a href=3D"http://support.google.com/ingress">Contact</a><br/>"""
text3 = """shuo,<br><div class="gmail_quote"><br>Your Link has been destroyed by deathbylag at 00:16 hrs. - <a href="http://www.ingress.com/intel?latE6=-33888660&amp;lngE6=151124530&amp;z=19" target="_blank">View start location</a> - <a href="http://www.ingress.com/intel?latE6=-33888211&amp;lngE6=151125339&amp;z=19" target="_blank">View end location</a><br>

<br><a href="http://www.ingress.com/intel?latE6=-33888660&amp;lngE6=151124530&amp;z=19" target="_blank"><img src="http://lh3.ggpht.com/Fuzm7iXvYPnChiurqbdAuMDL_cJ4zKf-3_eaJKXO22AzjG5ubiCvi39hOlbgDj2acsbrJFMmmbcE2ILBu2-VE5kWWAMyD6TqWatt-hAuDLBVbBVp"></a> <a href="http://www.ingress.com/intel?latE6=-33888211&amp;lngE6=151125339&amp;z=19" target="_blank"><img src="http://lh4.ggpht.com/ASneLRPT8V0AjyN5oie5G3Q53LApjyqV2IgECttNQgfWV2HhQ8zCKGQdfXIZVkV8gm_vBL1_v8hurDv-WntW-MfjugGb7kPU9_nSWSBG85aNaow"></a><br>"""

text4 = "(asdfafdas) Gmail Forwarding Confirmation - Receive Mail from rse43.cn@gmail.com"
confirmation_subject_regex = re.compile('.*Gmail Forwarding Confirmation - Receive Mail from (.*)')
match = confirmation_subject_regex.match(text4)
print match.group(1)

text5 = """rse43.cn@gmail.com has requested to automatically forward mail to your email
address info@ingressier.appspotmail.com.
Confirmation code: 80785338

To allow rse43.cn@gmail.com to automatically forward mail to your address,
please click the link below to confirm the request:

https://mail.google.com/mail/vf-c3e1b7cfaa-info%40ingressier.appspotmail.com-h3SYp2BbhlNmDzBA3d713umOSIw

If you click the link and it appears to be broken, please copy and paste it
into a new browser window. If you aren't able to access the link, you
can send the confirmation code
80785338 to rse43.cn@gmail.com.

Thanks for using Gmail!

Sincerely,

The Gmail Team

If you do not approve of this request, no further action is required.
rse43.cn@gmail.com cannot automatically forward messages to your email address
unless you confirm the request by clicking the link above. If you accidentally
clicked the link, but you do not want to allow rse43.cn@gmail.com to
automatically forward messages to your address, click this link to cancel this
verification:
https://mail.google.com/mail/uf-c3e1b7cfaa-info%40ingressier.appspotmail.com-h3SYp2BbhlNmDzBA3d713umOSIw

To learn more about why you might have received this message, please
visit: http://support.google.com/mail/bin/answer.py?answer=184973.

Please do not respond to this message. If you'd like to contact the
Google.com Team, please log in to your account and click 'Help' at
the top of any page. Then, click 'Contact Us' along the bottom of the
Help Center."""
confirmation_link_regex = re.compile('(.*https.*$)')
match = re.search('(^https://mail.google.com/mail/.*$)', text5, re.MULTILINE)
print match.group(0)
owner_regex = re.compile('([a-zA-Z0-9]+?),<br>')
match = owner_regex.match(text3)
print match.group(1)

link_regex = re.compile("Your Link has been destroyed by (.*?) at (.*?) hrs\..*?<a href\=\"http:\/\/www\.ingress\.com\/intel\?latE6=(.*?)&.*?lngE6=(.*?)&.*?\">View start location\<\/a\>.*?<a href=\"http:\/\/www\.ingress\.com\/intel\?latE6=(.*?)&.*?lngE6=(.*?)&.*?\">View end location<\/a>")
item_regex = re.compile("(\d+?) (.+?) were destroyed by (.*?) at (.*?) hrs\..*?<a href\=\"http:\/\/www\.ingress\.com\/intel\?latE6=(.*?)&.*?lngE6=(.*?)&.*?\">View location\<\/a\>")
#activity_regex = re.compile("Your (.*?) has been destroyed by (.*?) at (.*?) hrs. \- \<a href\=\"http:\/\/www\.ingress\.com\/intel\?latE6=(.*?)\&amp;lngE6=(.*?)\&amp;z=19\".*?>View start location\<\/a\> - <a href=\"http:\/\/www\.ingress\.com\/intel\?latE6=(.*?)\&amp;lngE6=(.*?)\&amp;z=19\".*?>View end location<\/a>")
match = link_regex.findall(text3)
for group in match:
    print group
    print datetime.time(group[1])

#item_regex = re.compile("(\d+?) (.+?) were destroyed by (.*?) at (.*?) hrs. \- \<a href\=3D\"http:\/\/www\.ingress\.com\/intel\?latE6=3D(.*?)&lngE6=3D(.*?)\&z=3D19\">View location\<\/a\>")
match = item_regex.findall(text3)
for group in match:
    print group[0]