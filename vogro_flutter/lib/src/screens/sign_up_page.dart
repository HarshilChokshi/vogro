import 'package:flutter/material.dart';

class SignUp extends StatelessWidget {
  Widget build(BuildContext context) {
    return Container(
      alignment: Alignment.topRight,
      child: Scaffold(
        backgroundColor: Colors.white,
        body: Container(
          child: Column(
            children: <Widget>[
              SizedBox(height: 20),
              Row(children: <Widget>[
                Back(context),
                SizedBox(width: 100),
                Text("SIGN UP",
                    style: TextStyle(
                      fontSize: 15,
                      fontWeight: FontWeight.bold,
                    )),
                SizedBox(width: 5),
                Vine(),
              ]),
              SizedBox(height: 15),
              Align(
                // alignment: Alignment(-0.75, 0),
                child: Text("Join Vogro Today",
                    style: TextStyle(
                      fontSize: 22,
                      fontWeight: FontWeight.bold,
                    )),
              ),
              SizedBox(height: 30),
              Email(),
              SizedBox(height: 10),
              Password(),
              SizedBox(height: 10),
              ConfirmPassword(),
              SizedBox(height: 10),
              Next(context),
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
            hintText: 'Email',
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
            hintText: 'New Password',
            contentPadding: EdgeInsets.fromLTRB(20.0, 10.0, 20.0, 10.0),
            border: OutlineInputBorder(),
          )));
}

Widget ConfirmPassword() {
  return Padding(
      padding: const EdgeInsets.fromLTRB(22.0, 0, 22, 0),
      child: TextFormField(
          keyboardType: TextInputType.visiblePassword,
          obscureText: true,
          autofocus: false,
          decoration: InputDecoration(
            hintText: 'Confirm Password',
            contentPadding: EdgeInsets.fromLTRB(20.0, 10.0, 20.0, 10.0),
            border: OutlineInputBorder(),
          )));
}

Widget Next(BuildContext context) {
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
              child: const Text('Next',
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
