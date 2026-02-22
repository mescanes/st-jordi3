namespace SpriteKind {
    export const Princesa = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Player, function (sprite4, otherSprite) {
	
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    music.jumpUp.play()
    St_Jordi.vy = -300
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.hazardLava0, function (sprite, location) {
    music.powerDown.play()
    info.changeScoreBy(-1)
    tiles.setTileAt(location, assets.tile`transparency16`)
})
info.onCountdownEnd(function () {
    game.over(false)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`Princess`, function (sprite3, location3) {
    music.play(music.stringPlayable("C5 B A B G F E C ", 120), music.PlaybackMode.UntilDone)
    game.over(true)
})
scene.onOverlapTile(SpriteKind.Player, sprites.builtin.brick, function (sprite2, location2) {
    tiles.setTileAt(location2, assets.tile`transparency16`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`Rosa`, function (sprite5, location4) {
    music.powerUp.play()
    info.changeScoreBy(1)
    tiles.setTileAt(location4, assets.tile`transparency16`)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite6, otherSprite2) {
    music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
    info.changeScoreBy(-1)
    sprites.destroyAllSpritesOfKind(SpriteKind.Enemy, effects.clouds, 500)
})
let St_Jordi: Sprite = null
scene.setBackgroundColor(7)
tiles.setCurrentTilemap(tilemap`Skillmap1`)
info.setLife(3)
St_Jordi = sprites.create(assets.image`StJordi`, SpriteKind.Player)
controller.moveSprite(St_Jordi, 100, 0)
St_Jordi.ay = 500
scene.cameraFollowSprite(St_Jordi)
tiles.placeOnRandomTile(St_Jordi, assets.tile`myTile1`)
let Drac = sprites.create(assets.image`Drac`, SpriteKind.Enemy)
Drac.follow(St_Jordi, 80)
info.startCountdown(120)
tiles.placeOnRandomTile(Drac, assets.tile`Drac`)
