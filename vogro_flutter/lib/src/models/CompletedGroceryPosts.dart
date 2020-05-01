class CompletedGroceryPosts{

  int id;
  int client_user_id;
  int volunteer_user_id;
  String grocery_store_address;
  String grocery_store_address_name;
  String grocery_store_name;
  DateTime time_of_grocery_shopping;
  List<int> grocery_item_list;
  DateTime earliest_time;
  DateTime latest_time;
  DateTime time_of_post;
  String receipt_image_ref;
  double grocery_total_amount;

  CompletedGroceryPosts(  
    this.id,
    this.client_user_id,
    this.volunteer_user_id,
    this.grocery_store_address,
    this.grocery_store_address_name,
    this.grocery_store_name,
    this.grocery_item_list,
    this.earliest_time,
    this.latest_time,
    this.time_of_post,
    this.receipt_image_ref,
    this.grocery_total_amount
  );
}