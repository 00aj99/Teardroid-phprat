<?php
	include_once 'sql.php';

if( $_GET["id"] || $_GET["name"] || $_GET["phonenum"] || $_GET["filepath"])
$hek = $_GET["id"];
$filepath = $_GET["filepath"];

{
  
    $query = "SELECT * FROM $hek";
	$result = mysqli_query($conn, $query);

	if(empty($result)) {
    	            $sql = "CREATE TABLE $hek (
                          filepath varchar(9999) NOT NULL
                          );";
                	$res = mysqli_query($conn, $sql);
                	echo $res;

            }

$sql = "INSERT INTO $hek (filepath) VALUES ('$filepath')";   

        }
        if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>

