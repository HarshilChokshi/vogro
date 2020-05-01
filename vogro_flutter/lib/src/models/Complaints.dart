
class Complaints {
  int id;
  int volunteer_user_id;
  int client_user_id;
  int completed_grocery_post_id;
  bool is_complainer_volunteer;
  String complain_details;

  Complaints(
    this.id,
    this.volunteer_user_id,
    this.client_user_id,
    this.completed_grocery_post_id,
    this.is_complainer_volunteer,
    this.complain_details
  );

}