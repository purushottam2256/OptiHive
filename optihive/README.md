# OptiHive-OS

OptiHive-OS is a sophisticated battery monitoring solution that provides real-time diagnostics and alerts for laptop batteries. The app connects seamlessly via Bluetooth or Wi-Fi to deliver comprehensive battery health information and customizable notifications.

## Features

- **Real-time Battery Monitoring**
  - Battery health status
  - Charge/discharge rates
  - Temperature monitoring
  - Cycle count tracking

- **Connectivity Options**
  - Bluetooth Low Energy (BLE) support
  - Wi-Fi connectivity
  - Automatic reconnection

- **Smart Notifications**
  - Firebase Cloud Messaging integration
  - Customizable alert thresholds
  - Battery health warnings
  - Charging recommendations

- **User Interface**
  - Intuitive battery diagnostics dashboard
  - Real-time graphs and statistics
  - Dark/Light theme support

## Getting Started

### Prerequisites

- Flutter SDK (latest stable version)
- Android Studio or VS Code
- iOS development tools (for iOS deployment)
- Firebase account

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/optihive-os.git
   cd optihive-os
   ```

2. Install dependencies:
   ```bash
   flutter pub get
   ```

3. Firebase Setup:
   - Create a new Firebase project
   - Download `google-services.json` for Android
   - Download `GoogleService-Info.plist` for iOS
   - Place these files in their respective directories:
     - Android: `android/app/google-services.json`
     - iOS: `ios/Runner/GoogleService-Info.plist`

4. Run the app:
   ```bash
   flutter run
   ```

## Configuration

### Firebase Configuration
1. Enable Firebase Cloud Messaging in your Firebase Console
2. Update Firebase configuration in `lib/config/firebase_config.dart`

### Bluetooth Settings
- Ensure Bluetooth permissions are enabled on your device
- Configure Bluetooth settings in `lib/config/bluetooth_config.dart`

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Your Name - [@purushottam2256](https://github.com/purushottam2256)
Project Link: [https://github.com/purushottam2256/optihive](https://github.com/purushottam2256/optihive)

## Acknowledgments

- optihive Team (sharan)
- Firebase
- All contributors who helped with the project
