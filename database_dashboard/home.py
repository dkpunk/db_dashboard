import requests
import json
import re
import os
import csv
from collections import Counter
import operator
print '''
<!DOCTYPE html>
<html>
<head>
<title>Database Details</title>
<style>
table {
  border-collapse: collapse;
}

table, th, td {
  border: 1px solid black;
}</style>
</head><body>'''
def getavg(filename):
	total=0
	row_count=0
	with open(filename,"rb") as f:
		reader=csv.reader(f)
		data=[r for r in reader ]
		data.pop(0)
		data_list=data
		row_count=0
		max_count=len(data_list)
		for row in data_list[max_count-3:max_count]:
#			print row
			try:
				n=float(row[2])
				total=total+n
				row_count=row_count+1
			except ValueError:
				row_count=row_count-1
	return(float(total/row_count))
				
				
	
#print '<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for database names" title="Type in a name">'
for region in os.listdir("./databasefiles/"):
	print "<h3>Database details of "+region+"</h3>"
	print "<table id=\"customers\" class=\"table table-bordered\" cellspacing=\"0\" style=\"width:100%\">"
	print "<thead><tr><th>Database Name<br></th><th> Active Session Trends</th><th>Active Sesson By Weightclass</th><th>Logical Reads</th></tr></thead><tbody>"
	for (dirpath,dirnames,filenames)in os.walk("./databasefiles/"+region+"/actsession"):
		for dbfiles in filenames:
		 	dbtemp=dbfiles.split("_")
			dbname=dbtemp[1].split(".")
			avgsession=getavg("./databasefiles/"+region+"/actsession/"+dbfiles)
			#print "<td>"+str(dbname[0])+"</td>"
			print "<tr><td align=\"center\">"+dbname[0]+"</td><td align=\"center\"><a style='color:white' target=\"_blank\" href=\"getactivesession.php?region="+region+"&db_name="+dbfiles+"\"><img src=\"graph.png\" style=\"width:40px; height:40px\" title=\"Statistics\"></a></td><td align=\"center\"><a style='color:white' target=\"_blank\"  href=\"getalldetails.php?region="+region+"&db_name="+dbname[0]+"\"><img src=\"graph.png\" style=\"width:40px; height:40px\" title=\"Statistics\"></a></td><td align=\"center\"><a style='color:white' target=\"_blank\"  href=\"getlogicalread.php?region="+region+"&db_name="+dbname[0]+"\"><img src=\"graph.png\" style=\"width:40px; height:40px\" title=\"Statistics\"></a></td></tr>"
	print "</tbody></table>"
print '''<script>
function myFunction() {
  // Declare variables 
  var input, filter, table, tr, td, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("customers");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
}
} 
</script>
<script src="jquery-1.12.4.js"></script> 
     <script src="jquery.dataTables.min.js"></script>
     <script src="dataTables.bootstrap.min.js"></script>
      <link href="bootstrap.min.css" rel="stylesheet"> 
      <link href="dataTables.bootstrap.min.css" rel="stylesheet">
      


    <script>


$(document).ready(function() {
     $('#customers').DataTable();
} );


</script></body></html>'''
	
	
