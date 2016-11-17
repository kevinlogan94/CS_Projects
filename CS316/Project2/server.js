/*
Kevin Logan
Program 2
CS316: Web Programming
*/
const http = require('http');
const url = require('url');
const fs = require('fs');
const paul = require('/homes/paul/HTML/CS316/p2_req.js');
const exec = require('child_process').exec;

const hostname = 'pen.cs.uky.edu';
const port = 4200;
const randport = Math.floor(Math.random() * (paul.pend() - paul.pstart() + paul.pstart()));

//check the type of file and return the same path with the directory added to it.
function checkurl(url) {
	var type = url.substring(url.indexOf(".") + 1);
	if (type == 'html'){
		url = 'PUBLIC' + url;
	}
	else if(type == 'cgi'){
		url = 'CGIDIR' + url;
	}
	return [url, type];
}

//Child exec function for executing the cgi files on the command line
function execute(xurl, callback){
        var child = exec(xurl, {env: {'PATH': './CGIDIR/'}}, function(error, stdout, stderr) {
                //If error is reported send the error(stderr, error). Otherwise post executed result.
		if (error) {
			console.log("EXECUTION FAILURE!!!");
                        console.error('Exec Error: '+ error);
			callback("EXECUTION FAILURE: " + error, 404);
                        return;
                };
		if(stderr != "") {
                	console.log('stderr: ' + stderr);
			callback(stderr, 404); 
		}
		else {
			console.log("Execute Successful for: " + xurl);
			callback(stdout, 200);
		}
        });
}

//Main function for this project. Function the server is built on that keeps track of 
//what to report to the screen. 
function myprocess(req, res) {
        var result = checkurl(req.url);
	var xurl = result[0];
	var filetype = result[1];
	//Check if file requested exists. If so load it.
	if(fs.existsSync(xurl) && xurl != '/'){
		if (filetype == 'html'){
		   var data = fs.readFileSync(xurl);
		   res.statusCode = 200;
                   res.setHeader("content-type", "text/plain");
		   console.log("Read File Successful for: " + xurl);
                   res.end(data);
		}
		else if (filetype == 'cgi') {
		   execute(xurl, function(output, statuscode) {
	         	res.statusCode = statuscode;
                   	res.setHeader("content-type", "text/plain");
                	res.end(output);	
		   }); 
		}
		else {
		   res.statusCode = 404;
                   res.setHeader("content-type", "text/plain");
		   console.log("This is neither a HTML or CGI: " + xurl);
                   res.end("This is neither a HTML or CGI: " + xurl);
		}
	}
	else {
		//If file doesn't exist
		res.statusCode = 404;
                res.setHeader("content-type", "text/plain");
		console.log("That file doesn't exist: " + xurl);
                res.end("That file doesn't exist: " + xurl);
	}
};

var server = http.createServer(myprocess);

//Listener function that keeps track what port and hostname everything is being hosted on.
function mylisten(server, port, hostname, logger){
	logger(port, hostname);
	server.listen(port,hostname, function(){
        //Callback triggered when server is successfully listening. Hurray!
        console.log('Go to: http://pen.cs.uky.edu:' +  port + '/');
    });
};

mylisten(server, randport, paul.phost(), paul.logger);
