# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp.http import route
from mierp.addons.mail.controllers.message_reaction import MessageReactionController
from mierp.addons.im_livechat.tools.misc import force_guest_env


class LivechatMessageReactionController(MessageReactionController):
    @route("/im_livechat/cors/message/reaction", methods=["POST"], type="json", auth="public", cors="*")
    def livechat_message_reaction(self, guest_token, message_id, content, action, **kwargs):
        force_guest_env(guest_token)
        return self.mail_message_reaction(message_id, content, action, **kwargs)
