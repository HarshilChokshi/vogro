import 'location_model.dart';

class ClientGroceryPostRequest {

  int id;
  int volunteer_user_id;
  int client_user_id;
  int volunteer_grocery_post_id;
  int grocery_store_address;
  String grocery_store_address_name;
  String grocery_store_name;
  DateTime time_of_grocery_shopping;
  List<String> grocery_item_list;
  DateTime earliest_time;
  DateTime latest_time;
  DateTime time_of_post;
  String notes;
  Location client_address;

  ClientGroceryPostRequest( 
    this.id,
    this.volunteer_user_id,
    this.client_user_id,
    this.volunteer_grocery_post_id,
    this.grocery_store_address,
    this.grocery_store_address_name,
    this.grocery_store_name,
    this.time_of_grocery_shopping,
    this.grocery_item_list,
    this.earliest_time,
    this.latest_time,
    this.time_of_post,
    this.notes,
    this.client_address
  );

}

