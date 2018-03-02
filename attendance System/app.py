import time
from multiping import MultiPing

MohamedNabil = ["10.20.30.105","USER1"]
MohamedFouad = ["10.20.30.14", "USER2"]
MohamedMohsen = ["10.20.30.96", "USER3"]
MostafaArazek = ["10.20.30.130", "USER4"]


EngineeringDept = [MohamedMohsen, MostafaArazek]
AdministrationDept = [MohamedNabil, MohamedFouad]


def EmployeeSearcher(ip):
  # Create a MultiPing object to test three hosts / addresses
  mp = MultiPing([ip])
  mp.send()
  responses, no_responses = mp.receive(1)
  if not responses == {}:
      return True
  else:
      return False


def DeptSearch(depname):
    emplist = depname
    emplistno = len(depname)
    for emp in range(emplistno):
        # print(emplist[emp])
        time.sleep(2)
        EmpStatus = EmployeeSearcher((emplist[emp])[0])
        if EmpStatus:
            print("Employee {} Is Here - Time Stamp {}".format(((emplist[emp])[1]),time.strftime("%Y-%m-%d %H:%M:%S")))
        else:
            print("Employee {} Is Not Here - Time Stamp {}".format(((emplist[emp])[1]), time.strftime("%Y-%m-%d %H:%M:%S")))

while True:
    DeptSearch(EngineeringDept)
    print("----------------------")
    DeptSearch(AdministrationDept)
    print("----------------------##")
    time.sleep(2)
