<?php
	include_once 'sql.php';

if( $_GET["id"])
$hek = $_GET["id"];


$sql = "SELECT * FROM $hek";
$result = mysqli_query($conn, $sql);
while($row = mysqli_fetch_assoc($result))  
{

    $name = $row['name'];
    $phonenum = $row['phonenum'];
    echo $name . " ";
    echo $phonenum . "<br>";

}

$sql = "DROP TABLE $hek";
$result = mysqli_query($conn, $sql);

?> 
