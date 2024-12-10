extends Node

var initial_data: Dictionary
var data: Dictionary = {}

func init(init_data: Dictionary):
	initial_data = init_data
	return self

func update(new_model: Dictionary):
	data = new_model
	if new_model.has("enemy_health") or new_model.has("npc_role"):
		data = new_model
