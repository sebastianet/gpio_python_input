#!/usr/bin/env node

// minimal web server for RRG page showing GPIO input
// start by "sudo node wsm.js" as we use port 80

// versions :
//  20190504 : 1.1 - code start

var myVersion = "1.1.a" ;

var path=require( 'path' ) ;                 //
var express = require( 'express' ) ;         // npm install express --save : add to package.json 
var app = express() ;                        // instantiate Express and assign our app variable to it.
app.set( 'mPort', process.env.PORT || 80 ) ; // need 80 for wget
var szHostName = require('os').hostname() ;  // https://nodejs.org/api/os.html

var szIP = process.argv [ 2 ] ;      // local IP passed from shell 

app.use( express.static( path.join( __dirname, '/public' ) ) ) ; // serve static files

// Date() prototypes - use as
//     var szOut = (new Date).yyyymmdd() + '-' + (new Date).hhmmss() + ' ' + szIn + '<br>' ;

Date.prototype.yyyymmdd = function ( ) {

     var yyyy = this.getFullYear().toString();
     var mm   = (this.getMonth()+1).toString(); // getMonth() is zero-based
     var dd   = this.getDate().toString();
     return yyyy + '/' + (mm[1]?mm:'0'+mm[0]) + '/' + (dd[1]?dd:'0'+dd[0]);

}; // yyyymmdd()

Date.prototype.hhmmss = function () {

     function fixTime(i) {
          return (i < 10) ? "0" + i : i;
     }
     var today = new Date(),
          hh = fixTime( today.getHours() ),
          mm = fixTime( today.getMinutes() ),
          ss = fixTime( today.getSeconds() ) ;
     var myHHMMSS = hh + ':' + mm + ':' + ss ;
     return myHHMMSS ;

} ; // hhmmss()

let szId = `*** MinWebSrv listening on port [` + szIP + ':' + app.get('mPort') + `], host {` + szHostName + `} *** `

app.listen( app.get( 'mPort' ), () => {
    console.log( szId )
} ) ;

// console.log( szId ) ;

