import time
# import pywinauto
#
# # def main():
# while True:
#     # Получаем текущее активное окно
#     try:
#         window = pywinauto.Desktop(backend="uia").active()
#         if "Chrome_WidgetWin_1" in str(window):
#             url = window.child_window(class_name="Chrome_WidgetWin_1").window_text()
#             print("Активный сайт:", url)
#         else:
#             title = window.window_text()
#             print("Активное приложение:", title)
#     except IndexError:
#         print("Нет активных окон")
#
#     # Ждем 1 секунду перед следующей проверкой
#     time.sleep(1)
#
# # if __name__ == '__main__':
# #     main()
# import time
# import psutil
#
# while True:
#     active_process = psutil.Process()
#     active_process_name = active_process.name()
#     active_process_time = active_process.cpu_times().user
#
#     print(f"Active process: {active_process_name}")
#     print(f"Time spent in active process: {active_process_time} seconds")
#     time.sleep(1)

# import win32gui
# while True:
#     active_window_handle = win32gui.GetForegroundWindow()
#     active_window_title = win32gui.GetWindowText(active_window_handle)
#     print(f"Active window title: {active_window_title}")
#
#     time.sleep(1)

# import win32api
# import win32gui
# import datetime
# import win32con
#
# def on_window_switch(event):
#     active_window_handle = win32gui.GetForegroundWindow()
#     active_window_title = win32gui.GetWindowText(active_window_handle)
#     current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     print(f'{current_time}: {active_window_title}')
#
# win32gui.SetWinEventHook(win32con.EVENT_SYSTEM_FOREGROUND, win32con.EVENT_SYSTEM_FOREGROUND, 0, on_window_switch, 0, 0, win32con.WINEVENT_OUTOFCONTEXT)
#
# while True:
#     win32api.Sleep(100)

# import ctypes
# import datetime
#
# user32 = ctypes.WinDLL('user32', use_last_error=True)
# ole32 = ctypes.WinDLL('ole32', use_last_error=True)
#
# EVENT_SYSTEM_FOREGROUND = 0x0003
# WINEVENT_OUTOFCONTEXT = 0x0000
#
# def on_window_switch(hWinEventHook, event, hwnd, idObject, idChild, dwEventThread, dwmsEventTime):
#     length = user32.GetWindowTextLengthW(hwnd)
#     buff = ctypes.create_unicode_buffer(length + 1)
#     user32.GetWindowTextW(hwnd, buff, length + 1)
#     active_window_title = buff.value
#     current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     print(f'{current_time}: {active_window_title}')
#
# WinEventProcType = ctypes.WINFUNCTYPE(
#     None, ctypes.wintypes.HANDLE, ctypes.wintypes.DWORD,
#     ctypes.wintypes.HWND, ctypes.wintypes.LONG, ctypes.wintypes.LONG,
#     ctypes.wintypes.DWORD, ctypes.wintypes.DWORD)
#
# user32.SetWinEventHook.restype = ctypes.wintypes.HANDLE
# user32.SetWinEventHook.argtypes = (
#     ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.wintypes.HMODULE,
#     WinEventProcType, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD,
#     ctypes.wintypes.DWORD)
#
# ole32.CoInitialize(None)
# WinEventProc = WinEventProcType(on_window_switch)
# user32.SetWinEventHook(EVENT_SYSTEM_FOREGROUND, EVENT_SYSTEM_FOREGROUND, 0, WinEventProc, 0, 0, WINEVENT_OUTOFCONTEXT)
#
# msg = ctypes.wintypes.MSG()
# while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
#     user32.TranslateMessageW(msg)
#     user32.DispatchMessageW(msg)

from datetime import datetime
import win32gui

def get_active_window():
    """
    Получение информации об активном окне
    """
    window = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(window)
    return window_title

prev_window = ""
prev_time = time.time()

while True:
    # Получаем информацию об активном окне
    curr_window = get_active_window()
    curr_time = datetime.now()

    # Если активное окно изменилось
    if curr_window != prev_window:
        # Выводим информацию об окне и времени, проведенном в предыдущем окне
        print(f"Window: {curr_window} Time: {curr_time}")
        prev_window = curr_window
        # prev_time = curr_time

