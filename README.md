# found the tv glow
python code to find locations from films. a bit strenuous but very effective with some effort.  

## getting started  
1. download the code and unzip into an empty folder.
2. go to [overpass turbo](https://overpass-turbo.eu) and run the following code, replacing "Your Area" with the specific area to search
```
[out:json][timeout:25];
{{geocodeArea:Your Area}};
nwr["highway"="residential"](area,{{bbox}});
out geom;
```
3. export the file in the top right corner as a geojson file. download it into the same folder as the code.
4. open `config.json`. set the area-name property to your area's name, and area-raw-file to your geojson file name, with extension. if you know the house number you're looking for, add that too
5. run `main.py`. at the menu, press f. this formats your geojson into a lightweight, simpler file.
6. run it again and you're all set! you can check by number if you know what street number you're on or you can just brute force the full street.
7. once you finish searching each place, close the google maps window hit enter on the terminal to go to the next place. if you want to know how far you are, type 'how' and then press enter.
8. once you're done, to leave while saving your progress, type 'exit' and press enter.
