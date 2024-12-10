from django.contrib.auth.models import User
from server.models import (
    GameUser, Entity, InstancedEntity, Character, 
    Guild, Quest, Item, FriendlyNPC, EnemyNPC, Actor
)
from django.utils import timezone

# Clean existing data
print("Cleaning existing data...")
User.objects.all().delete()
GameUser.objects.all().delete()
Entity.objects.all().delete()
InstancedEntity.objects.all().delete()
Character.objects.all().delete()
Guild.objects.all().delete()
Quest.objects.all().delete()
Item.objects.all().delete()
FriendlyNPC.objects.all().delete()
EnemyNPC.objects.all().delete()
Actor.objects.all().delete()

# Create Player 1
print("Creating Player 1...")
user1 = User.objects.create_user(
    username='player1',
    email='player1@example.com',
    password='testpass123',
    is_staff=False,
    is_active=True,
    date_joined=timezone.now()
)

game_user1 = GameUser.objects.create(
    user=user1,
    username='player1',
    email='player1@example.com',
    password='testpass123'
)

# Create Player 2
print("Creating Player 2...")
user2 = User.objects.create_user(
    username='player2',
    email='player2@example.com',
    password='testpass456',
    is_staff=False,
    is_active=True,
    date_joined=timezone.now()
)

game_user2 = GameUser.objects.create(
    user=user2,
    username='player2',
    email='player2@example.com',
    password='testpass456'
)

# Create Entities
print("Creating Entities...")
player1_entity = Entity.objects.create(name='player1')
player2_entity = Entity.objects.create(name='player2')
merchant_entity = Entity.objects.create(name='merchant_npc')
guard_entity = Entity.objects.create(name='guard_npc')
wolf_entity = Entity.objects.create(name='wolf_npc')
wolf_boss_entity = Entity.objects.create(name='wolf_boss_npc')
shadow_mage_entity = Entity.objects.create(name='shadow_mage_npc')

# Create InstancedEntities
print("Creating InstancedEntities...")
player1_instance = InstancedEntity.objects.create(
    x=0.0,
    y=0.0,
    entity=player1_entity
)

player2_instance = InstancedEntity.objects.create(
    x=0.0,
    y=0.0,
    entity=player2_entity
)

merchant_instance = InstancedEntity.objects.create(
    x=310.0,
    y=-500.0,
    entity=merchant_entity
)

guard_instance = InstancedEntity.objects.create(
    x=-410.0,
    y=-30.0,
    entity=guard_entity
)

wolf_instance_1 = InstancedEntity.objects.create(
    x=-1100.0,
    y=530.0,
    entity=wolf_entity
)

wolf_instance_2 = InstancedEntity.objects.create(
    x=-900.0,
    y=530.0,
    entity=wolf_entity
)

wolf_boss_instance = InstancedEntity.objects.create(
    x=-1020.0,
    y=475.0,
    entity=wolf_boss_entity
)

shadow_mage_instance = InstancedEntity.objects.create(
    x=-900.0,
    y=-330,
    entity=shadow_mage_entity
)

# Create Guilds
print("Creating Guilds...")
guild1 = Guild.objects.create(
    guild_name='Dragon Knights',
    created_at=timezone.now(),
    leader=game_user1
)

guild2 = Guild.objects.create(
    guild_name='Shadow Walkers',
    created_at=timezone.now(),
    leader=game_user2
)

# Create Characters
print("Creating Characters...")
character1 = Character.objects.create(
    level=5,
    xp=1000,
    hp=190,
    mp=20,
    vitality=19,
    strength=8,
    magic=5,
    character_class='Warrior',
    user=game_user1,
    guild=guild1,
    character_name='DragonSlayer',
    avatar_id=1,
    instanced_entity=player1_instance
)

character2 = Character.objects.create(
    level=4,
    xp=800,
    hp=120,
    mp=30,
    vitality=12,
    strength=6,
    magic=11,
    character_class='Mage',
    user=game_user2,
    guild=guild2,
    character_name='Spellweaver',
    avatar_id=2,
    instanced_entity=player2_instance
)

# Create Actors
print("Creating Actors...")
actor1 = Actor.objects.create(
    user=user1,
    instanced_entity=player1_instance,
    avatar_id=1
)

actor2 = Actor.objects.create(
    user=user2,
    instanced_entity=player2_instance,
    avatar_id=2
)

# Create Quests
print("Creating Quests...")
quest1 = Quest.objects.create(
    quest_id=1,
    quest_status='available'
)

quest2 = Quest.objects.create(
    quest_id=2,
    quest_status='available'
)

# Create Items
print("Creating Items...")

item0 = Item.objects.create(
    rarity='Common',
    item_name='Wolf Pelt',
    item_type='Trade Good'
)

item1 = Item.objects.create(
    rarity='Rare',
    item_name='Wolf-Tooth Blade',
    item_type='Weapon'
)

item2 = Item.objects.create(
    rarity='Epic',
    item_name='Crystal Staff',
    item_type='Weapon'
)

# Create NPCs
print("Creating NPCs...")
merchant = FriendlyNPC.objects.create(
    npc_role='Merchant',
    npc_name='Marcus the Trader',
    npc_x_location=310.0,
    npc_y_location=-500.0,
    instanced_entity=merchant_instance
)

guard = FriendlyNPC.objects.create(
    npc_role='Guard',
    npc_name='Captain Steel',
    npc_x_location=-410.0,
    npc_y_location=-30.0,
    instanced_entity=guard_instance
)

# Create Enemy NPCs
print("Creating Enemy NPCs...")
enemy1 = EnemyNPC.objects.create(
    enemy_name='Dark Wolf',
    enemy_x_location=-1100.0,
    enemy_y_location=530.0,
    enemy_health=150,
    enemy_item=item0,
    instanced_entity=wolf_instance_1
)

enemy2 = EnemyNPC.objects.create(
    enemy_name='Dark Wolf',
    enemy_x_location=-900.0,
    enemy_y_location=530.0,
    enemy_health=150,
    enemy_item=item0,
    instanced_entity=wolf_instance_2
)

enemy3 = EnemyNPC.objects.create(
    enemy_name='Dark Wolf Alpha',
    enemy_x_location=-1020.0,
    enemy_y_location=475.0,
    enemy_health=500,
    enemy_item=item1,
    instanced_entity=wolf_boss_instance
)

enemy4 = EnemyNPC.objects.create(
    enemy_name='Shadow Mage',
    enemy_x_location=-900.0,
    enemy_y_location=-330.0,
    enemy_health=1200,
    enemy_item=item2,
    instanced_entity=shadow_mage_instance
)

print("Setup complete!")