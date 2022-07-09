#!/usr/bin/which python3
"""
0.whatsapp-pywhatkit.py
send message to single WhatsApp user or a GroupID

"""
import sys
from datetime import datetime,timedelta
import argparse
import pywhatkit


def parse_arguments():
    """parse the argument list, build help and usage messages

    parses command line for
        -p --phone  (str): WhatsApp phone number to call  TODO: validate as phone #

        -g --group  (str): WhatsApp Group ID to call

    Returns:
        namespace (ns): namespace with the arguments passed and their values

    """
    parser = argparse.ArgumentParser(
        description='contact a WhatsApp user via their phone number or Group ID')
    # if omitted, the script will prompt for the phone or group id
    parser.add_argument('-p', '--phone',
                        action='store',
                        help='WhatsApp phone number',
                        required=False,
                        # nargs="?",   # command line arg w/o flag
                        )
    # if neither is passed, the phone is prompted
    parser.add_argument('-g', '--group',
                        action="store",
                        help='WhatsApp Group ID',
                        required=False
                        )
    args = parser.parse_args()
    return args  # namespace containing the argument passed on the command line


def main():
    """parse WhatsApp phone number or group ID and contact that number
    """
    args = parse_arguments()
    if args.phone:
        phone_number = args.phone
    else:
        phone_number = input("Enter phone number: ")

    # this could just as easily been now + timedelta(seconds=10)
    # but we need to pass the hours minutes and seconds
    now = datetime.now()
    call_hh = now.hour
    call_mm = now.minute

    # Send message to a contact 10 from when program was run
    # sendwhatmsg_instantly(phone_no: str,
    #                       message: str,
    #                       wait_time: int = 15,
    #                       tab_close: bool = False,
    #                       close_time: int = 3) -> None
    # sendwhatmsg( phone_no: str,
    #           message: str,
    #           time_hour: int,
    #           time_min: int,
    #           wait_time: int = 15,
    #           tab_close: bool = False,
    #           close_time: int = 3)
    pywhatkit.sendwhatmsg_instantly('+1' + phone_number, "Instant Test")
    # pywhatkit.sendwhatmsg('+1' + phone_number, "Test", call_hh, call_mm+2)
    pywhatkit.sendwhatmsg('+1' + phone_number,
                          "Test...wait 7...close....close=2",
                          call_hh, call_mm+1,
                          7, True, 2
                          )

    if args.group:
        group_id = args.group
    else:
        group_id = input("Enter group id: ")

    # Send message to a group
    # sendwhatmsg_to_group( group_id: str,
    #                       message: str,
    #                       time_hour: int,
    #                       time_min: int,
    #                       wait_time: int = 15,
    #                       tab_close: bool = False,
    #                       close_time: int = 3) -> None
    pywhatkit.sendwhatmsg_to_group(group_id,
                                   "Test Group",
                                   call_hh, call_mm+3
                                   )
    return 0


if __name__ == '__main__':
    sys.exit(main())
