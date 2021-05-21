def foodFalling():
    global falling
    if True:
        falling = sprites.create(list2[randint(0, len(list2) - 0)], SpriteKind.projectile)
    falling.vy = randint(10, 20)
    falling.y = -10
    falling.x = randint(10, 160)

def on_left_pressed():
    Michael.x += -5
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_countdown_end():
    game.over(True, effects.confetti)
info.on_countdown_end(on_countdown_end)

def on_right_pressed():
    Michael.x += 5
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

list2: List[Image] = []
falling: Sprite = None
Michael: Sprite = None
class ActionKind(Enum):
    Walking = 0
    Idle = 1
    Jumping = 2
    walk_right = 3
scene.set_background_image(img("""
    dddbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbbddcdddddddddddddddddddddddcbbbbbdddddddddddddddd
        ddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddcdddddddddddddddddddddddcbbbbddddddddddddddddd
        dddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbddddcdddddddddddddddddddddddcbbddddddddddddddddddd
        ddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddcdddddddddddddddddddddddcbbddddddddddddddddddd
        dddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbddddddcdddddddddddddddddddddddcbdddddddddddddddddddd
        ddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddcdddddddddddddddddddddddcbdddddddddddddddddddd
        dddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbddddddddcdddddddddddddddddddddddcddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcdddddddddddddddddddddbdcdbddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcdddddddddddddddddddddbdcdbddddddddddddddddddd
        dddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbddddddddcdddddddddddddddddddddbdcdbddddddddddddddddddd
        ddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddcdddddddddddddddddddddbdcdbddddddddddddddddddd
        dddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbddddddcdddddddddddddddddddddbdcdbddddddddddddddddddd
        ddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddcdddddddddddddddddddddbdcdbddddddddddddddddddd
        dddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbddddcdddddddddddddddddddddbdcdbddddddddddddddddddd
        ddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddcbddddddddddddddddddddbdcdbddddddddddddddddddd
        dddbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbbddcbddddddddddddddddddddbdcdbddddddddddddddddddd
        ddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddcbddddddddddddddddddddbdcdbddddddddddddddddddd
        dddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbddddcbbdddddddddddddddddddbdcdbddddddddddddddddddd
        ddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddcbbdddddddddddddddddddbdcdbddddddddddddddddddd
        dddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbddddddcbbdddddddddddddddddddbdcdbddddddddddddddddddd
        ddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddcbbdddddddddddddddddddbdcdbddddddddddddddddddd
        dddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbddddddddcbbdddddddddddddddddddbdcdbddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcbbdddddddddddddddddddbdcdbddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcbbdddddddddddddddddddbdcdbddddddddddddddddddd
        dddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbddddddddcbbbddddddddddddddddddbdcdbddddddddddddddddddd
        ddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddcbbbddddddddddddddddddbdcdbddddddddddddddddddd
        dddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbddddddcbbbbdddddddddddddddddddcddddddddddddddddddddd
        ddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddcbbbbddddddddddddddccdddcdddccdddddddddddddddd
        dddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbddddcbbbbbddddddddddddceecddcddceecddddddddddddddd
        ddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddcbbbbbbdddddddddddceecddcddceecddddddddddddddd
        dddbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbbddcbbbbbbbdddddddddddccdddcdddccdddddddddddddddd
        ddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddcbbbbbbbbdddddddddddddddcddddddddddddddddddddd
        dddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbddddcbbbbbbbbbddddddddddddddcddddddddddddddddddddd
        ddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbddddddccccccccccccccccccccccccccccccccccccccccccccc
        dddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddccccccddbbbbbdddddddddddbbbbbdddddddceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        ddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbddddccccccdddbbbdddddddddddddbbbddddddddceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        dddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddccccccddddbdddddddddddddddbdddddddddceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddc999999cdddddddddddddddddddddddddddddceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddc999999cdddddddddddddddddddddddddddddceeeeeeeeeeebbbbbbeeeeeeeeeebbbbbbbbbbbbbbbbb
        dddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddcccddddc999999cdddbdddddddddddddddbdddddddddccccccccccccccccccccccccccccccccccccccccccccc
        ddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbddddddddddddcccbdddc999999cddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbddddd
        dddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbddddddddddcccccbddc111111cdbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddd
        ddddddbbbbbbbddccccccccccccccccccccccccccccccccccdddddbbbbbbbdddddddddc999cbbdc111111cbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbddd
        dddddbbbbbbbbbccddddddddddddddddddddddddddddddddccdddbbbbbbbbbdddddddbc999cbbbc111111cbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdd
        ddddbbbbbbbbbccddddddddddddddddddddddddddbbbbddddccdbbbbbbbbbbbdddddbbc999cbbbc111111cbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbd
        dddbbbbbbbbbbcdddddddddddddddddddddddddddddbbbbdddcbbbbbbbbbbbbbdddbbbc666cbbbc111111cbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbb
        ddddbbbbbbbbbcddddddddddddddddddddddddddddddddbbbdcdbbbbbbbbbbbdddddbbc666cbbbc111111cbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbd
        dddddbbbbbbbbcdddddddddddddddddddddddddddddddddbbdcddbbbbbbbbbdddddddbc666cbbbc111111cbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdd
        ddddddbbbbbbbcdbbdbdddddddddddddddddddddddddddddbdcdddbbbbbbbdddddddddc666cbbdc111111cbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbddd
        dddddddbbbbbdcdbbdddddddddddddddddddddddddddddddbdcddddbbbbbddddddddccccccccccccccccccccbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddd
        ddddddddbbbddcdbbdbdddddddddddddddddddddddddddddbdcdddddbbbddddddddccccccccccccccccccccccbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbddddd
        dddddddddbdddcdbbdbdddddddddddddddddddddddddddddbdcddddddbddddddddddccccccccccccccccccccdbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddd
        dddddddddddddcdbbdddddddddddddddddddddddddddddddddcddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddcdbbdddddddddddddddddddddddddddddddddcddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddbdddcdbbbddddddddddddddddddddddddddddddddcddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddd
        ddddddddbbbddcdbbbbdddddddddddddddddddddddddddddddcdddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbddddd
        dddddddbbbbbdcdbbbbbddddddddddddddddddddddddddddddcddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddd
        ddddddbbbbbbbcdbdbbbbbbbbdddddddddddddddddddddddddcdddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbddd
        dddddbbbbbbbbcdbddbbbbbbbbdbbbddbdddddddddddddddddcddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdd
        ddddbbbbbbbbbcdbddddddddddddddddddddddddddddddddddcdbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbd
        dddbbbbbbbbbbcdbddccccccccccccccccccccccccccccddddcbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbbdddbbbbbbbbbbbbb
        ddddbbbbbbbbbcdbdcbbbbbbbbbbbbbbbbbbbbbbbbbbbbcdddcdbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbdddddbbbbbbbbbbbd
        dddddbbbbbbbbcdbddccccccccccccccccccccccccccccddddcddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdd
        ddddddbbbbbbbcddddddddddddddddddddddddddddddddddddcdddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbddd
        dddddddbbbbbdccccccccccccccccccccccccccccccccccccccddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddd
        ddddddddbbbddcddddddddddddddddddddddddddddddddddddcdddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbddddd
        dddddddddbdddcddddccccccccccccccccccccccccccccddddcddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddd
        dddddddddddddcdddcbbbbbbbbbbbbbbbbbbbbbbbbbbbbcdddcddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddcddddccccccccccccccccccccccccccccddddcddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddbdddcddddddddddddddddddddddddddddddddddddcddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddddddddddddbdddddd
        ddddddddbbbddcdbddddddddddddddddddddddddddddddddddcdddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbdddddddddddddbbbddddd
        dddddddbbbbbdcdbddddddddddddddddddddddddddddddddddcddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddddddddddbbbbbdddd
        ddddddbbbbbbbcdbdddddddddddddcccddddddddddddddddddcdddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbdddddddddbbbbbbbddd
        dddddbbbbbbbbcdbdddddddddddcccccccddddddddddddddddcddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdddddddbbbbbbbbbdd
        ccccccccccccccdbdddddddddddc1ccc1cddddddddddddddddcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        aaaaaaaaaaaaacdbdddddddddddc11111cddddddddddddddddcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        aaaaaaaaaaaaacdbdccccccddddc11111cddddccccccddddddcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        ccccccccccccccdbdc9999cddddc11111cddddc3333cddddddcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        aacaaaaacaaaacdbdc9c99cddddc11111cddddc3333cddddddcaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaacaa
        aacaaaaacaaaacdbdc9cc9cddddcccccccddddc3333cddddddcaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaaacaaaacaa
        aacaaaaacaaaacdbdc9999cdddddddddddddddc3333cddddddcaaaaacaaaaacaaaaacaaaaacaaacccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccaaaacaa
        aacaaaaacaaaacdbdc999cddddddddddddddddccccccddddddcaaaaacaaaaacaaaaacaaaaacaaacdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcaaaacaa
        aacaaaaacaaaacdbdc99cdddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccaaaacaa
        aacaaaaacaaaacdbdcccddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcaaaacaa
        aacaaaaacaaaacdbddddddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacdcccccccdddddddddddddddddddddddddddddddddddddddddddddddddddddddddcccccccdcaaaacaa
        aacaaaaacaaaacdbddddddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacddcccccddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddcccccddcaaaacaa
        aacaaaaacaaaacdbbdddddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcaaaacaa
        aacaaaaacaaaacdbbbddddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccaaaacaa
        aacaaaaacaaaacdbbbddddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacbbbbbbddddddddddddcbbbbddddddddddddddcbbbbdddddddddddddcbbbdddddddddddddbcaaaacaa
        aacaaaaacaaaacdbbbddddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacbbbbddddddddddddddcbbddddddddddddddddcbbbddddddddddddddcbbddddddddddddddbcaaaacaa
        aacaaaaacaaaacdbbbddddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacbbbddddddddddccdddcbdccddddddddddddddcbbdddddddddddccddcbdccddddddddddddbcaaaacaa
        aacaaaaacaaaacdbbbddddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacbbbdddddddddceecddcbceecdddddddddddddcbdddddddddddceecdcbceecdddddddddddbcaaaacaa
        aacaaaaacaaaacdbbbddddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacbbddddddddddceecddcbceecdddddddddddddcbdddddddddddceecdcbceecdddddddddddbcaaaacaa
        aacaaaaacaaaacdbbbddddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacbbdddddddddddccdddcbdccddddddddddddddcbddddddddddddccddcddccddddddddddddbcaaaacaa
        aacaaaaacaaaacdbbbddddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacbdddddddddddddddddcbdddddddddddddddddcbddddddddddddddddcddddddddddddddddbcaaaacaa
        aacaaaaacaaaacdbbbddddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacbdddddddddddddddddcbdddddddddddddddddcbddddddddddddddddcddddddddddddddddbcaaaacaa
        aacaaaaacaaaacdbbbddddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacbdddddddddddddddddcbdddddddddddddddddcdddddddddddddddddcddddddddddddddddbcaaaacaa
        aacaaaaacaaaacdbbbddddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacbdddddddddddddddddcbdddddddddddddddddcdddddddddddddddddcddddddddddddddddbcaaaacaa
        aacaaaaacaaaacdbbbddddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacbdddddddddddddddddcbdddddddddddddddddcdddddddddddddddddcddddddddddddddddbcaaaacaa
        aacaaaaacaaaacdbbbddddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacbdddddddddddddddddcbdddddddddddddddddcdddddddddddddddddcddddddddddddddddbcaaaacaa
        aacaaaaacaaaacdbbbddddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacbdddddddddddddddddcbdddddddddddddddddcdddddddddddddddddcddddddddddddddddbcaaaacaa
        aacaaaaacaaaacdbbbddddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacbdddddddddddddddddcddddddddddddddddddcdddddddddddddddddcdddddddddddddddddcaaaacaa
        aacaaaaacaaaacdbbbddddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacbdddddddddddddddddcddddddddddddddddddcdddddddddddddddddcdddddddddddddddddcaaaacaa
        aacaaaaacaaaacdbbbbdddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacbdddddddddddddddddcddddddddddddddddddcdddddddddddddddddcdddddddddddddddddcaaaacaa
        aacaaaaacaaaacdbbbbbddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacbdddddddddddddddddcddddddddddddddddddcdddddddddddddddddcdddddddddddddddddcaaaacaa
        aacaaaaacaaaacdbbbbbddddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacbdddddddddddddddddcddddddddddddddddddcdddddddddddddddddcdddddddddddddddddcaaaacaa
        aacaaaaacaaaacdbbbbbbdddddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacbdddddddddddddddddcddddddddddddddddddcdddddddddddddddddcdddddddddddddddddcaaaacaa
        aacaaaaacaaaacdbbbbbbbbbddddddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacbdddddddddddddddddcddddddddddddddddddcdddddddddddddddddcdddddddddddddddddcaaaacaa
        aacaaaaacaaaacdbbbbbbbbbbbbdddddddddddddddddddddddcaaaaacaaaaacaaaaacaaaaacaaacbdddddddddddddddddcddddddddddddddddddcdddddddddddddddddcdddddddddddddddddcaaaacaa
        ccccccccccccccddbbbbbbbbbbbbbbbbbbbbbbddddddddddddcccccccccccccccccccccccccccccbdddddddddddddddddcddddddddddddddddddcdddddddddddddddddcdddddddddddddddddcccccccc
        aaaaaaaaaaaaacdddbbbbbbbbbbbbbbbbbbbbbbbbbddddddddcaaaaaaaaaaaaaaaaaaaaaaaaaaacddddddddddddddddddcddddddddddddddddddcdddddddddddddddddcdddddddddddddddddcaaaacaa
        aaaaaaaaaaaaacddddddddddddddddddddddddddddddddddddcaaaaaaaaaaaaaaaaaaaaaaaaaaacddddddddddddddddddcddddddddddddddddddcdddddddddddddddddcdddddddddddddddddcaaaacaa
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        eedddceedddceedddceedddceedddceedddceedddceedddceedddceedddceedddceedddceedddceedddceedddceedddceedddceedddceedddceedddceedddceedddceedddceedddceedddceedddceddd
        eeeedceeeedceeeedceeeedceeeedceeeedceeeedceeeedceeeedceeeedceeeedceeeedceeeedceeeedceeeedceeeedceeeedceeeedceeeedceeeedceeeedceeeedceeeedceeeedceeeedceeeedceeed
        eeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeee
        cccccdcccccdcccccdcccccdcccccdcccccdcccccdcccccdcccccdcccccdcccccdcccccdcccccdcccccdcccccdcccccdcccccdcccccdcccccdcccccdcccccdcccccdcccccdcccccdcccccdcccccdcccc
        eeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeee
        eeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeee
        eeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeeeeceeee
"""))
tiles.set_tilemap(tilemap("""
    level2
"""))
game.show_long_text(" Welcome to food fall !", DialogLayout.TOP)
game.show_long_text("Your objective is to catch as many falling food items in 60 seconds. Good luck!",
    DialogLayout.TOP)
