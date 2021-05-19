class ActionKind(Enum):
    Walking = 0
    Idle = 1
    Jumping = 2
    walk_right = 3

def on_left_pressed():
    Michael.x += -5
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    Michael.x += 5
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

toco: Sprite = None
strawberry: Sprite = None
pizza: Sprite = None
donut: Sprite = None
chicken: Sprite = None
cake: Sprite = None
burger: Sprite = None
apple: Sprite = None
Michael: Sprite = None
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
speed = 20
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
Michael.set_position(80, 103)
Michael.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
info.start_countdown(60)
seconds = 60
foodd = [apple, burger, cake, chicken, donut, pizza, strawberry, toco]

def on_update_interval():
    global apple, burger, cake, chicken, donut, pizza, strawberry, toco, speed
    apple = sprites.create_projectile_from_side(img("""
            . . . . . . . e c 7 . . . . . . 
                    . . . . e e e c 7 7 e e . . . . 
                    . . c e e e e c 7 e 2 2 e e . . 
                    . c e e e e e c 6 e e 2 2 2 e . 
                    . c e e e 2 e c c 2 4 5 4 2 e . 
                    c e e e 2 2 2 2 2 2 4 5 5 2 2 e 
                    c e e 2 2 2 2 2 2 2 2 4 4 2 2 e 
                    c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                    c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                    c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                    c e e 2 2 2 2 2 2 2 2 2 2 4 2 e 
                    . e e e 2 2 2 2 2 2 2 2 2 4 e . 
                    . 2 e e 2 2 2 2 2 2 2 2 4 2 e . 
                    . . 2 e e 2 2 2 2 2 4 4 2 e . . 
                    . . . 2 2 e e 4 4 4 2 e e . . . 
                    . . . . . 2 2 e e e e . . . . .
        """),
        50,
        speed)
    apple.y = randint(0, 160)
    burger = sprites.create_projectile_from_side(img("""
            . . . . c c c b b b b b . . . . 
                    . . c c b 4 4 4 4 4 4 b b b . . 
                    . c c 4 4 4 4 4 5 4 4 4 4 b c . 
                    . e 4 4 4 4 4 4 4 4 4 5 4 4 e . 
                    e b 4 5 4 4 5 4 4 4 4 4 4 4 b c 
                    e b 4 4 4 4 4 4 4 4 4 4 5 4 4 e 
                    e b b 4 4 4 4 4 4 4 4 4 4 4 b e 
                    . e b 4 4 4 4 4 5 4 4 4 4 b e . 
                    8 7 e e b 4 4 4 4 4 4 b e e 6 8 
                    8 7 2 e e e e e e e e e e 2 7 8 
                    e 6 6 2 2 2 2 2 2 2 2 2 2 6 c e 
                    e c 6 7 6 6 7 7 7 6 6 7 6 c c e 
                    e b e 8 8 c c 8 8 c c c 8 e b e 
                    e e b e c c e e e e e c e b e e 
                    . e e b b 4 4 4 4 4 4 4 4 e e . 
                    . . . c c c c c e e e e e . . .
        """),
        50,
        speed)
    burger.x = randint(0, 10)
    cake = sprites.create_projectile_from_side(img("""
            . . . . . . . . . . b b b . . . 
                    . . . . . . . . b e e 3 3 b . . 
                    . . . . . . b b e 3 2 e 3 a . . 
                    . . . . b b 3 3 e 2 2 e 3 3 a . 
                    . . b b 3 3 3 3 3 e e 3 3 3 a . 
                    b b 3 3 3 3 3 3 3 3 3 3 3 3 3 a 
                    b 3 3 3 d d d d 3 3 3 3 3 d d a 
                    b b b b b b b 3 d d d d d d 3 a 
                    b d 5 5 5 5 d b b b a a a a a a 
                    b 3 d d 5 5 5 5 5 5 5 d d d d a 
                    b 3 3 3 3 3 3 d 5 5 5 d d d d a 
                    b 3 d 5 5 5 3 3 3 3 3 3 b b b a 
                    b b b 3 d 5 5 5 5 5 5 5 d d b a 
                    . . . b b b 3 d 5 5 5 5 d d 3 a 
                    . . . . . . b b b b 3 d d d b a 
                    . . . . . . . . . . b b b a a .
        """),
        50,
        speed)
    cake.x = randint(0, 10)
    chicken = sprites.create_projectile_from_side(img("""
            . . 2 2 b b b b b . . . . . . . 
                    . 2 b 4 4 4 4 4 4 b . . . . . . 
                    2 2 4 4 4 4 d d 4 4 b . . . . . 
                    2 b 4 4 4 4 4 4 d 4 b . . . . . 
                    2 b 4 4 4 4 4 4 4 d 4 b . . . . 
                    2 b 4 4 4 4 4 4 4 4 4 b . . . . 
                    2 b 4 4 4 4 4 4 4 4 4 e . . . . 
                    2 2 b 4 4 4 4 4 4 4 b e . . . . 
                    . 2 b b b 4 4 4 b b b e . . . . 
                    . . e b b b b b b b e e . . . . 
                    . . . e e b 4 4 b e e e b . . . 
                    . . . . . e e e e e e b d b b . 
                    . . . . . . . . . . . b 1 1 1 b 
                    . . . . . . . . . . . c 1 d d b 
                    . . . . . . . . . . . c 1 b c . 
                    . . . . . . . . . . . . c c . .
        """),
        50,
        speed)
    chicken.x = randint(0, 10)
    donut = sprites.create_projectile_from_side(img("""
            . . . . . . b b b b a a . . . . 
                    . . . . b b d d d 3 3 3 a a . . 
                    . . . b d d d 3 3 3 3 3 3 a a . 
                    . . b d d 3 3 3 3 3 3 3 3 3 a . 
                    . b 3 d 3 3 3 3 3 b 3 3 3 3 a b 
                    . b 3 3 3 3 3 a a 3 3 3 3 3 a b 
                    b 3 3 3 3 3 a a 3 3 3 3 d a 4 b 
                    b 3 3 3 3 b a 3 3 3 3 3 d a 4 b 
                    b 3 3 3 3 3 3 3 3 3 3 d a 4 4 e 
                    a 3 3 3 3 3 3 3 3 3 d a 4 4 4 e 
                    a 3 3 3 3 3 3 3 d d a 4 4 4 e . 
                    a a 3 3 3 d d d a a 4 4 4 e e . 
                    . e a a a a a a 4 4 4 4 e e . . 
                    . . e e b b 4 4 4 4 b e e . . . 
                    . . . e e e e e e e e . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        50,
        speed)
    donut.x = randint(0, 10)
    pizza = sprites.create_projectile_from_side(img("""
            . . . . . . b b b b . . . . . . 
                    . . . . . . b 4 4 4 b . . . . . 
                    . . . . . . b b 4 4 4 b . . . . 
                    . . . . . b 4 b b b 4 4 b . . . 
                    . . . . b d 5 5 5 4 b 4 4 b . . 
                    . . . . b 3 2 3 5 5 4 e 4 4 b . 
                    . . . b d 2 2 2 5 7 5 4 e 4 4 e 
                    . . . b 5 3 2 3 5 5 5 5 e e e e 
                    . . b d 7 5 5 5 3 2 3 5 5 e e e 
                    . . b 5 5 5 5 5 2 2 2 5 5 d e e 
                    . b 3 2 3 5 7 5 3 2 3 5 d d e 4 
                    . b 2 2 2 5 5 5 5 5 5 d d e 4 . 
                    b d 3 2 d 5 5 5 d d d 4 4 . . . 
                    b 5 5 5 5 d d 4 4 4 4 . . . . . 
                    4 d d d 4 4 4 . . . . . . . . . 
                    4 4 4 4 . . . . . . . . . . . .
        """),
        50,
        speed)
    pizza.x = randint(0, 10)
    strawberry = sprites.create_projectile_from_side(img("""
            . . . . . . . 6 . . . . . . . . 
                    . . . . . . 8 6 6 . . . 6 8 . . 
                    . . . e e e 8 8 6 6 . 6 7 8 . . 
                    . . e 2 2 2 2 e 8 6 6 7 6 . . . 
                    . e 2 2 4 4 2 7 7 7 7 7 8 6 . . 
                    . e 2 4 4 2 6 7 7 7 6 7 6 8 8 . 
                    e 2 4 5 2 2 6 7 7 6 2 7 7 6 . . 
                    e 2 4 4 2 2 6 7 6 2 2 6 7 7 6 . 
                    e 2 4 2 2 2 6 6 2 2 2 e 7 7 6 . 
                    e 2 4 2 2 4 2 2 2 4 2 2 e 7 6 . 
                    e 2 4 2 2 2 2 2 2 2 2 2 e c 6 . 
                    e 2 2 2 2 2 2 2 4 e 2 e e c . . 
                    e e 2 e 2 2 4 2 2 e e e c . . . 
                    e e e e 2 e 2 2 e e e c . . . . 
                    e e e 2 e e c e c c c . . . . . 
                    . c c c c c c c . . . . . . . .
        """),
        50,
        speed)
    strawberry.x = randint(0, 10)
    toco = sprites.create_projectile_from_side(img("""
            . . . . . . . e e e e . . . . . 
                    . . . . . e e 4 5 5 5 e e . . . 
                    . . . . e 4 5 6 2 2 7 6 6 e . . 
                    . . . e 5 6 6 7 2 2 6 4 4 4 e . 
                    . . e 5 2 2 7 6 6 4 5 5 5 5 4 . 
                    . e 5 6 2 2 8 8 5 5 5 5 5 4 5 4 
                    . e 5 6 7 7 8 5 4 5 4 5 5 5 5 4 
                    e 4 5 8 6 6 5 5 5 5 5 5 4 5 5 4 
                    e 5 c e 8 5 5 5 4 5 5 5 5 5 5 4 
                    e 5 c c e 5 4 5 5 5 4 5 5 5 e . 
                    e 5 c c 5 5 5 5 5 5 5 5 4 e . . 
                    e 5 e c 5 4 5 4 5 5 5 e e . . . 
                    e 5 e e 5 5 5 5 5 4 e . . . . . 
                    4 5 4 e 5 5 5 5 e e . . . . . . 
                    . 4 5 4 5 5 4 e . . . . . . . . 
                    . . 4 4 e e e . . . . . . . . .
        """),
        50,
        speed)
    toco.x = randint(0, 10)
    speed += 5
game.on_update_interval(5000, on_update_interval)
