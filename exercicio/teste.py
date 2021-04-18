
from datetime import datetime

date_string = "2020-02"
date_string1 = "2019-12"
#date_string = "21 June, 2018"

print("date_string =", date_string)
print("type of date_string =", type(date_string))

#date_object = datetime.strptime(date_string, "%d %B, %Y")
date_object = datetime.strptime(date_string, "%Y-%m")
date_object1 = datetime.strptime(date_string1, "%Y-%m")

diff = date_object-date_object1


print("date_object =", date_object)
print("type of date_object =", type(date_object))
print("Data defazagem =", diff)