info.set_score(0)
Michael = sprites.create(img("""
        ..................
            ..................
            ..................
            .ffffffffffffffff.
            .f51155555555555f.
            .f33333333333333f.
            .f51155555555555f.
            .f31155555555555f.
            ..f535555555555f..
            ...f5353535555f...
            ....f53535355f....
            .....ffffffff.....
            .......ffff.......
            .....ffffffff.....
            ....ffffffcfff....
            ...ffffffccfffc...
            ...fffcfffffffc...
            ...cccfffeeffcc...
            ...fffffeeffccf...
            ...fffbfeefbfff...
            ....f41f44f14f....
            ....fe444444ef....
            ....fffeeeefff....
            ...fefb7777bfef...
            ...e4f777777f4e...
            ...eef666666fee...
            ......ffffff......
            ......ff..ff......
    """),
    SpriteKind.player)
falling = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.projectile)
Michael.set_position(80, 103)
Michael.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
info.start_countdown(60)
list2 = [assets.image("""
        apple
    """),
    assets.image("""
        burger
    """),
    assets.image("""
        cake
    """),
    assets.image("""
        chicken
    """),
    assets.image("""
        donut
    """),
    assets.image("""
        pizza
    """),
    assets.image("""
        strawberry
    """),
    assets.image("""
        taco
    """)]

def on_update_interval():
    foodFalling()
game.on_update_interval(3200, on_update_interval)
