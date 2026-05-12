import subprocess

target = input("Enter target IP or subnet: ")

print(f"\nScanning {target}...\n")

result = subprocess.run(
    ["nmap", "-sV", target],
    capture_output=True,
    text=True
)

print(result.stdout)
