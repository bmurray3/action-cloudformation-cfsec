import os
import sys
import subprocess

def write_file(content):
  file_name = "cfsec.log"
  with open(file_name, "w") as file:
    print(f"writing cfsec log to {file_name} ...")
    file.write(content)

try:
  output = subprocess.run(
    [f"cfsec --no-color ."],
    check=True,
    capture_output=True,
    text=False,
    shell=True
  )
  print(output.stdout.decode("utf8"))
  write_file(output.stdout.decode("utf8"))
except subprocess.CalledProcessError as error:
  print(error.stdout.decode("utf8"))
  print(error.stderr.decode("utf8"))
  write_file(error.stdout.decode("utf8"))
  sys.exit(error.returncode)