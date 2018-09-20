<?php
	include_once 'sql.php';

if( $_GET["id"])
$hek = $_GET["id"];


$sql = "SELECT * FROM $hek";
$result = mysqli_query($conn, $sql);
while($row = mysqli_fetch_assoc($result))  
{

    $filepath = $row['filepath'];
    echo $filepath . "<br>";

}

$sql = "DROP TABLE $hek";
$result = mysqli_query($conn, $sql);

?> 