var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );

var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

//if i change the size of the browser, the program changes so.
window.addEventListener( 'resize', function(){
	var height = window.innerHeight;
	var width  = window.innerWidth;
	renderer.setSize( width, height);
	camera.aspect = width / height;
	camera.updateProjectionMatrix( );

} );

//contolling

controls = new THREE.OrbitControls( camera, renderer.domElement );
controls.enableZoom = false;

var geometry = new THREE.BoxGeometry( 1, 1, 1 );
var material = new THREE.MeshBasicMaterial( { color: 0x00ff00, wireframe: true } );
var cube = new THREE.Mesh( geometry, material );
scene.add( cube );
camera.position.z = 5;
var animate = function () {
	requestAnimationFrame( animate );
	cube.rotation.x += 0.01;
	cube.rotation.y += 0.01;
	renderer.render(scene, camera);
};
animate();