**Hadoop Cloud HW4**

**command to run mapper and reducer:**

hadoop fs -cat /data/nyc/nyc-traffic.csv | python mapper.py | sort | python reducer.py


**add files and directories to hadoop:**

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file /home/beckerau/mapper.py -mapper /home/beckerau/mapper.py -file /home/beckerau/reducer.py -reducer /home/beckerau/reducer.py -input /data/nyc/nyc-traffic.csv -output /user/beckerau/cloud

**output:**

AMBULANCE       3713

BICYCLE 24153

BUS     25871

FIRE TRUCK      1333

LARGE COM VEH(6 OR MORE TIRES)  27981

LIVERY VEHICLE  17775

MOTORCYCLE      10029

OTHER   51360

PASSENGER VEHICLE       1005161

PEDICAB 123

PICK-UP TRUCK   26281

SCOOTER 534

SMALL COM VEH(4 TIRES)  30048

SPORT UTILITY / STATION WAGON   363210

TAXI    63892

UNKNOWN 105481

VAN     51666
