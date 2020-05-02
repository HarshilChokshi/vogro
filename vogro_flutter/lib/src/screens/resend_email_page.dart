import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';

class ResendEmail extends StatelessWidget {
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
              Padding(
                padding: const EdgeInsets.fromLTRB(22.0, 0, 22, 0),
                child: Text("Click to Resend email",
                    style: TextStyle(
                      fontSize: 22,
                      fontWeight: FontWeight.bold,
                    )),
              ),
              SizedBox(height: 30),
              SizedBox(height: 10),
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
            onPressed: () {},
            textColor: Colors.black,
            child: Container(
              padding: const EdgeInsets.all(10.0),
              child: const Text('Resend email',
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
