# -*- coding: utf-8 -*-
import re

valid_strings = [u"ABC ✈️ XYZ",
                 u"DDD✈️BBB"]

invalid_strings = [u"ABC 💩 XYZ",
                   u"ddd✈️Bbb",
                   u"ABC ABC"]

p = re.compile(u"[A-Z][A-Z][A-Z](\\s*)✈️(\\s*)[A-Z][A-Z][A-Z]")

for s in valid_strings:
    print s, p.match(s)

for s in invalid_strings:
    print s, p.match(s)
