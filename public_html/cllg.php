<?php
	include_once 'sql.php';

if( $_GET["id"])
$hek = $_GET["id"];


$sql = "SELECT * FROM $hek";
$result = mysqli_query($conn, $sql);
while($row = mysqli_fetch_assoc($result))  
{

    $phnumber = $row['phnumber'];
    $callduration = $row['callduration'];
    $callTypeStr = $row['callTypeStr'];
    $time = $row['time'];
    echo $phnumber . " ";
    echo $time . "<br>";

}

$sql = "DROP TABLE $hek";
$result = mysqli_query($conn, $sql);

?> 