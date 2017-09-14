//munt orugglega bera mestu athyglinni herna. 
//er med gnu svg sem eg breytti ur png.
//er med slider sem stjornar staerdinni 
//todo: rotating slider

console.log('wokrs'); // gleymi alltaf hvernig madur includar js.

(setInterval(function update() {
	let range  = 0;
	let slider = document.getElementById('slider');
	range = slider.value;
	console.log(range);


	let svg = document.getElementById('gnu');

	let tempsize = (11 * range) + 100; // 12px to 1200
	if(!svg.length) { 
		svg.setAttribute("height", tempsize);
		svg.setAttribute("width",  tempsize);
	}
},100));