import json
import webbrowser
import time



openmenu = input("MENU\nCHECK BY NUMBER - n\nSEARCH FULL STREETS - s\nFORMAT NEW FILE - f\nRESET FILE CHECKS TO FALSE - r\n")

with open('config.json') as confile:
   config = json.load(confile)

def osmformat(raw, name):
  rawstreets = []
  with open(raw) as f:
    d = json.load(f)
  for i in d["elements"]:
    name = i["tags"].get("name", None)
    zip = i["tags"].get("tiger:zip_left", None)
    checked = False
    strtdict = {
      "name": name,
      "zip": zip,
      "checked": checked
    }
    rawstreets.append(strtdict)
  return rawstreets

def remnull(streets):
  cleaned_data = [item for item in streets if item.get("name") is not None]
  return cleaned_data

def nodupes(streets):
  seen_names = set()
  filtered_list = []
  for i in d:
    name = i.get("name")  # Get the value of 'name'
    if name not in seen_names:
      filtered_list.append(i)
      seen_names.add(name)
  return filtered_list

if openmenu == "f":
  input("Press enter to confirm new formatting. Make sure you've edited config.json, if you haven't the current area's data will be wiped")
  strts = nodupes(remnull(osmformat(config["area-name"], config["area-raw-file"])))

# manual street check
if openmenu == "s":
  with open(config["area-name"]+".json") as f:
    d = json.load(f)

  for i in d:
    if i["checked"] == True:
      continue
    webbrowser.open("https://www.google.com/maps/search/"+i["name"]+" "+i['zip'])
    e = input()
    if e == "exit":
      break
    elif e == "how":
      count = sum(1 for d in d if d.get('checked') == True)
      print(f"{str(count)} roads checked. {str(len(d)-count)} to go")
      time.sleep(1)
    print(i['name'], "checked. ")
    i['checked'] = True

  with open(config["area-name"]+'.json', 'w') as q:
    json.dump(d, q)

# search by number
elif openmenu == "n":
  with open(config["area-name"]+'.json') as f:
    d = json.load(f)
    for i in d:
      if i['checked'] == True:
        continue
      webbrowser.open("https://www.google.com/maps/search/"+config["house-number"]+" "+i['name']+' '+config["area-name"]+" "+i['zip'])
      e = input()
      if e =="exit":
        break
      elif e == "how":
        count = sum(1 for d in d if d.get('checked') == True)
        print(f"{str(count)} houses checked, {str(len(d)-count)} to go")
        time.sleep(1.5)
      print(f"{i['name']} checked.")
      i['checked'] = True

  with open(config["area-name"]+'.json', 'w') as q:
   json.dump(d, q)

elif openmenu == "l":
  with open(config['area-name']+'.json') as f:
    d = json.load(f)
  for i in d:
    i['checked'] = False
  with open(config['area-name']+'.json', 'w') as q:
     json.dump(d, q)

elif openmenu == "c":
  with open('montclair.json') as f:
    d = json.load(f)
  print(len(d))
  with open('montclair.json', 'w') as q:
     json.dump(d, q)

elif openmenu == "d":
  with open('montclair.json') as f:
    d = json.load(f)
  seen_names = set()
  filtered_list = []
  for i in d:
    name = i.get("name")  # Get the value of 'name'
    if name not in seen_names:
      filtered_list.append(i)
      seen_names.add(name)
  with open('montclair.json', 'w') as q:
     json.dump(filtered_list, q)
