from machine import UART, Pin


CMD_PREFIX="7E FF 06"
CMD_SUFFIX="EF"


uart = UART(0, 9600, tx=Pin(0), rx=Pin(1))


def to_hex(dec_str):
    num = int(dec_str)
    hex_str = hex(num)[2:].upper()
    
    if len(hex_str) % 2 != 0:
        hex_str = '0' + hex_str
    
    return hex_str


def send_uart(cmd):
    uart.write(bytearray.fromhex(cmd.replace(" ", "")))
    
    
def next_song():
    cmd=f"{CMD_PREFIX} 01 00 00 00 {CMD_SUFFIX}"
    send_uart(cmd)


def prev_song():
    cmd=f"{CMD_PREFIX} 02 00 00 00 {CMD_SUFFIX}"
    send_uart(cmd)


def play_with_index(index):
    cmd=f"{CMD_PREFIX} 03 00 00 {to_hex(index)} {CMD_SUFFIX}"
    send_uart(cmd)


def volume_up():
    cmd=f"{CMD_PREFIX} 04 00 00 00 {CMD_SUFFIX}"
    send_uart(cmd)


def volume_up():
    cmd=f"{CMD_PREFIX} 05 00 00 00 {CMD_SUFFIX}"
    send_uart(cmd)


def set_volume(volume):
    cmd=f"{CMD_PREFIX} 06 00 00 {to_hex(volume)} {CMD_SUFFIX}"
    send_uart(cmd)


def single_cicle_play():
    cmd=f"{CMD_PREFIX} 08 00 00 01 {CMD_SUFFIX}"
    send_uart(cmd)
    

def set_storage_device():
    cmd=f"{CMD_PREFIX} 09 00 00 02 {CMD_SUFFIX}"
    send_uart(cmd)
    
    
def sleep_mode():
    cmd=f"{CMD_PREFIX} 0A 00 00 00 {CMD_SUFFIX}"
    send_uart(cmd)
    

def wake_up():
    cmd=f"{CMD_PREFIX} 0B 00 00 00 {CMD_SUFFIX}"
    send_uart(cmd)
    

def reset():
    cmd=f"{CMD_PREFIX}0C 00 00 00 {CMD_SUFFIX}"
    send_uart(cmd)
    

def play():
    cmd=f"{CMD_PREFIX} 0D 00 00 00 {CMD_SUFFIX}"
    send_uart(cmd)
    

def pause():
    cmd=f"{CMD_PREFIX} 0E 00 00 00 {CMD_SUFFIX}"
    send_uart(cmd)
    

def play_with_folder_and_filename(folder, song):
    cmd=f"{CMD_PREFIX} 0F 00 {to_hex(folder)} {to_hex(song)} {CMD_SUFFIX}"
    send_uart(cmd)
    
    
def stop_play():
    cmd=f"{CMD_PREFIX} 16 00 00 00 {CMD_SUFFIX}"
    

def cycle_play_with_folder_name(folder):
    cmd=f"{CMD_PREFIX} 17 00 00 {to_hex(folder)} {CMD_SUFFIX}"
    send_uart(cmd)
    

def shuffle_play():
    cmd=f"{CMD_PREFIX} 18 00 00 00 {CMD_SUFFIX}"
    

def set_single_cycle_play():
    cmd=f"{CMD_PREFIX} 19 00 00 00 {CMD_SUFFIX}"