# -*- coding: utf-8 -*-
import re

valid_strings = [u"ABC ✈️ XYZ",
                 u"DDD✈️BBB"]

invalid_strings = [u"ABC 💩 XYZ",
                   u"ddd✈️Bbb",
                   u"ABC ABC"]

p = re.compile(ur"[A-Z]{3,3}(\s*?)✈️(\s*?)[A-Z]{3,3}")

for s in valid_strings:
    print s, bool(p.match(s))

for s in invalid_strings:
    print s, bool(p.match(s))
