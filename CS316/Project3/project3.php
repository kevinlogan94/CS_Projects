<?php
/*

Kevin Logan
Program 3

*/
//function to check if all the variables for the search have been received from the get request
function decodeJson($object) {
    $result = json_decode($object);
    switch (json_last_error()) {
        case JSON_ERROR_NONE:
        break;
        case JSON_ERROR_DEPTH:
            echo ' - Maximum stack depth exceeded';
        break;
        case JSON_ERROR_STATE_MISMATCH:
            echo ' - Underflow or the modes mismatch';
        break;
        case JSON_ERROR_CTRL_CHAR:
            echo ' - Unexpected control character found';
        break;
        case JSON_ERROR_SYNTAX:
            echo ' - Syntax error, malformed JSON';
        break;
        case JSON_ERROR_UTF8:
            echo ' - Malformed UTF-8 characters, possibly incorrectly encoded';
        break;
        default:
            echo ' - Unknown error';
        break;
    }

    return $result;
}

?>

<!DOCTYPE html>
<html>
<head>

<title>Kevin Logan Program 3</title>
</head>
<body>

<?php
//read in UKgames.json and decode it to dynamically load the selects
$object = file_get_contents("UKgames.json"); 
$result = decodeJson($object);

$enumFiles = $result->files;
$enumStats = $result->stats;
?>


<h1>Kevin Logan Program 3</h1>

<form action='results.php' method='get'>

<select name='fileToSearch'>
  <?php
   //Dynamically load fileToSearch with files to search based off the json.
   foreach ($enumFiles as $File){
   echo "<option value=" . $File . ">" . $File . "</option>"; 
  } ?>
</select>
<br>
<select name='statToSearch'>
  <?php
   //Dynamically load statToSearch based off the json.
   foreach ($enumStats as $Stat){
   echo "<option value=" . $Stat . ">" . $Stat . "</option>";
  } ?>
</select>
<br>
<select name='functWanted'>
  <option value="High">High</option>
  <option value="Low">Low</option>
</select>
<br>
<input type="submit" value="Submit">
</form>

</body>
</html>
