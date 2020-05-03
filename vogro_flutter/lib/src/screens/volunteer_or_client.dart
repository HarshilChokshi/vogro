
import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'package:vogro_flutter/src/screens/user_info.dart';
import 'log_in_page.dart';
import 'validate.dart';

class VolunteerOrClient extends StatelessWidget {
  @override
  @override
  Widget build(BuildContext context) {
    return new MaterialApp(
      theme: new ThemeData(
        primarySwatch: Colors.lightBlue,

      ),
      home: new HomePage(),
    );
  }
}

class HomePage extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      
      resizeToAvoidBottomPadding: false ,
      appBar: new AppBar(),
      
      body: new Container(
       
        padding: EdgeInsets.all(21.0),
        child: new Column(
          
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.stretch, 
          children: <Widget>[
           
            RaisedButton ( onPressed: ( ) {Navigator.push(
                  context, CupertinoPageRoute(builder: (context) => LoginPage()));} , child:
                   Text('Login As Volunteer'),
                    ),
            FlatButton(onPressed: () {Navigator.push(
              //for now I just added the 'Login as client' to the onPushed because we dont have the functional buttons
              //change later
                  context, CupertinoPageRoute(builder: (context) => UserInfo()));}, child: Text('Login As Client'),
                   color: Colors.green,),
          ],
        ),
      ),
    );
  }
}