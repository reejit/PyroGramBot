import random
from pyrogram import Client, filters
from pyrobot import COMMAND_HAND_LER
from pyrobot.helper_functions.cust_p_filters import f_onw_fliter


RUN_STRINGS = (
    "Shajietta, we have become the underworld without even knowing it ...",
    "Call me bad ... good thunder if you want ... but don't advise .....",
    "Oh bloody villagers!",
    "See Maggie I'm going to pay the bill.",
    "Go with me!",
    "Motherfucker is not over !!",
    "I will lock up the person who did this, Sabarimala Sastha, Hariharasuthan, under a good watch.",
    "I saw ... !! Kindi ... Kindi ...!",
    "Give it to Monta and show him the ISI mark", ""
    "Davisetta, Kingfisher ... Child ...!.",
    "Did your father make porridge and chicken for midnight ....",
    "This is our tool, King.",
    "If you don't play, I'll feed you tamarind ....",
    "If only we could have a beer ...",
    "Oh then when you all love it is love .... When we all love it is wire ...",
    "Is not the liar the liar of the carp .....",
    "Dr. Vijaya, why did we not feel this wisdom before ...!",
    "Where have you been for so long ....!",
    "God save me alone ....",
    "I know his father's name is Bhavaniamma ...",
    "Da Dasa ... what a mess .....",
    "Salt English English Salt Mango Tree .....",
    "Children .. don't try to send sand to Rajasthan desert .....",
    "Your father, Paul Barber ...",
    "Car Engine Out Completely .....",
    "Is it the eye or the magnet ...",
    "I'll be there before the ice cubes fall on the fourth peg .....",
    "The stone and the wet rain that drank for her was a waste ....",
    "Tell me I love you ...",
    "No, it's not Meenakshi from Waryampilly ... what a mole on a scooter ...."
)


@Client.on_message(
    filters.command("runs", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def runs(_, message):
    """ /runs strings """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
