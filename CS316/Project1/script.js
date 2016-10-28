/*
CS316 program 1
Student: Kevin Logan

WINNING PERCENTAGE - Usually lands between 54-60%. It also shows up in the winning percentage input on the 
webpage after 1000runs.

*/
//****************************** GLOBAL VARIABLES ***********************************************
// DSIZE is size of deck: 52 for normal deck
// Note: do not hardcode deck size. Use this variable
// to simplify my (and your) testing
var DSIZE = 52; // size of deck
var card = new Array(DSIZE); // shuffled deck
var cardstart = new Array(DSIZE); // starting deck in order
var cc; // index into card array during play
var dealpressed = 0;    // deal button has been pressed
var mycards = 0;
var dlcards = 0;
// Put other global variables here ***********************************************************************
shuffle();   // start with new deal
// shuffle
// This is one way to create a shuffled deck
// reshuffle the cards, put in card array
// Preconditions:
//	New Deal button pressed
// Postconditions:
//	Card array filled and shuffled

function shuffle() {  
	// cardstart is unshuffled 1,2,3....
	// card 1 is ace of clubs (1.png)
	// card 2 is ace of spades (2.png)
	// card 52 is 2 of diamonds (52.png)
	for (var i = 0; i < DSIZE;i++) {
		cardstart[i] = i+1;
	}
	// select card randomly from cardstart and put in card
	var randcard; // randomly selected card 
	for (var j = 0; j < DSIZE; j++) {
		randcard = Math.round(Math.random() * (DSIZE - j - 1)); // choose card
		card[j] = cardstart[randcard]; // store random card
		cardstart.splice(randcard, 1); // pack array
	}  
	cc = 0;              // index into card array
}

// resetdata
// reset all variables, screen fields to start fresh
function resetdata() {
        dealpressed=0;
        shuffle();
        document.getElementById("mycards").innerHTML = "";
        document.getElementById("dlcards").innerHTML = "";
	document.getElementsByName("myscore")[0].value = "";
	document.getElementsByName("opscore")[0].value = "";
        document.getElementsByName("myresult")[0].innerHTML = "";
	document.JForm.winning.value = "";
	document.JForm.myresult.value = "";
}

// calculate
// calculate value of card
// Preconditions:
//	Card passed
//	1 <= card <= 52
// Postconditions:
//	Card value returned
function calculate(card) {
var value; // numerical value of card
	if (card <= 4) {    // ace
		value = 11;
		return value; 
	}
	if (card <= 20) {   // face card or 10
		value = 10;
		return value;
	}
	if (card <= 24) {  // 9, and so forth
		value = 9;
		return value;
	}    
	if (card <= 28) {
		value = 8;
		return value;
	}      
	if (card <= 32) {
		value = 7;
		return value;
	}    
	if (card <= 36) {
		value = 6;
		return value;
	}    
	if (card <= 40) {
		value = 5;
		return value;
	}    
	if (card <= 44) {
		value = 4;
		return value;
	}    
	if (card <= 48) {
		value = 3;
		return value;
	}   
	value = 2;          // only 2 left
	return value; 
}

/*hit function for adding another card to your hand
  Parameter: User - this can be either 'me' or 'dealer' depending on who is hitting to add a card to their hand.
*/
  function gethit(user) {
    var hand;
    //Check the user
    if(user == 'dealer') {
      hand = dlcards;
    } 
    else {
      hand = mycards;
    }
    var handamount = hand.length; 
    if(handamount >= 2) {
      var cardnum = card[cc++];
      //if the card in my hand exists
      if(cardnum != undefined) {
        hand.push("<img src = '"+cardnum+".png' />");
        //output the new cards to the appropriate user.
        if(user != 'dealer') {
          document.getElementById("mycards").innerHTML = hand;
        }
        else {
          document.getElementById("dlcards").innerHTML = hand;
        }
        getscore(user);
      }
      else {
        //Alert to shuffle
        alert("you are out of cards! Please reshuffle and try again!");
      }
    }
    else {
      //If somehow to the dealorhit function doesn't work and there isn't a deal. 
      //Report the user must deal.
      alert("You must deal before you can hit!");
    }
  }

/*Function Deal/hit button
  Decides whether the button should produce a deal or hit.
*/ 
 function dealorhit() {
    if(dealpressed == 0) {
      deal();
    } 
    else {
      gethit('me')
    }
  }

