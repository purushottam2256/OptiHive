import 'package:flutter_blue/flutter_blue.dart';

class BluetoothService {
  FlutterBlue flutterBlue = FlutterBlue.instance;
  List<BluetoothDevice> devicesList = [];

  void startScan() {
    flutterBlue.startScan(timeout: const Duration(seconds: 4));
    flutterBlue.scanResults.listen((results) {
      // Display devices found
      devicesList.clear();
      for (ScanResult result in results) {
        devicesList.add(result.device);
      }
    });
  }

  void stopScan() {
    flutterBlue.stopScan();
  }

  // Function to connect to laptop
  Future<void> connectToDevice(BluetoothDevice device) async {
    await device.connect();
  }
}
