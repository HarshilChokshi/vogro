import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'agree_to_terms_page.dart';

class Disclaimer extends StatelessWidget {
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
              ]),
              SizedBox(height: 15),
              Align(
                child: Text("Disclaimer",
                    style: TextStyle(
                      fontSize: 22,
                      fontWeight: FontWeight.bold,
                    )),
              ),
              SizedBox(height: 30),
              SizedBox(height: 10),
              SizedBox(width: 100),
              Padding(
                padding: const EdgeInsets.fromLTRB(22.0, 0, 22, 0),
                child: Text(
                    '''Volunteer - This is what a volunteer is, This is what a volunteer does. 

Client - This is what a client is, This is what a client does.''',
                    style: TextStyle(
                      fontSize: 15,
                      fontWeight: FontWeight.bold,
                    )),
              ),
              SizedBox(width: 5),
              SizedBox(height: 10),
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
            onPressed: () {
              Navigator.push(context,
                  CupertinoPageRoute(builder: (context) => AgreeToTerms()));
            },
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
