import 'package:flutter/material.dart';
import 'screens/battery_diagnostics.dart';
import 'wifi_service.dart'; // Import Wifi service
import 'firebase_service.dart'; // Import Firebase service
import 'bluetooth_service.dart'; // Import Bluetooth service

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  MyApp({super.key});

  final WifiService wifiService = WifiService();
  final FirebaseService firebaseService = FirebaseService();
  final BluetoothService bluetoothService = BluetoothService();

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'OptiHive-OS',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: BluetoothConnectionScreen(),
    );
  }
}

class BluetoothConnectionScreen extends StatelessWidget {
  BluetoothConnectionScreen({super.key});

  final BluetoothService bluetoothService = BluetoothService();
  final WifiService wifiService = WifiService();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Connect to Laptop')),
      body: Center(
        child: ElevatedButton(
          onPressed: () async {
            final navigatorContext = context;
            bluetoothService.startScan();
            var laptopDetails = await wifiService.fetchLaptopDetails();
            if (context.mounted) {
              Navigator.push(
                navigatorContext,
                MaterialPageRoute(
                  builder: (context) => BatteryDiagnosticsScreen(
                    laptopName: laptopDetails['name'],
                    batteryPercentage: laptopDetails['battery_percentage'],
                  ),
                ),
              );
            }
          },
          child: const Text('Connect to Laptop'),
        ),
      ),
    );
  }
}
