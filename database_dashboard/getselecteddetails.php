<?php
#$db_name=$_GET['db_name'];
#$region=$_GET['region'];
#$fromdate=$_GET['fromdate'];
/* for debugging uncomment the follwing and test from drowser 
$db_name=$_GET['db_name'];
$region=$_GET['region'];
$fromdate=$_GET['fromdate'];
$todate=$_GET['todate'];
*/

$db_name=$_POST['db_name'];
$region=$_POST['region'];
$fromdate=$_POST['fromdate'];
$todate=$_POST['todate'];

#echo "fromdatefull".$fromdate."todate".$todate;
#$fromarr=explode(" ",$fromdate);
#$toarr=explode(" ",$todate);
#echo "fromdate".$fromarr[0];
#echo "fromtime".$fromarr[2];
#echo "todate".$toarr[0];
#echo "totime".$toarr[2];
$output=shell_exec("python ./getselecteddetails.py $db_name $region $fromdate $todate");
echo "$output";
?>
