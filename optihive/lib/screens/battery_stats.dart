import 'package:flutter/material.dart';
import 'package:fl_chart/fl_chart.dart';

class BatteryStats extends StatelessWidget {
  final List<FlSpot> dataPoints;

  const BatteryStats({super.key, required this.dataPoints});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: LineChart(
          LineChartData(
            lineBarsData: [
              LineChartBarData(
                spots: dataPoints,
                isCurved: true,
                color: Colors.blue,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
