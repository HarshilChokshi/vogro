import 'location_model.dart';

class VolunteerGroceryPosts{
  int id;
  int volunteer_user_id;
  Location grocery_store_address;
  String grocery_store_address_name;
  String grocery_store_name;
  DateTime time_of_grocery_shopping;
  DateTime earliest_time;
  DateTime latest_time;
  DateTime time_of_post;

  VolunteerGroceryPosts( 
    this.id,
    this.volunteer_user_id,
    this.grocery_store_address,
    this.grocery_store_address_name,
    this.grocery_store_name,
    this.time_of_grocery_shopping,
    this.earliest_time,
    this.latest_time,
    this.time_of_post
  );
}

