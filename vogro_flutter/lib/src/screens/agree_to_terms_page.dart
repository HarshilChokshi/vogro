import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'package:vogro_flutter/src/screens/sign_up_page.dart';
import 'package:flutter/scheduler.dart' show timeDilation;

class AgreeToTerms extends StatelessWidget {
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
                // Text("Disclaimer",
                //     style: TextStyle(
                //       fontSize: 15,
                //       fontWeight: FontWeight.bold,
                //     )),
                SizedBox(width: 5),
              ]),
              SizedBox(height: 15),
              Align(
                // alignment: Alignment(-0.75, 0),
                child: Text("How Would You Like to Sign Up?",
                    style: TextStyle(
                      fontSize: 22,
                      fontWeight: FontWeight.bold,
                    )),
              ),
              SizedBox(height: 30),
              SignUpUsingEmail(context),
              SignUpWithFacebookButton(context),
              SignUpWithGoogleButton(),
              Padding(
                padding: const EdgeInsets.fromLTRB(22.0, 0, 22, 0),
                child: Check(context),
              ),
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

Widget SignUpUsingEmail(BuildContext context) {
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
                'SIGN UP USING EMAIL',
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

Widget SignUpWithFacebookButton(BuildContext context) {
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

Widget SignUpWithGoogleButton() {
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

Widget Check(BuildContext context) {
  return CheckboxListTile(
    title: const Text('Agree To Terms'),
    value: timeDilation != 1.0,
    onChanged: (bool value) {
      // setState(() {
      //   timeDilation = value ? 10.0 : 1.0;
      // });
    },
  );
}
