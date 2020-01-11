from collections import OrderedDict
import json

class TelegramSimpleResponse:
    """
    Simple telegram response
    message: str
    """
    def __init__(self, message):
        self.response = OrderedDict()
        simple_reponse = OrderedDict()
        responses_list = []
        responses_list.append(message)
        simple_reponse["text"] = responses_list
        self.response["text"] = simple_reponse
        self.response["platform"] = "TELEGRAM"

class TelegramMessageResponse:
    """
    message: str
    - Text of the message to be sent. It may contain html or markdown.
    Check https://core.telegram.org/bots/api/#markdown-style for supported markdown style and
    https://core.telegram.org/bots/api/#html-style for supported html style
    (Optional) parse_mode: str
    - "html" or "markdown"
    (Optional) reply_to_message_id: int
    - If the message is a reply, ID of the original message
    (Optional) disable_notification: Boolean
    - Default: False
    (Optional) disable_web_page_preview: Boolean
    - Default: False
    """
    def __init__(self, message, parse_mode="", reply_message_id=None, disable_notification=False, disable_web_page_preview=False):
        self.response = OrderedDict()
        telegram_response = dict()
        simple_reponse = OrderedDict()
        simple_reponse["text"] = message
        simple_reponse["parse_mode"] = parse_mode
        simple_reponse["disable_notification"] = disable_notification
        simple_reponse["disable_web_page_preview"] = disable_web_page_preview
        if reply_message_id is not None:
            simple_reponse["reply_to_message_id"] = reply_message_id
        telegram_response['telegram'] = simple_reponse
        self.response["payload"] = telegram_response
        self.response["platform"] = "TELEGRAM"

class TelegramKeyboardButtonResponse:
    """
    message: str
    - Text of the message to be sent.
    inline_keyboard : list
    - Array of button rows, each represented by an Array of InlineKeyboardButton objects
    Example:
    inline_keyboard = [
        {
            "text": "A",
            "callback_data": "A1"
        },
        {
            "text": "B",
            "callback_data": "C1"
        }
    ]
    """

    def __init__(self, message, inline_keyboard = []):
        self.response = OrderedDict()
        telegram_response = dict()
        simple_reponse = OrderedDict()
        simple_reponse["text"] = message
        reply_markup = dict()
        reply_markup["inline_keyboard"] = inline_keyboard
        simple_reponse["reply_markup"] = reply_markup
        telegram_response['telegram'] = simple_reponse
        self.response["payload"] = telegram_response
        self.response["platform"] = "TELEGRAM"