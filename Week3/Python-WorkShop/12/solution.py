def main(logfile_path):
  codes = dict()
  with open(logfile_path, "r") as file:
    for line in file:
      code = line.split(" ")[8]
      if code in codes.keys():
        codes[code] = str(int(codes[code]) + 1)
      else:
        codes.update({str(code): "1"})
  return sorted( ((int(k),int(v)) for k, v in codes.items()), reverse=False)