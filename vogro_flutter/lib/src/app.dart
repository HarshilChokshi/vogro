import 'package:flutter/material.dart';
import 'package:vogro_flutter/src/screens/sign_up_page.dart';
import 'screens/home_page.dart';

class App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      initialRoute: '/',
      routes: {
        '/': (context) => HomePage(),
      },
    );
  }
}
