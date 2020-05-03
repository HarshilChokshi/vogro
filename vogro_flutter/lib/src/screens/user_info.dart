import 'package:flutter/material.dart';
import 'validate.dart';


class UserInfo extends StatelessWidget {


  Widget build(BuildContext context) {
  
    return Container(
      alignment: Alignment.topRight,
      child: Scaffold(
         resizeToAvoidBottomPadding: false ,
        backgroundColor: Colors.white,
        body: Container(
          child: Column(
            children: <Widget>[
              SizedBox(height: 20),
              Row(children: <Widget>[
                Back(context),
                SizedBox(width: 50),
                Text("LOG IN",
                    style: TextStyle(
                      fontSize: 15,
                      fontWeight: FontWeight.bold,
                    )),
                SizedBox(width: 5),
                Vine(),
              ]),
              Align(
                alignment: Alignment(-0.75, 0),
                child: Text("First Name",
                    style: TextStyle(
                      fontSize: 22,
                      fontWeight: FontWeight.bold,
                    )),
              ),
              SizedBox(height: 10),
              Email(),
              SizedBox(height: 15),
              Align(
                alignment: Alignment(-0.75, 0),
                child: Text("Last Name",
                    style: TextStyle(
                      fontSize: 22,
                      fontWeight: FontWeight.bold,
                    )),
              ),
              SizedBox(height: 10),
              Password(),
              SizedBox(height: 15),
              Align(
                alignment: Alignment(-0.75, 0),
                child: Text("Address",
                    style: TextStyle(
                      fontSize: 22,
                      fontWeight: FontWeight.bold,
                    )),
              ),
              SizedBox(height: 10),
              Password(),
              SizedBox(height: 10),
              Align(
                alignment: Alignment(-0.75, 0),
                child: Text("Choose Pic",
                    style: TextStyle(
                      fontSize: 22,
                      fontWeight: FontWeight.bold,
                    )),
              ),
              SizedBox(height: 10),
              SignIn(context),
              
            ],
          ),
        ),
      ),
    );
  }
}

Widget Back(BuildContext context) {
  return Container(
    child: Column(
      children: <Widget>[
        SizedBox(
          child: BackButton(
            color: Colors.black,
            onPressed: () {
              Navigator.pop(context);
            },
          ),
        ),
      ],
    ),
  );
}

Widget Vine() {
  return Image(
    image: AssetImage('assets/images/vine.png'),
    height: 25,
  );
}

Widget Email() {
  return Padding(
      padding: const EdgeInsets.fromLTRB(22.0, 0, 22, 0),
      child: TextFormField(
          keyboardType: TextInputType.emailAddress,
          autofocus: false,
          decoration: InputDecoration(
            hintText: 'Alex',
            contentPadding: EdgeInsets.fromLTRB(20.0, 10.0, 20.0, 10.0),
            border: OutlineInputBorder(),
          )));
}



Widget Password() {
  return Padding(
      padding: const EdgeInsets.fromLTRB(22.0, 0, 22, 0),
      child: TextFormField(
          keyboardType: TextInputType.visiblePassword,
          obscureText: true,
          autofocus: false,
          decoration: InputDecoration(
            hintText: 'Jones',
            contentPadding: EdgeInsets.fromLTRB(20.0, 10.0, 20.0, 10.0),
            border: OutlineInputBorder(),
          )));
}

Widget Address() {
  return Padding(
      padding: const EdgeInsets.fromLTRB(22.0, 0, 22, 0),
      child: TextFormField(
          keyboardType: TextInputType.text,
          autofocus: false,
          decoration: InputDecoration(
            hintText: '420 Cool St',
            contentPadding: EdgeInsets.fromLTRB(20.0, 10.0, 20.0, 10.0),
            border: OutlineInputBorder(),
          )));
}

Widget SignIn(BuildContext context) {
  return Center(
    child: Column(
      children: <Widget>[
        SizedBox(
          width: 200,
          child: RaisedButton(
            shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(24),
                side: BorderSide(color: Colors.black)),
            color: Color(0xff39d47f),
            onPressed: () {},
            textColor: Colors.black,
            child: Container(
              padding: const EdgeInsets.all(10.0),
              child: const Text('SIGN IN',
                  style: TextStyle(
                    fontSize: 13,
                    letterSpacing: 2.0,
                    fontWeight: FontWeight.bold,
                  )),
            ),
          ),
        ),
      ],
    ),
  );
}
