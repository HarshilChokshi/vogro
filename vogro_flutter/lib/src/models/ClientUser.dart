import 'location_model.dart';
class ClientUser{

  int id;
  String first_name;
  String last_name;
  String email;
  String phone_number;
  int total_orders;
  bool is_allowed_to_use_app; //(default = true)
  int strikes; //(default = 0)
  String profile_image_ref; //(default = null)
  Location address;
  String address_name;

  ClientUser(
    this.id,
    this.first_name,
    this.last_name,
    this.email,
    this.phone_number,
    this.total_orders,
    this.is_allowed_to_use_app,
    this.strikes,
    this.profile_image_ref,
    this.address,
    this.address_name
  );
}