//Declare three.js variables
var camera, scene, renderer, stars=[];

window.addEventListener('load', init, false);

//assign three.js objects to each variable
function init(){

    //camera
    camera = new THREE.PerspectiveCamera(20, window.innerWidth / window.innerHeight, 1, 1000);
    camera.position.z = 5;

    //scene
    scene = new THREE.Scene();

    //renderer
    renderer = new THREE.WebGLRenderer({alpha: true});
    //set the size of the renderer
    renderer.setSize( window.innerWidth, window.innerHeight );

    //add the renderer to the html document body
    var container = document.getElementById('world');
    container.appendChild(renderer.domElement);

    addSphere();
    //addCube();
    addLights();
    render();

}


function addSphere(){

    // The loop will move from z position of -1000 to z position 1000, adding a random particle at each position.
    for ( var z= -1000; z < 1000; z+=1 ) {

        // Make a sphere (exactly the same as before).
        var geometry   = new THREE.TetrahedronGeometry(0.5, 0);
        var material = new THREE.MeshBasicMaterial( {color: 0xffffff} );
        var sphere = new THREE.Mesh(geometry, material)

        // This time we give the sphere random x and y positions between -500 and 500
        sphere.position.x = Math.random() * 1000 - 500;
        sphere.position.y = Math.random() * 1000 - 500;

        // Then set the z position to where it is in the loop (distance of camera)
        sphere.position.z = z;

        // scale it up a bit
        //sphere.scale.x = sphere.scale.y = 2;

        //add the sphere to the scene
        scene.add( sphere );

        //finally push it to the stars array
        stars.push(sphere);
    }
}

/*function addCube() {
    var geometry = new THREE.CubeGeometry(5, 5, 5);
    var material = new THREE.MeshLambertMaterial( {color: 0xFF0000});
    var cube = new THREE.Mesh(geometry, material);

    cube.position.x = 0;
    cube.position.y = -5;
    cube.position.z = -100;

    cube.rotation.z = 2;
    cube.rotation.x = 2;

    scene.add(cube);


}*/

var shadowLight;
function addLights() {
    shadowLight = new THREE.DirectionalLight(0xffffff, .9);
    shadowLight.position.set(5, 0, 60);
    shadowLight.castShadow = false;

    scene.add(shadowLight);

}

function animateStars() {

    // loop through each star
    for(var i=0; i<stars.length; i++) {

        star = stars[i];

        // and move it forward dependent on the mouseY position.
        star.position.z +=  i/200;

        // if the particle is too close move it to the back
        if(star.position.z>1000) star.position.z-=2000;

    }

}

function render() {
    //get the frame
    requestAnimationFrame( render );

    //render the scene
    renderer.render( scene, camera );
    animateStars();

}
