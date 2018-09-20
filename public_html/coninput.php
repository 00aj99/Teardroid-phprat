<?php
	include_once 'sql.php';

if( $_GET["id"] || $_GET["name"] || $_GET["phonenum"])
$hek = $_GET["id"];
$NAME = $_GET["name"];
$phonenum = $_GET["phonenum"];

{
  
    $query = "SELECT * FROM $hek";
	$result = mysqli_query($conn, $query);

	if(empty($result)) {
    	            $sql = "CREATE TABLE $hek (
                          name varchar(255) NOT NULL,
                          phonenum varchar(255) NOT NULL
                          );";
                	$res = mysqli_query($conn, $sql);
                	echo $res;

            }

$sql = "INSERT INTO $hek (name, phonenum) VALUES ('$NAME' ,'$phonenum')";   

        }
        if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>