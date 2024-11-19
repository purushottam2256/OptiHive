import 'package:firebase_messaging/firebase_messaging.dart';

class FirebaseService {
  final FirebaseMessaging _firebaseMessaging = FirebaseMessaging.instance;

  void setupFirebase() {
    FirebaseMessaging.onMessage.listen((RemoteMessage message) {
      // Handle notifications here
    });
  }

  Future<String> getToken() async {
    String? token = await _firebaseMessaging.getToken();
    return token ?? '';
  }
}
