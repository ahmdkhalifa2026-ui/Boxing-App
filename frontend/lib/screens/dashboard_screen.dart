import 'package:flutter/material.dart';

class DashboardScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Dashboard'),
      ),
      body: SingleChildScrollView(
        child: Column(
          children: <Widget>[  
            PlayerOverview(),
            TeamStatistics(),
            TopPlayers(),
            PerformanceMetrics(),
          ],
        ),
      ),
    );
  }
}

class PlayerOverview extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            Text('Player Overview', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
            // Add player overview widgets here
          ],
        ),
      ),
    );
  }
}

class TeamStatistics extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            Text('Team Statistics', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
            // Add team statistics widgets here
          ],
        ),
      ),
    );
  }
}

class TopPlayers extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            Text('Top Players', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
            // Add top players widgets here
          ],
        ),
      ),
    );
  }
}

class PerformanceMetrics extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            Text('Performance Metrics', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
            // Add performance metrics visualization here
          ],
        ),
      ),
    );
  }
}
