import 'package:flutter/material.dart';

class LiveGroceryPost{

  int id;
  int client_user_id;
  int volunteer_user_id;
  String grocery_store_address;
  String grocery_store_address_name;
  String grocery_store_name;
  TimeOfDay time_of_grocery_shopping;
  DateTime earliest_time;
  DateTime latest_time;
  TimeOfDay time_of_post;
  String receipt_image_ref;
  double grocery_total_amount;
  String state_of_volunteer;
  List<int> grocery_item_list;

  LiveGroceryPost(
    this.id,
    this.client_user_id,
    this.volunteer_user_id,
    this.grocery_store_address,
    this.grocery_store_address_name,
    this.grocery_store_name,
    this.time_of_grocery_shopping,
    this.grocery_item_list,
    this.earliest_time,
    this.latest_time,
    this.time_of_post,
    this.receipt_image_ref,
    this.grocery_total_amount,
    this.state_of_volunteer
  );

}