import 'location_model.dart';

class ClientGroceryPost{


  int id;
  int client_user_id;
  Location grocery_store_address;
  String grocery_store_address_name;
  String grocery_store_name;
  DateTime time_of_grocery_shopping;
  List<String> grocery_item_list;
  DateTime earliest_time;
  DateTime latest_time;
  DateTime time_of_post;

  ClientGroceryPost (
    this.id,
    this.client_user_id,
    this.grocery_store_address,
    this.grocery_store_address_name,
    this.grocery_store_name,
    this.time_of_grocery_shopping,
    this.earliest_time,
    this.latest_time,
    this.time_of_post
  );
  
}

// class client_user_id{
//     this.id = id ;
//   }