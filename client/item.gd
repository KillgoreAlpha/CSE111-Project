extends Node2D

# Item properties
var id: int
var item_name: String
var description: String
var quantity: int
var icon_path: String

# Initialize item data
func init(item_data: Dictionary):
	id = item_data.get("id", 0)
	item_name = item_data.get("item_name", "Unknown Item")
	description = item_data.get("description", "No description available.")
	quantity = item_data.get("quantity", 1)
	icon_path = item_data.get("icon_path", "res://default_icon.png")
	update_visuals()
	return self

# Update item's visual representation
func update_visuals():
	var icon_texture = load(icon_path) if icon_path else null
	if has_node("Icon") and icon_texture:
		$Icon.texture = icon_texture
	if has_node("Label"):
		$Label.text = item_name + " x" + str(quantity)
