import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'package:vogro_flutter/src/screens/log_in_page.dart';
import 'sign_up_page.dart';

class HomePage extends StatelessWidget {
  Widget build(BuildContext context) {
    return Container(
      child: Scaffold(
        backgroundColor: Colors.white,
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.end,
            children: <Widget>[
              logo(),
              SizedBox(
                height: 120,
              ),
              Help(),
              SizedBox(
                height: 50,
              ),
              SignUpButton(context),
              ContinueWithFacebookButton(context),
              ContinueWithGoogleButton(),
              LoginButton(context),
            ],
          ),
        ),
      ),
    );
  }
}

Widget SignUpButton(BuildContext context) {
  return Center(
    child: Column(
      children: <Widget>[
        SizedBox(
          width: 300,
          child: RaisedButton(
            shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(24),
                side: BorderSide(color: Colors.black)),
            color: Color(0xff39d47f),
            onPressed: () {
              Navigator.push(
                  context, CupertinoPageRoute(builder: (context) => SignUp()));
            },
            textColor: Colors.black,
            child: Container(
              padding: const EdgeInsets.all(10.0),
              child: const Text(
                'SIGN UP',
                style: TextStyle(
                  fontSize: 13,
                  letterSpacing: 2.0,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
          ),
        ),
      ],
    ),
  );
}

Widget ContinueWithFacebookButton(BuildContext context) {
  return Center(
    child: Column(
      children: <Widget>[
        SizedBox(
          width: 300,
          child: RaisedButton(
            shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(24),
                side: BorderSide(color: Colors.black)),
            color: Color(0xff4267b2),
            onPressed: () {},
            textColor: Colors.white,
            child: Container(
              padding: const EdgeInsets.all(10.0),
              child: const Text('CONTINUE WITH FACEBOOK',
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

Widget ContinueWithGoogleButton() {
  return Center(
    child: Column(
      children: <Widget>[
        SizedBox(
          width: 300,
          child: RaisedButton(
            shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(24),
                side: BorderSide(color: Colors.black)),
            color: Color(0xff4385F4),
            onPressed: () {},
            textColor: Colors.white,
            child: Container(
              padding: const EdgeInsets.all(10.0),
              child: const Text('CONTINUE WITH GOOGLE',
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

Widget LoginButton(BuildContext context) {
  return Center(
    child: Column(
      children: <Widget>[
        SizedBox(
          width: 300,
          child: FlatButton(
            onPressed: () {
              Navigator.push(
                  context, CupertinoPageRoute(builder: (context) => LogIn()));
            },
            textColor: Colors.black,
            child: Container(
              child: const Text('LOG IN',
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

Widget logo() {
  return Image(
    image: AssetImage('assets/images/logo.png'),
    height: 200,
  );
}

Widget Help() {
  return Text('WE NEED YOUR HELP.',
      style: TextStyle(
        fontSize: 25,
        letterSpacing: 2.0,
        wordSpacing: 10.0,
        fontWeight: FontWeight.bold,
      ));
}
