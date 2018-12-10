if ( WEBGL.isWebGLAvailable() === false ) {

				document.body.appendChild( WEBGL.getWebGLErrorMessage() );

			}

			var container, stats, controls;
			var camera, scene, renderer, light;
            var cameraControls;

			var clock = new THREE.Clock();

            var camera_height = 150;


            var WIDTH = 640;
	        var HEIGHT = 360;

			var mixers = [];

            //character state
            //1 - forward rot
            //2 - right
            //3 - back
            //4 - left
            var state = 1;

            //user state
            //1 - creating algorithm
            //2 - running algorithm
            var user_state = 1;

            var load_count = 0;

			init();
			animate();
            load_elem("Running")


			function init() {


	           var c = document.getElementById("gameCanvas");


				container = document.createElement( 'div' );
				document.body.appendChild( container );

				camera = new THREE.PerspectiveCamera( 45, window.innerWidth / window.innerHeight, 1, 2000 );
				camera.position.set( 0, 1500, 0 );

				controls = new THREE.OrbitControls( camera );
				controls.target.set( 0, 100, 0 );
				controls.update();

				scene = new THREE.Scene();
				scene.background = new THREE.Color( 0x434343);


				light = new THREE.HemisphereLight( 0xffffff, 0x444444 );
				light.position.set( 0, 200, 0 );
				scene.add( light );

				light = new THREE.DirectionalLight( 0xffffff );
				light.position.set( 0, 200, 100 );
				light.castShadow = true;
				light.shadow.camera.top = 180;
				light.shadow.camera.bottom = - 100;
				light.shadow.camera.left = - 120;
				light.shadow.camera.right = 120;
				scene.add( light );

				// scene.add( new THREE.CameraHelper( light.shadow.camera ) );

				// ground
                var textureLoader = new THREE.TextureLoader();
                var map = textureLoader.load('../models/grasslight-big.jpg');
                var map2 = textureLoader.load('../models/grasslight-big-nm.jpg');
                var material = new THREE.MeshPhongMaterial({map: map, normalMap: map2});
				var mesh = new THREE.Mesh( new THREE.PlaneBufferGeometry( 1000, 1000 ),
                                          material  );
				mesh.rotation.x = - Math.PI / 2;
				mesh.receiveShadow = true;
                mesh.position.y-=1
                mesh.name = "Ground"

				scene.add( mesh );





                create_road('../models/finish_line.jpg', 0, 450);

                create_road('../models/ground.jpeg', 0, 350);
                create_road('../models/ground.jpeg', 0, 250);
                create_road('../models/ground.jpeg', 0, 150);
                create_road('../models/ground.jpeg', 200, 150);
                create_road('../models/ground.jpeg', 200, 250);
                create_road('../models/ground.jpeg', 200, 50);
                create_road('../models/ground.jpeg', 200, -50);
                create_road('../models/ground.jpeg', 200, -150);
                create_road('../models/ground.jpeg', 200, -250);
                create_road('../models/ground.jpeg', 100, -250);
                create_road('../models/ground.jpeg', 0, -250);
                create_road('../models/ground.jpeg', -100, -250);
                create_road('../models/ground.jpeg', -200, -250);
                create_road('../models/ground.jpeg', -200, -350);
                create_road('../models/ground.jpeg', 0, -150);
                create_road('../models/ground.jpeg', -100, -150);
                create_road('../models/ground.jpeg', -200, -150);

                create_road('../models/finish_line.jpg', -200, -450);

				var grid = new THREE.GridHelper( 2000, 40, 0xffffff, 0xffffff );
				grid.material.opacity = 0.3;
                grid.position.y+=1;
				grid.material.transparent = true;
                grid.name = "grid";
				scene.add( grid );







				renderer = new THREE.WebGLRenderer( { antialias: true, stencil: false } );
                renderer.setSize(WIDTH, HEIGHT);



				renderer.setPixelRatio( window.devicePixelRatio );
				renderer.shadowMap.enabled = true;
                c.appendChild(renderer.domElement);


				window.addEventListener( 'resize', onWindowResize, false );

				// stats
				stats = new Stats();
				container.appendChild( stats.dom );

			}





            function create_road(path_to_file, position_x, position_z){
                var textureLoader = new THREE.TextureLoader();
                var map = textureLoader.load(path_to_file);

                var material = new THREE.MeshPhongMaterial({map: map});
				var mesh = new THREE.Mesh( new THREE.PlaneBufferGeometry( 200, 100 ),
                                          material  );
				mesh.rotation.x = - Math.PI / 2;
				mesh.receiveShadow = true;
                mesh.position.x+=position_x
                mesh.position.z+=position_z



				scene.add( mesh );
            }






            function removeEntity(name) {
                var selectedObject = scene.getObjectByName(name);
                scene.remove( selectedObject );
                animate();
            }




            function checkEntity(name) {
                var selectedObject = scene.getObjectByName(name);
                return selectedObject;
            }




            function addEntity(name) {
                var selectedObject = scene.getObjectByName(name);
                scene.add( selectedObject );
                animate();
            }


            function move_to_start (name){
                var boy = scene.getObjectByName(name);
                boy.updateMatrix();
                boy.position.set(0, 0, 450);

                switch (state ){
                    case 1:
                        break;
                    case 2:
                        rotateObject(boy, 0, 90, 0);
                        break;
                    case 3:
                        rotateObject(boy, 0, 180, 0);
                        break;
                    case 4:
                        rotateObject(boy, 0, -90, 0);
                        break;
                }
                if (vr == 1){
                    change_camera ()
                }
                state = 1;



            }



            function load_elem(name, position){

                var loader = new THREE.FBXLoader();
                road_tofile = '../models/'+ name + '.fbx';
				loader.load(road_tofile , function ( object ) {

					object.mixer = new THREE.AnimationMixer( object );
					mixers.push( object.mixer );

					var action = object.mixer.clipAction( object.animations[ 0 ] );
					action.play();

					object.traverse( function ( child ) {

						if ( child.isMesh ) {

							child.castShadow = true;
							child.receiveShadow = true;

						}

					} );
                    object.name = name;
                    object.position.z+=450
                    rotateObject(object, 0, 180, 0);
                    scene.add( object );

				} );

            }



            function rotateObject(object, degreeX, degreeY, degreeZ) {
                    object.rotateX(THREE.Math.degToRad(degreeX));
                    object.rotateY(THREE.Math.degToRad(degreeY));
                    object.rotateZ(THREE.Math.degToRad(degreeZ));

                }




			function onWindowResize() {
				camera.aspect = window.innerWidth / window.innerHeight;
				camera.updateProjectionMatrix();

				renderer.setSize( window.innerWidth, window.innerHeight );

			}


            function animate() {

				requestAnimationFrame( animate );



				if ( mixers.length > 0 ) {

					for ( var i = 0; i < mixers.length; i ++ ) {

						mixers[ i ].update( clock.getDelta() );

					}

				}


				renderer.render( scene, camera );


				stats.update();

			}


            function move_algorithm(){
                cons = document.getElementById("console");
                path_alg = cons.innerHTML

                for ( var i = 0; i < path_alg.length; i++ ){
                    switch (path_alg[i]){

                        case '1':
                            move_elem_forward("Running");
                            break;
                        case '2':
                            var boy = scene.getObjectByName("Running");
                            rotateObject(boy, 0, -90, 0);
                            break;
                        case 3:
                            move_elem_back("Running");
                            break;
                        case 4:
                            var boy = scene.getObjectByName("Running");
                            rotateObject(boy, 0, -90, 0);
                            break;

                    }
                }
            }








            function check_lines (x, z){
                if ( (300<z && z<500 && -100<x && x<100) ||
                    (100<z && z<=300 && -100<x && x<300) ||
                    (-100<z && z<=100 && 100<x && x<300) ||
                    (-300<z && z<=-100 && -300<x && x<300) ||
                    (-500<z && z<=-300 && -300<x && x<-100)){
                    return 1;
                }
                else{
                    if (z<=-500 && -300<x && x<-100){
                        return 2;
                    }

                else{
                    return 3;
                }
                }

            }


            function move_elem_forward(name, length = 10){


                var selectedObject = scene.getObjectByName(name);
                selectedObject.updateMatrix();

                var z = selectedObject.position.z
                var x = selectedObject.position.x
                current_position = check_lines (x, z)
                switch(current_position){
                    case 1:
                        switch (state) {
                        case 1:
                        selectedObject.position.z-=length;

                        break;
                        case 2:
                        selectedObject.position.x+=length;

                        break;
                        case 3:
                        selectedObject.position.z+=length;

                        break;
                        case 4:
                        selectedObject.position.x-=length;

                        break;
                        default:
                        alert( 'state error' + a);

                        }
                        break;
                    case 2:
                        background_music.pause()
                        foot_sound.pause();
                        foot_sound.currentTime = 0;
                        winner_sound.play()
                         show_winner()
                        break;
                    case 3:
                        background_music.pause()
                        foot_sound.pause();
                        foot_sound.currentTime = 0;
                        looser_sound.play()
                        show_looser()
                        break;
                }

            }

            function move_elem_back(name, length = 10){

                var selectedObject = scene.getObjectByName(name);
                selectedObject.updateMatrix();

                var z = selectedObject.position.z
                var x = selectedObject.position.x
                current_position = check_lines (x, z)
                switch(current_position){
                    case 1:
                        switch (state) {
                        case 1:
                        selectedObject.position.z+=length;

                        break;
                        case 2:
                        selectedObject.position.x-=length;

                        break;
                        case 3:
                        selectedObject.position.z-=length;

                        break;
                        case 4:
                        selectedObject.position.x+=length;

                        break;
                        default:
                        alert( 'state error' + a);
                    }


                        break;
                    case 2:
                        background_music.pause()
                        foot_sound.pause();
                        foot_sound.currentTime = 0;
                        winner_sound.play()
                        show_winner()
                        break;
                    case 3:
                        background_music.pause()
                        foot_sound.pause();
                        foot_sound.currentTime = 0;
                        looser_sound.play()
                        show_looser()
                        break;
                }

            }


            function anim () {

	// snip
	       const delta = clock.getDelta();
	       const isControlsUpdated = cameraControls.update( delta );

	       requestAnimationFrame( anim );

	       if ( isControlsUpdated ) {

		      renderer.render( scene, camera );

	}
}




            function change_camera (){
                var object = scene.getObjectByName("Running");
                camera.position.copy( object.position );
                camera.rotation.copy( object.rotation );
                camera.updateMatrix();
                camera.translateZ( -300 );
                camera.translateY( 150 );
                rotateObject(camera, 0, 180, 0);
            }


            function run (){
                camera.position.set( 0, camera_height, 800 );
                var selectedObject = scene.getObjectByName("grid");
                scene.remove( selectedObject );
				controls = new THREE.OrbitControls( camera );
				controls.target.set( 0, 150, 0 );
				controls.update();
                scene.fog = new THREE.Fog( 0x434343, 200, 2000 );
                window.setTimeout(move_algorithm,1000);
            }