import 'package:flutter/material.dart';

class PlayerProfileScreen extends StatelessWidget {
  final String playerName;
  final String playerImage;
  final List<String> performanceMetrics;
  final List<String> matchHistory;
  final List<String> trainingSessions;

  PlayerProfileScreen({
    required this.playerName,
    required this.playerImage,
    required this.performanceMetrics,
    required this.matchHistory,
    required this.trainingSessions,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(playerName),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: SingleChildScrollView(
          child: Column(
            children: [
              // Player Image
              Container(
                height: 150,
                width: 150,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  image: DecorationImage(
                    image: NetworkImage(playerImage),
                    fit: BoxFit.cover,
                  ),
                ),
              ),
              SizedBox(height: 20),
              // Player Details
              Text(
                'Player Name: $playerName',
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              ),
              SizedBox(height: 10),
              // Performance Metrics
              Text(
                'Performance Metrics:',
                style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
              ),
              ...performanceMetrics.map((metric) => Text(metric)).toList(),
              SizedBox(height: 10),
              // Match History
              Text(
                'Match History:',
                style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
              ),
              ...matchHistory.map((match) => Text(match)).toList(),
              SizedBox(height: 10),
              // Training Sessions
              Text(
                'Training Sessions:',
                style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
              ),
              ...trainingSessions.map((session) => Text(session)).toList(),
            ],
          ),
        ),
      ),
    );
  }
}