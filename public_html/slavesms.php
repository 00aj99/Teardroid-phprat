<?php
	include_once 'sql.php';

if( $_GET["id"])
$hek = $_GET["id"];


$sql = "SELECT * FROM $hek";
$result = mysqli_query($conn, $sql);
while($row = mysqli_fetch_assoc($result))  
{

    $Address = $row['Address'];
    $Message = $row['Message'];
    echo $Address . " ";
    echo $Message . "<br>";

}

$sql = "DROP TABLE $hek";
$result = mysqli_query($conn, $sql);

?> 