/*Function: getscore(user)
  Parameter: User - This is either 'dealer' or 'me'
  Retreives the score and puts it in the appropriate input depending on the user.
*/
  function getscore(user) {
    //Check the type of user.
    var hand;
    if(user == 'dealer') {
      hand = dlcards;
    }
    else {
      hand = mycards;
    }
    //Go through each card in the hand and add it to the score.
    var score = 0;
    for (var i = 0; i < hand.length; i++) {
      var cardtemp = hand[i].substring(hand[i].indexOf("=")+3, hand[i].indexOf("."));
      var tempadd = calculate(cardtemp);
      if(tempadd == 11 && (score + tempadd) > 21 ) {
        score += 1;
      }
      else {
        score += tempadd;
      }
    }
    //Print out the score into the appropriate input.
    if (user == 'dealer') {
       if (score > 21) {
         document.JForm.opscore.value = "Bust";
         document.JForm.myresult.value = "WIN";
         dealpressed=0;
       }
       else {
         document.JForm.opscore.value = score;
       }
    }
    else if (score > 21) {
      document.JForm.myscore.value = "BUST";
      document.JForm.myresult.value = "LOSS";
      dealpressed=0;
    }
    else {
      document.JForm.myscore.value = score;
    }
  }

 /*Function run1000
   Simulates the game of blackjack 1000times and reports your win% in the appropriate input.
 */
  function run1000() {
    var winctr = 0;
    var losectr = 0;
    var tiectr = 0;
    for (var i=0;i<1000;i++) {
 
      shuffle();   // start with shuffled deck
      
      deal();    // then deal 
      
      //If nobody not blackjack then do hit algorithm for 'me'
      if(dealpressed == 1) {
        var hitflag = hit(mycards, dlcards);
        //While the hit algorithm says true keep hitting.             
        while(hitflag == true) {
          gethit();
	  hitflag = hit(mycards, dlcards);
        }
        //Run the hit algorithm for the dealer
        run();
      }
      //If the game result is a win or tie add to the win counter.
      if(document.JForm.myresult.value == 'WIN' || document.JForm.myresult.value == 'PUSH/TIE') {
	winctr++;
      }
    }   
    // when done, update the win percentage
    document.JForm.winning.value = ((winctr/1000)*100);
 
  }
 
  // hit
  // Determine whether to take one more card
  // Preconditions:
  //    playerhand - array of card values
  //	dealerhand - array of card values
  // Postconditions:
  //    returns true: take another card
  //            false: do not take card
  //    For the input cards (playerhand[], dealerhand[])
  //    ace  11
  //    face card 10
  //    all others their value 
  function hit(playerhand, dealerhand) {
 	var opscore = getscore('dealer');
        var myscore = getscore('me');

	//If statement to decide if I should pull a card.
	if(((myscore < opscore) && (mycards.length < 4) && (myscore < 17)) || ((mycards.length == 2) && (myscore < 14)) ||((mycards.length == 4) && (myscore < 10))) {
	   return true;
	}
	return false;
  }



// run
// Function that allows dealer to pull his set of cards after player stays
// Preconditions:
//	Deal button pressed
// Postconditions:
//	Game completed
//	Results displayed 
function run() {
  //If the game isn't over
  if(dealpressed == 1) {
    var opscore = document.getElementsByName("opscore")[0].value;
    var myscore = document.getElementsByName("myscore")[0].value;
    //Dealer will continue to hit till his score is <= 17
    while(opscore <= 17) {
      gethit('dealer');
      opscore = document.getElementsByName("opscore")[0].value;
    }
    //Determine whether the game is a win/loss/tie for 'me'
    if ((opscore <= 21) && (opscore > myscore)) {
      document.JForm.myresult.value = "LOSS";
      dealpressed = 0;
    }
    else if ((opscore <= 21) && (opscore < myscore)) {
      document.JForm.myresult.value = "WIN";
      dealpressed = 0;
    }
    else if ((opscore <= 21) && (myscore == opscore)) {
      document.JForm.myresult.value = "PUSH/TIE";
      dealpressed = 0;
    }
  }
  else {
    //Notify user to deal the game before staying.
    alert("Please Deal/Hit before stay!!");
  }
}


// Funciton deal
// start by dealing 2 cards to opponent and you
function deal() {
	// deal cards and display data
	dealpressed = 1; // deal button has been pressed
        var deckctr = 0;
        document.JForm.myresult.value = "";        
	
	// Check if we still have 20% of the deck. IF not then dealpressed = 0
	if(cc > 41){
	  deckctr++;
	  dealpressed = 0;
	}
	
        // draw 4 cards .
	var dealcards = []; //Cards used for the deal
        for(var i = 0; i<4; i++) {
	  dealcards.push(card[cc++]);
	}
        // If you have enough cards, draw two cards for each player
        if(deckctr == 0) {
	  var dlcard1 = "<img src = '"+dealcards[0]+".png' />";
	  var dlcard2 = "<img src = '"+dealcards[1]+".png' />";
	  dlcards = new Array (dlcard1, dlcard2);
	  var mycard1 = "<img src = '"+dealcards[2]+".png' />";
	  var mycard2 = "<img src = '"+dealcards[3]+".png' />";
	  mycards = new Array(mycard1, mycard2);
          getscore('me');
          getscore('dealer');
    	  // Display cards on screen
    	  document.getElementById("dlcards").innerHTML = dlcards[0] + dlcards[1]; 
	  document.getElementById("mycards").innerHTML = mycards[0]+ mycards[1];
	  //check for blackjack.
	  var opscore = document.getElementsByName("opscore")[0].value;
    	  var myscore = document.getElementsByName("myscore")[0].value;
          if(myscore == 21 && opscore != 21) {
            document.JForm.myresult.value = "WIN";
	    dealpressed = 0;
	  }
          else if(myscore == 21 && opscore == 21) {
            document.JForm.myresult.value = "PUSH/TIE";
	    dealpressed = 0;
	  }
	  else if(myscore != 21 && opscore == 21) {
	    document.JForm.myresult.value = "LOSS";
	    dealpressed = 0;
	  }
        }
	else {
          //Alert the user to reshuffle deck.
	  alert("you are out of cards! Please reshuffle and try again!");
	}
}
