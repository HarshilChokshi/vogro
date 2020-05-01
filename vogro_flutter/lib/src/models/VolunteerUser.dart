import 'location_model.dart';
class VolunteerUser {
  int id;
  String first_name;
  String last_name;
  String email;
  int phone_numbers;
  int total_deliveries;
  bool is_allowed_to_use_app;
  int strikes;
  String profile_image_ref;
  Location address;
  List<Location> preferred_grocery_stores;
  bool get_store_notification;


  VolunteerUser( 
    this.id,
    this.first_name,
    this.last_name,
    this.email,
    this.phone_numbers,
    this.total_deliveries,
    this.is_allowed_to_use_app,
    this.strikes,
    this.profile_image_ref,
    this.address,
    this.preferred_grocery_stores,
    this.get_store_notification
  );
  
}
