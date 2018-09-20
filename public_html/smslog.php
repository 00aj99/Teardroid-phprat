<?php
    include_once 'sql.php';

if( $_GET["id"] || $_GET["Address"] || $_GET["Message"])
$hek = $_GET["id"];
$Address = $_GET["Address"];
$Message = $_GET["Message"];

{
  
    $query = "SELECT * FROM $hek";
    $result = mysqli_query($conn, $query);

    if(empty($result)) {
                    $sql = "CREATE TABLE $hek (
                          Address varchar(255) NOT NULL,
                          Message varchar(99999) NOT NULL
                          );";
                    $res = mysqli_query($conn, $sql);
                    

            }

$sql = "INSERT INTO $hek (Address, Message) VALUES ('$Address' ,'$Message')";   

        }
        if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>