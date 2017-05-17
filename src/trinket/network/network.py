class Network:

    TYPE_PACKET_UNKNOWN = 00
    TYPE_PACKET_DUMMY = 1
    TYPE_PACKET_LOGIN = 68
    TYPE_PACKET_DISCONNECT = 82
    TYPE_PACKET_COMMAND = 93
    TYPE_PACKET_DATA_REQUEST = 37
    TYPE_PACKET_DATA_SEND = 45
    TYPE_PACKET_COMMAND_EXECUTE = 89

    TYPE_DISCONNECT_FORCED = 11000001

    TYPE_ERROR_INVALID_PASSWORD = 10101010
    TYPE_ERROR_INVALID_PACKET = 10111000
    TYPE_ERROR_EMPTY = 11100111

    TYPE_SELECTION_PLAYERS_ALL = 10001101
    TYPE_SELECTION_PLAYERS_OP = 10111001

    TYPE_DATA_CLIENTLIST = 10010000
    TYPE_DATA_CHAT = 11001000