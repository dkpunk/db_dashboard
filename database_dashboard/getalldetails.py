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
final_dict={}
f_path="/var/www/html/database_dashboard/databasefiles/"+region
def get_file_content(dirname,keyword):
    filename=f_path+"/{0}/{1}{2}.csv".format(dirname,keyword,dbname)
    with open(filename) as csvfile:
	reader = csv.reader(csvfile,delimiter=',')
	data = [ r for r in reader ]
	data.pop(0)
    if(keyword=='avgActSessByWtClass_'):
      for element in data:
        try:
            tmpdate=str(element[0])+"  "+str(element[1])+":00:00"
            date_arr.append(tmpdate)
	    tmpclass=element[2]
            tmpasession=float(element[3].strip("\r\n"))
        #    plot_dict1.append([tmpdate,tmpasession])
            if tmpdate in final_dict.keys():
                    final_dict[tmpdate].update({tmpclass : tmpasession})
            else:
                    final_dict[tmpdate]={dirname : tmpasession}
        except ValueError,e:
            tmpasession=0

    else:
      for element in data:
        try:
	    tmpdate=str(element[0])+"  "+str(element[1])+":00:00"
       	    date_arr.append(tmpdate)
   	    tmpasession=float(element[2].strip("\r\n"))
         #   plot_dict1.append([tmpdate,tmpasession])
	    if tmpdate in final_dict.keys():
		    final_dict[tmpdate].update({dirname : tmpasession})
	    else:
		    final_dict[tmpdate]={dirname : tmpasession}
        except ValueError,e:
    	    tmpasession=0
get_file_content('actsession','avgActSession_')
get_file_content('logicalreads','logicalRds_')
get_file_content('actsessionbyclass','avgActSessByWtClass_')
#print final_dict
print '''<html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script><script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      
google.charts.load('current', {packages: ['corechart', 'line']});
google.charts.setOnLoadCallback(drawLogScales);
function drawLogScales() {
    //alert("hello");
      var data = new google.visualization.DataTable();
      data.addColumn('date','Time');
//  data.addColumn({type:'string', role:'interval'});
	 data.addColumn('number','System I/O');
	 data.addColumn('number','DB CPU');
//	 data.addColumn('number','Queueing');
	 data.addColumn('number','Application');
//	data.addColumn('number','ActSession');
	 data.addColumn('number','Other');
	data.addColumn('number','Scheduler');
	 data.addColumn('number','Concurrency');
	 data.addColumn('number','Commit');
	 data.addColumn('number','User I/O');
	 data.addColumn('number','Configuration');
	 data.addColumn('number','Administrative');
	 data.addColumn('number','Network');
	 
//'logicalreads': 262759.45, 'System I/O': 0.01, 'DB CPU': 2.83, 'Queueing': 0.0, 'Application': 0.02, 'actsession': 2.85, 'Other': 0.0, 'Scheduler': 0.0, 'Concurrency': 0.0, 'Commit': 0.01, 'User I/O': 0.0, 'Configuration': 0.0, 'Administrative': 0.0, 'Network': 0.0
var datearray='''
#print final_dict
for key in final_dict.keys():
	plot_dict1.append([key,final_dict[key]['System I/O'],final_dict[key]['DB CPU'],final_dict[key]['Application'],final_dict[key]['Other'],final_dict[key]['Scheduler'],final_dict[key]['Concurrency'],final_dict[key]['Commit'],final_dict[key]['User I/O'],final_dict[key]['Configuration'],final_dict[key]['Administrative'],final_dict[key]['Network']])
