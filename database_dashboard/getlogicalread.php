<?php
$db_name=$_GET['db_name'];
$region=$_GET['region'];
$output=shell_exec("python ./getlogicalread.py $db_name $region");
echo "$output";
?>
