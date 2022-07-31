"""составить грамотное регулярное выражение для поиска"""

import requests
import re
from collections import Counter

response = requests.get('http://www.columbia.edu/~fdc/sample.html').text
#result = re.match(r'.h3', response)
result = re.findall(r'<h3 .*?>(.*?)</h3>', response)
print(result)
