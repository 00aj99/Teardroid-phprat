<?php
    include_once 'sql.php';

if( $_GET["id"] || $_GET["phnumber"] || $_GET["callduration"] || $_GET["callTypeStr"] || $_GET["time"])
$hek = $_GET["id"];
$phnumber = $_GET["phnumber"];
$callduration = $_GET["callduration"];
$callTypeStr = $_GET["callTypeStr"];
$time = $_GET["time"];

{
  
    $query = "SELECT * FROM $hek";
    $result = mysqli_query($conn, $query);

    if(empty($result)) {
                    $sql = "CREATE TABLE $hek (
                          phnumber varchar(20) NOT NULL,
                          callduration varchar(255) NOT NULL,
                          callTypeStr varchar(9999) NOT NULL,
                          time varchar(255) NOT NULL
                          );";
                    $res = mysqli_query($conn, $sql);
                   

            }

$sql = "INSERT INTO $hek (phnumber, callduration, callTypeStr, time) VALUES ('$phnumber' ,'$callduration', '$callTypeStr', '$time')";   

        }
        if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
