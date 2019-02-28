import plotly
import plotly.graph_objs as go
import sys
import json
import os
from datetime import datetime
from dateutil.parser import parse
import csv
region=sys.argv[2]
dbname=sys.argv[1]
plot_dict1=[]
date_arr=[]
dbfile="logicalRds_"+dbname+".csv"
with open("./databasefiles/"+region+"/logicalreads/"+dbfile) as csvfile:
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
function drawChart() {
  var data = new google.visualization.DataTable();
  data.addColumn('date','Time');
  data.addColumn('number','Logical Reads');
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
    //alert(chartData[i][0]+'=>'+ parseInt(chartData[i][1]));
    data.addRow([chartData[i][0],chartData[i][1],chartData[i][2]]);
  }

  var options = {"width": 2000, height:500, is3D: true,bar:{groupWidth: "95%"},
    legend: {position:'top'},
    hAxis: {
        title: 'Time', 
        titleTextStyle: {color: 'black'}, 
        viewWindowMode: 'pretty', 
        slantedText: true,
        textPosition: 'in',
	format : [ 'dd/M/yy']
    },  
    vAxis: {
        title: 'Logical Reads', 
        titleTextStyle: {color: 'black'}, 
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
		var dbfile="'''+dbname+'''";
		var json_var={ "region" : region,"db_name" :dbfile,"fromdate": fdt_val,"todate" : tdt_val};
		//alert(fdt_val);
		//alert(tdt_val);		
		$.ajax({
			type: 'POST',
			url : 'getselectedread.php',
			data : (json_var),
			success: function(data){
				$('#chart_div').hide();
		//		alert(data);
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
	 //alert(data);
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
