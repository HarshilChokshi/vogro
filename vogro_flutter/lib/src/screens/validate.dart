import 'package:flutter/material.dart';
import 'package:email_validator/email_validator.dart';

class LoginPage extends StatefulWidget {
  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final formKey = GlobalKey<FormState>();
  final scaffoldKey = GlobalKey<ScaffoldState>();

  String _email;
  String _password;

  void _submitCommand() {
    final form = formKey.currentState;

    if (form.validate()) {
      form.save();

      // Email & password matched our validation rules
      // and are saved to _email and _password fields.
      
      // _loginCommand();
    }
  }

  // void _loginCommand() {
  //   // This is just a demo, so no actual login here.
  //   final snackbar = SnackBar(
  //     content: Text('Email: $_email, password: $_password'),
  //   );
  
  //   scaffoldKey.currentState.showSnackBar(snackbar);
  // }



  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: scaffoldKey,
      appBar: AppBar(
        title: Text('VoGro'),
      ),
      body: Padding(
        padding: const EdgeInsets.fromLTRB(22.0, 0, 22, 0),
        child: Form(
          key: formKey,
          child: Column(
            children: [
              SizedBox(height: 20),
               SizedBox(width: 100),
               Text("Log In",
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                    )),
                    SizedBox(height: 20,),
              TextFormField(
                decoration: InputDecoration(labelText: 'Email',
                border: OutlineInputBorder(),
                hintText: 'JonDoe@gmail.com',
                contentPadding: EdgeInsets.fromLTRB(20.0, 10.0, 20.0, 10.0)),
                validator: (val) => !EmailValidator.validate(val, true)
                    ? 'Not a valid email.'
                    : null,
                onSaved: (val) => _email = val,
              ),
              SizedBox(height:20),
              TextFormField(
                decoration: InputDecoration(labelText: 'Password',
                border: OutlineInputBorder(),
                hintText: 'Jondoe123',
                contentPadding: EdgeInsets.fromLTRB(20.0, 10.0, 20.0, 10.0)),
                // validator: (val) =>
                //     val.length < 4 ? 'Password too short..' : null,
                // onSaved: (val) => _password = val,
                obscureText: true,
              ),
              SizedBox(height:20),
              RaisedButton(
                onPressed: _submitCommand,
                child: Text('Sign in'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