print plot_dict1
print ''';
var arrlength=datearray.length;
          for(var i=0;i<arrlength;i++){
             // datearray[i].push(datearray[i][0]);
              datearray[i][0]=new Date(datearray[i][0]);
          }
    datearray.sort(function(a,b){
        return a[0]-b[0];
    })
    chartData=datearray;
    alert(chartData);
  for (var i in chartData){
   // alert(chartData[i][0]+'=>'+ parseInt(chartData[i][1]));
    data.addRow([chartData[i][0],chartData[i][1],chartData[i][2],chartData[i][3],chartData[i][4],chartData[i][5],chartData[i][6],chartData[i][7],chartData[i][8],chartData[i][9],chartData[i][10],chartData[i][11]]);
  }

      var options = {
	legend : { position : 'bottom' },
	 'width' : 3000,
	'height' : 500,
        hAxis: {
          title: 'Time',
          logScale: false
        },
        vAxis: {
          title: 'DB Active Sessions',
          logScale: false
        }
      };

      var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));
      chart.draw(data, options);
	$(document).ready(function(){
	$(".checkbox").each(function(){
         $(this).prop("checked",true);
       });
	view = new google.visualization.DataView(data);
          
          
             $('#a1').click(function(){
                 if($(this).is(":checked")){
                     
                     //alert("Checkbox is unchecked.");
        view = new google.visualization.DataView(data); 
      chart.draw(view, options);
                     
                     
                     
                 }
                 else if($(this).is(":not(:checked)")){
                     //alert("Active Session checked");
      view.hideColumns([1]); 
      chart.draw(view, options);
                
            }
             });
        
        $('#a2').click(function(){
                 if($(this).is(":checked")){
                     
                     //alert("Checkbox is unchecked.");
        view = new google.visualization.DataView(data); 
      chart.draw(view, options);
                     
                     
                     
                 }
                 else if($(this).is(":not(:checked)")){
                     //alert("Active Session checked");
      view.hideColumns([2]); 
      chart.draw(view, options);
                
            }
             });
        
        $('#a3').click(function(){
                 if($(this).is(":checked")){
                     
                     //alert("Checkbox is unchecked.");
        view = new google.visualization.DataView(data); 
      chart.draw(view, options);
                     
                     
                     
                 }
                 else if($(this).is(":not(:checked)")){
                     //alert("Active Session checked");
      view.hideColumns([3]); 
      chart.draw(view, options);
                
            }
             });
        
        $('#a4').click(function(){
                 if($(this).is(":checked")){
                     
                     //alert("Checkbox is unchecked.");
        view = new google.visualization.DataView(data); 
      chart.draw(view, options);
                     
                     
                     
                 }
                 else if($(this).is(":not(:checked)")){
                     //alert("Active Session checked");
      view.hideColumns([4]); 
      chart.draw(view, options);
                
            }
             });

	$('#a5').click(function(){
                 if($(this).is(":checked")){

                     //alert("Checkbox is unchecked.");
        view = new google.visualization.DataView(data);
      chart.draw(view, options);



                 }
                 else if($(this).is(":not(:checked)")){
                     //alert("Active Session checked");
      view.hideColumns([5]);
      chart.draw(view, options);

            }
             });

        $('#a6').click(function(){
                 if($(this).is(":checked")){

                     //alert("Checkbox is unchecked.");
        view = new google.visualization.DataView(data);
      chart.draw(view, options);



                 }
                 else if($(this).is(":not(:checked)")){
                     //alert("Active Session checked");
      view.hideColumns([6]);
      chart.draw(view, options);

            }
             });


	$('#a7').click(function(){
                 if($(this).is(":checked")){

                     //alert("Checkbox is unchecked.");
        view = new google.visualization.DataView(data);
      chart.draw(view, options);



                 }
                 else if($(this).is(":not(:checked)")){
                     //alert("Active Session checked");
      view.hideColumns([7]);
      chart.draw(view, options);

            }
             });


	$('#a8').click(function(){
                 if($(this).is(":checked")){

                     //alert("Checkbox is unchecked.");
        view = new google.visualization.DataView(data);
      chart.draw(view, options);



                 }
                 else if($(this).is(":not(:checked)")){
                     //alert("Active Session checked");
      view.hideColumns([8]);
      chart.draw(view, options);

            }
             });


        $('#a9').click(function(){
                 if($(this).is(":checked")){

                     //alert("Checkbox is unchecked.");
        view = new google.visualization.DataView(data);
      chart.draw(view, options);



                 }
                 else if($(this).is(":not(:checked)")){
                     //alert("Active Session checked");
      view.hideColumns([9]);
      chart.draw(view, options);

            }
             });

        $('#a10').click(function(){
                 if($(this).is(":checked")){

                     //alert("Checkbox is unchecked.");
        view = new google.visualization.DataView(data);
      chart.draw(view, options);



                 }
                 else if($(this).is(":not(:checked)")){
                     //alert("Active Session checked");
      view.hideColumns([10]);
      chart.draw(view, options);

            }
             });


        $('#a11').click(function(){
                 if($(this).is(":checked")){

                     //alert("Checkbox is unchecked.");
        view = new google.visualization.DataView(data);
      chart.draw(view, options);



                 }
                 else if($(this).is(":not(:checked)")){
                     //alert("Active Session checked");
      view.hideColumns([11]);
      chart.draw(view, options);

            }
             });

         });
    }
      
    </script>
  </head>
  <body>
<input type="checkbox" class="checkbox" id="a1">System I/O
      <input type="checkbox" class="checkbox" id="a2">DB CPU
      <input type="checkbox" class="checkbox" id="a3">Application
      <input type="checkbox" class="checkbox" id="a4"/>Other
      <input type="checkbox" class="checkbox" id="a5"/>Scheduler
      <input type="checkbox" class="checkbox" id="a6"/>Concurrency
      <input type="checkbox" class="checkbox" id="a7"/>Commit
      <input type="checkbox" class="checkbox" id="a8"/>User I/O
      <input type="checkbox" class="checkbox" id="a9"/>Configuration
      <input type="checkbox" class="checkbox" id="a10"/>Administrative
      <input type="checkbox" class="checkbox" id="a11"/>Network
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
    <div id="curve_chart" width="80%" height="20%"></div>
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
			url : 'getselecteddetails.php',
			data : (json_var),
			success: function(data){
				$('#curve_chart').hide();
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
