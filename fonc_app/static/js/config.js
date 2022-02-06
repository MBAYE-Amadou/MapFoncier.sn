///// Carte de base ( OpenStreetMaps )
var OpenStreetMap = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
var WorldImagery = L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}');
var Humanitarian =L.tileLayer('http://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png');
var HikeBike =L.tileLayer('https://tiles.wmflabs.org/hikebike/{z}/{x}/{y}.png');

///// Configuration de la carte
var map = L.map('map', {
	layers: [OpenStreetMap], /// fond de base
	center: [16.47905, -15.98837],	/// coordonnées de la zone (Ronkh)
	zoom: 14	//// zoom par defaut
});


///// couches / layers de base
var baseLayers = {
	"Plan": OpenStreetMap,
	"Satellite": WorldImagery,
	"Humanitaire":Humanitarian,
	"Randonnée":HikeBike,
	
};

//	http://localhost:8080/geoserver/Projet_SIG/wms
var nomProjet = "Projet_SIG";
var lienWms = "http://localhost:8080/geoserver/" + nomProjet + "/wms";
var nomCouche1 = nomProjet + " ";
var nomCouche2 = nomProjet + " ";
var nomCouche3 = nomProjet + " ";
var nomCouche4 = nomProjet + " ";
var nomCouche5 = nomProjet + " ";


///// layers à partir de Geoserver (format WMS)
var layer1 = L.tileLayer.wms(lienWms, {
	layers: nomCouche1,
	format: 'image/png',
	transparent: true,
	version: '1.1.0',
	attribution: nomCouche1
});
var layer2 = L.tileLayer.wms(lienWms, {
	layers: nomCouche2,
	format: 'image/png',
	transparent: true,
	version: '1.1.0',
	attribution: nomCouche2
});
var layer3 = L.tileLayer.wms(lienWms, {
	layers: nomCouche3,
	format: 'image/png',
	transparent: true,
	version: '1.1.0',
	attribution: nomCouche3
});
var layer4 = L.tileLayer.wms(lienWms, {
	layers: nomCouche4,
	format: 'image/png',
	transparent: true,
	version: '1.1.0',
	attribution: nomCouche4
});
var layer5 = L.tileLayer.wms(lienWms, {
	layers: nomCouche5,
	format: 'image/png',
	transparent: true,
	version: '1.1.0',
	attribution: nomCouche5
});
  
///// Groupe layers
var overlays = {
	//	"nomCouche" : objetCouche,
	"Couche 1": layer1,
	"Couche 2": layer2,
	//"Occupation_de_Sol (polygones)": layer3,
	//"Localites_GT (points)": layer4,
	//"STATIONS (points)": layer5
};

//// Add the Find to the map
var osmGeocoder = new L.Control.OSMGeocoder();
map.addControl(osmGeocoder);
		
///// Add the Overview to the map 
var osm2 = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
var miniMap = new L.Control.MiniMap(osm2, { toggleDisplay: true }).addTo(map);

///// Add the scale control to the map
L.control.scale().addTo(map);
	
///// Add the Navigation Bar to the map ( home, right, left )
L.control.navbar({position: 'topleft'}).addTo(map);
	
///// Add the geolocate control to the map ( geolocation marker )
L.control.locate().addTo(map);

///// Add the mouse position to the map 
L.control.mousePosition().addTo(map);


///// Ajout des couches de base + couches geoserver
L.control.layers(baseLayers, overlays).addTo(map);


// displays a note to the user
function displayInfo(str, timeOutValue = -1) {
	toastr.info(
		str,
		"Info :",
		{
			timeOut: timeOutValue,
			extendedTimeOut: timeOutValue
		}
	);
}