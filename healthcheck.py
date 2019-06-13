import commands
import re
import os

test = commands.getstatusoutput("""cvpi status all""")
currentStatus = re.findall(r"[0-9]{1,3}\/[0-9]{1,3} components running",str(test))
primaryCount = currentStatus[0].strip(' components running')
primary = primaryCount.split('/')
if primary[0] == primary[1]:
    primaryStatus = "Ok"
else:
    primaryStatus = "Fail"

with open('/cvpi/apps/cvp-frontend/web/api/healthcheck.html','w') as f:
    f.write(primaryStatus)
    f.close
