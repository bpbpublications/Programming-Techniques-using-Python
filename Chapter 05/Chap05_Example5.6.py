import time
from imp import reload
import safetyprecautions
print("I am inside testmodule")
print("I am sleeping for 40 secs")
print("--------------------------")
time.sleep(40)
reload(safetyprecautions)
print("This is displayed after updation of module")
