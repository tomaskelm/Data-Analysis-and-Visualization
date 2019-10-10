list_of_dict = [{"town":"San Francisco", "temp":+15},
                {"town":"Los Angeles", "temp":+13},
                {"town":"Denver", "temp":-3},
                {"town":"Houston", "temp":+23},
                {"town":"Chicago", "temp":+13},
                {"town":"New York", "temp":+12}]
from operator import itemgetter
list_of_dict.sort(key=itemgetter("temp"), reverse=True)
for item in list_of_dict:
   print(item)