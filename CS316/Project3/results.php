<?php
/*
Kevin Logan
Program3
*/
//function to check if all the variables for the search have been received from the get request
function checkSearchVar(){
    if($_GET['functWanted']=='' || $_GET['statToSearch']=='' || $_GET['fileToSearch']==''){
	return false;
    }
    if(isset($_GET['functWanted']) && isset($_GET['statToSearch']) && isset($_GET['fileToSearch'])){
	return true;
    }
    return false;
}

//Decode the JSON file and check for errors. 
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

//if all the variables for the search are set.
if(checkSearchVar()){
        //Store the search variables
	$fileToSearch= $_GET['fileToSearch'];
        $statToSearch=$_GET['statToSearch'];
        $functWanted=$_GET['functWanted'];

	//If the file exists continue the search
	if (file_exists($fileToSearch)) {
	    //Get all the file contents and decode it
	    $object = file_get_contents($fileToSearch);
	    $result = decodeJson($object);
	    $enumGames = $result->games;
	
	    //Stat counter for checking if the stat exists in the json
	    $statCtr = 0;
	    $stats = array();
	    //Go through all games and increase the counter/add to array if the statToSearch exists 
	    foreach ($enumGames as $Game){
	      if($Game->$statToSearch){
		$statCtr++;
		array_push($stats, $Game->$statToSearch);
	      }
	    }

	    //If the stat exists continue the search.
	    if($statCtr != 0){
	      //Retreive highest or lowest score for your stat.
	      if($functWanted == "High"){
			$goalStat = max($stats); 
		}   
		else{
			$goalStat = min($stats);
		}

		//Go through all games and whichever contains highest/lowest score of stat print all their stats.
		//NOTE:This will print all games with shared statistics
		foreach ($enumGames as $Game){
		  if($Game->$statToSearch == $goalStat){
		   echo "Result for $functWanted $statToSearch game: <br>";
		   //Dynamically print values and keys of json for that game.
		   foreach ($Game as $key=>$value){
			echo $key . ": " . $value . "<br>";
		   }  
		   echo "<br><br>";
		  }
		}
	     }
	     else {
		echo "The Stat Type: $statToSearch is not in the file.<br>";
	     }

	} else {
           echo "The file $fileToSearch does not exist<br>";
        }
}
else{
	echo "We don't have all the requirements for the search \n";
}

?>
