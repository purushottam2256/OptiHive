import 'package:http/http.dart' as http;
import 'dart:convert';

class WifiService {
  static const String apiUrl = 'http://<your-flask-server-ip>:<port>/api/laptop_details';

  Future<Map<String, dynamic>> fetchLaptopDetails() async {
    var response = await http.get(Uri.parse(apiUrl));
    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    } else {
      throw Exception('Failed to load laptop details');
    }
  }
}
