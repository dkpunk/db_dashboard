import plotly
import plotly.graph_objs as go
import sys
import json
import os
from datetime import datetime
from dateutil.parser import parse
import csv
from itertools import islice
import operator
min_date=sys.argv[3].strip()
min_hr=sys.argv[4].strip()
max_date=sys.argv[5].strip()
max_hr=sys.argv[6].strip()
region=sys.argv[2]
dbfile=sys.argv[1]
plot_dict1=[]
date_arr=[]
min_line=0
plot_dict1.append(["time","Active Session"])
with open("./databasefiles/"+region+"/"+dbfile) as csvfile:
	reader = csv.reader(csvfile,delimiter=',')
	data = [ r for r in reader ]
	max_line=len(data)
	data.pop(0)
	data1=sorted(data,key=operator.itemgetter(0,1))
count=0
for element in data1:
  date_arr.append(str(element[0])+"  "+str(element[1])+" hrs")
  if(element[0].strip()==min_date and int(element[1].strip())==int(min_hr)):
	min_line=count	
  	#print "minfound"+str(element)
  if(element[0].strip()==max_date and int(element[1].strip())==int(max_hr)):
	max_line=count
	#print "maxfound"+str(element)
  count=count+1
date_arr=list(set(date_arr))
#print min_line
#print max_line
#print data1[min_line]
#print data1[max_line]
for element in data1[min_line:max_line]:
    try:
	tmpdate=str(element[0])+"  "+str(element[1])+" hrs"
	tmpasession=float(element[2].strip("\r\n"))
	plot_dict1.append([tmpdate,tmpasession])
    except ValueError,e:
	tmpasession=0
'''xlist=[]
ylist=[]
plot_dict2=sorted(plot_dict,key=plot_dict.get)
print plot_dict2
#xlist=tuple(plot_dict.keys())
#ylist=tuple(plot_dict.values())
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(xlist, ylist)
fig.savefig(cobname+'.png')   # save the figure to file
'''

print '''<html>
  <head>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["columnchart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
	var data = google.visualization.arrayToDataTable('''
print plot_dict1
print ''');

        var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
        chart.draw(data, {width: 3000, height:500, is3D: true, title: 'Database Performance'});
      }
    </script>
  </head>

  <body>
    <div id="chart_div" width="80%" height="20%"></div>
  </body>
</html>
'''



'''
plotly.offline.plot({
    "data": [go.Scatter(x=xlist,y=ylist)],
    "layout": go.Layout(title="MQ Trends of"+cobname)
}, auto_open=True,filename=cobname+".html")
'''
