import 'package:flutter/material.dart';

void main() {
  runApp(BoxingApp());
}

class BoxingApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Boxing Performance Evaluation Platform',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: HomeScreen(),
      routes: {
        '/home': (context) => HomeScreen(),
        // Add other routes here as needed
      },
    );
  }
}

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Home')), 
      body: Center(child: Text('Welcome to the Boxing Performance Evaluation Platform!')), 
    );
  }
}