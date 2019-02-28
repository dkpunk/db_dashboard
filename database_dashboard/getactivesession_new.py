import plotly
import plotly.graph_objs as go
import sys
import json
import os
from datetime import datetime
from dateutil.parser import parse
import csv
region=sys.argv[2]
dbfile=sys.argv[1]
plot_dict1=[]
date_arr=[]
plot_dict1.append(["time","Active Session"])
with open("./databasefiles/"+region+"/"+dbfile) as csvfile:
	reader = csv.reader(csvfile,delimiter=',')
	data = [ r for r in reader ]
	data.pop(0)
for element in data:
    try:
	tmpdate=str(element[0])+"  "+str(element[1])+":00:00"
	date_arr.append(tmpdate)
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
<style>
.iframe-container {
  overflow: hidden;
  padding-top: 56.25%;
  position: relative;
}

.iframe-container iframe {
   border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;
}
</style>
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
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
<form method="post">
From : <select id="fdt">'''
for selectelem in date_arr:
        print "<option value=\"{0}\">{0}</option>".format(selectelem)
print '''</select>
        To : <select id="tdt">'''
for selectelem in date_arr:
        print "<option value=\"{0}\">{0}</option>".format(selectelem)
print '''</select></form>
    <button onclick="myFunction()">Submit</button>
    <div id="chart_div" width="80%" height="20%"></div>
    <iframe name="iFrameName" id="test" width="2000" height="1000"></iframe>
     <script type="text/javascript">
	function myFunction(){
		var fdt=document.getElementById("fdt");
		var fdt_val=fdt.options[fdt.selectedIndex].value;
		var tdt=document.getElementById("tdt");
		var tdt_val=tdt.options[tdt.selectedIndex].value;
		var region="'''+region+'''";
		var dbfile="'''+dbfile+'''";
		var json_var={ "region" : region,"db_name" :dbfile,"fromdate": fdt_val,"todate" : tdt_val};
		alert(fdt_val);
		
		$.ajax({
			type: 'POST',
			url : 'getselectedsession.php',
			data : (json_var),
			success: function(data){
				$('#chart_div').html(data);
				
				alert(data);
				var iframe = document.getElementById('test');
				var iframedoc = iframe.document;
        if (iframe.contentDocument)
            iframedoc = iframe.contentDocument;
        else if (iframe.contentWindow)
            iframedoc = iframe.contentWindow.document;
		if (iframedoc){
         // Put the content in the iframe
         iframedoc.open();
         iframedoc.writeln(data);
         iframedoc.close();
     } else {
        //just in case of browsers that don't support the above 3 properties.
        //fortunately we don't come across such case so far.
        alert('Cannot inject dynamic contents into iframe.');
     }
			},
			error : function(jq,status,message){
			alert("unable to fetch chart"+status+" Message "+message);}
		});
	}
	</script>
  </body>
</html>
'''



'''
plotly.offline.plot({
    "data": [go.Scatter(x=xlist,y=ylist)],
    "layout": go.Layout(title="MQ Trends of"+cobname)
}, auto_open=True,filename=cobname+".html")
'''
