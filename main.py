@namespace
class SpriteKind:
    Princesa = SpriteKind.create()

def on_on_overlap(sprite4, otherSprite):
    pass
sprites.on_overlap(SpriteKind.player, SpriteKind.player, on_on_overlap)

def on_a_pressed():
    music.jump_up.play()
    St_Jordi.vy = -300
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile(sprite, location):
    music.power_down.play()
    info.change_score_by(-1)
    tiles.set_tile_at(location, assets.tile("""
        transparency16
        """))
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava0,
    on_overlap_tile)

def on_countdown_end():
    game.over(False)
info.on_countdown_end(on_countdown_end)

def on_overlap_tile2(sprite3, location3):
    music.play(music.string_playable("C5 B A B G F E C ", 120),
        music.PlaybackMode.UNTIL_DONE)
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        Princess
        """),
    on_overlap_tile2)

def on_overlap_tile3(sprite2, location2):
    tiles.set_tile_at(location2, assets.tile("""
        transparency16
        """))
scene.on_overlap_tile(SpriteKind.player, sprites.builtin.brick, on_overlap_tile3)

def on_overlap_tile4(sprite5, location4):
    music.power_up.play()
    info.change_score_by(1)
    tiles.set_tile_at(location4, assets.tile("""
        transparency16
        """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        Rosa
        """),
    on_overlap_tile4)

def on_on_overlap2(sprite6, otherSprite2):
    music.play(music.melody_playable(music.pew_pew),
        music.PlaybackMode.UNTIL_DONE)
    info.change_score_by(-1)
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy, effects.clouds, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

St_Jordi: Sprite = None
scene.set_background_color(7)
tiles.set_current_tilemap(tilemap("""
    Skillmap1
    """))
info.set_life(3)
St_Jordi = sprites.create(assets.image("""
    StJordi
    """), SpriteKind.player)
controller.move_sprite(St_Jordi, 100, 0)
St_Jordi.ay = 500
scene.camera_follow_sprite(St_Jordi)
tiles.place_on_random_tile(St_Jordi, assets.tile("""
    myTile1
    """))
Drac = sprites.create(assets.image("""
    Drac
    """), SpriteKind.enemy)
Drac.follow(St_Jordi, 80)
info.start_countdown(120)
tiles.place_on_random_tile(Drac, assets.tile("""
    Drac
    """))