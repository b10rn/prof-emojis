import prof

emojis = {
        ":sleep:": u"( ᴗ˳ᴗ) zZ",
        ":kiss:": u"(づ ￣ ³￣)づ",
        ":relieved:": u"( ˘ω˘)",
        ":shrug:": u"┐(￣ε￣)┌",
        ":unamused:": u"( ¬､¬)",
        ":sad:": u"(︶︹︶)",
        ":cry:": u"(╥﹏╥)",
        ":comfy:": u"(ﾉ)'ω`(ヾ)",
        ":hey:": u"( ´◔ ω◔`) ノシ",
        ":bye:": u"( ╥﹏╥) ノシ",
        ":cute:": u"(｡◕‿‿◕｡)",
        ":astonished:": u"( 0 _ 0 )",
}

def _insert_emojis(input_str):
    result = input_str
    for code, emoji in emojis.items():
        result = result.replace(code, emoji)

    return result


def prof_pre_chat_message_send(barejid, message):
    return _insert_emojis(message)


def prof_pre_room_message_send(barejid, message):
    return _insert_emojis(message)


def prof_pre_priv_message_send(barejid, nick, message):
    return _insert_emojis(message)
