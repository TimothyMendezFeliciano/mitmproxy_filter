import winreg
import os
import subprocess

def set_windows_proxy(proxy_ip="127.0.0.1", proxy_port="8080"):
    """ Enable system-wide proxy """
    try:
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, f"{proxy_ip}:{proxy_port}")
        print("[+] Proxy set successfully!")
    except Exception as e:
        print(f"[-] Failed to set proxy: {e}")

def install_mitmproxy_cert():
    """ Download and install mitmproxy CA certificate """
    try:
        cert_url = "http://mitm.it/cert/pem"
        cert_path = os.path.expandvars(r"%USERPROFILE%\Downloads\mitmproxy-ca-cert.pem")

        subprocess.run(["powershell", "-Command", f"Invoke-WebRequest -Uri {cert_url} -OutFile {cert_path}"], check=True)
        subprocess.run(["certutil", "-addstore", "Root", cert_path], check=True)
        print("[+] mitmproxy certificate installed successfully!")
    except Exception as e:
        print(f"[-] Failed to install mitmproxy certificate: {e}")

def setup_mitmproxy():
    set_windows_proxy()
    install_mitmproxy_cert()

if __name__ == "__main__":
    setup_mitmproxy()
