import psutil
import subprocess
import os
import ctypes
import time

def kill_ghub():
    # 遍历系统中的所有进程并终止 G HUB 相关进程
    for proc in psutil.process_iter():
        try:
            if "lghub" in proc.name().lower():  # G HUB 进程名可能是 "lghub.exe"
                print(f"Terminating process {proc.name()} (PID: {proc.pid})")
                proc.terminate()  # 终止进程
                proc.wait()  # 等待进程终止
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def is_admin():
    # 检查当前进程是否具有管理员权限
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def restart_ghub_as_admin():
    ghub_path = r"C:\Program Files\LGHUB\lghub.exe"  # G HUB 的安装路径
    if os.path.exists(ghub_path):
        if is_admin():
            print("Running as admin. Restarting G HUB...")
            subprocess.run([ghub_path], check=True)
        else:
            print("Requesting admin privileges to restart G HUB...")
            # 重新以管理员权限运行 G HUB
            ctypes.windll.shell32.ShellExecuteW(None, "runas", ghub_path, None, None, 1)
    else:
        print(f"Logitech G HUB executable not found at {ghub_path}")

if __name__ == "__main__":
    kill_ghub()  # 关闭 G HUB
    time.sleep(2)  # 等待2秒
    restart_ghub_as_admin()  # 以管理员身份重新启动 G HUB
