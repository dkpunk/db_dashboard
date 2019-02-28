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
min_hr_arr=sys.argv[4].strip().split(':')
min_hr=min_hr_arr[0]
max_date=sys.argv[5].strip()
max_hr_arr=sys.argv[6].strip().split(':')
max_hr=max_hr_arr[0]
region=sys.argv[2]
dbfile=sys.argv[1]
plot_dict1=[]
date_arr=[]
min_line=0
with open("./databasefiles/"+region+"/"+dbfile) as csvfile:
	reader = csv.reader(csvfile,delimiter=',')
	data = [ r for r in reader ]
	max_line=len(data)
	data.pop(0)
	data1=sorted(data,key=operator.itemgetter(0,1))
count=0
for element in data1:
  date_arr.append(str(element[0])+"  "+str(element[1]))
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
	tmpdate=str(element[0])+"  "+str(element[1])+":00:00"
	tmpasession=float(element[2].strip("\r\n"))
	plot_dict1.append([tmpdate,tmpasession])
    except ValueError,e:
	tmpasession=0

print '''<html>
  <head>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["columnchart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
var data = new google.visualization.DataTable();
  data.addColumn('date','Time');
  data.addColumn('number','Active Session');
  data.addColumn({type:'string', role:'interval'});
var datearray='''
print plot_dict1
print ''';
var arrlength=datearray.length;
          for(var i=0;i<arrlength;i++){
	      datearray[i].push(datearray[i][0]);
              datearray[i][0]=new Date(datearray[i][0]);
          }
    datearray.sort(function(a,b){
        return a[0]-b[0];
    })
    chartData=datearray;
  for (var i in chartData){
   // alert(chartData[i][0]+'=>'+ parseInt(chartData[i][1]));
    data.addRow([chartData[i][0],chartData[i][1],chartData[i][2]]);
  }

  var options = {"width": 2000, height:500, is3D: true,bar:{groupWidth: "95%"},
    legend: {position:'top'},

    hAxis: {
        title: 'Time',
        titleTextStyle: {color: 'black'},
        count: -1,
        viewWindowMode: 'pretty',
        slantedText: true,
        textPosition: 'in',
	format : [ 'dd/M/yy HH:mm:ss']
    },
    vAxis: {
        title: 'Active Sessions',
        titleTextStyle: {color: 'black'},
        count: -1
    },
    colors: ['#F1CA3A']
  };

  var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
  chart.draw(data, options);
}

google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawChart);
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
