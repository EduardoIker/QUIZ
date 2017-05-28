# coding=utf-8
#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

MAIN_PAGE_HTML= """\
<!DOCTYPE html>
<html lang="es">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="description" content="HADS">
	<meta name="author" content="Iker y Eduardo">
	<title> QUIZ </title>
	<link href="css/bootstrap.min.css" rel="stylesheet">
	<link href="css/animate.min.css" rel="stylesheet"> 
	<link href="css/font-awesome.min.css" rel="stylesheet">
	<link href="css/lightbox.css" rel="stylesheet">
	<link href="css/main.css" rel="stylesheet">
	<link id="css-preset" href="css/presets/preset1.css" rel="stylesheet">
	<link href="css/responsive.css" rel="stylesheet">
	<link href='http://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700' rel='stylesheet' type='text/css'>
	<link rel="shortcut icon" href="images/favicon.ico">
</head>
<body>
	<div class="preloader"> <i class="fa fa-circle-o-notch fa-spin"></i></div>

	<header id="home">
		<div id="home-slider" class="carousel slide carousel-fade" data-ride="carousel">
			<div class="carousel-inner">
				<div class="item active" style="background-image: url(images/slider/1.jpg)">
					<div class="caption">
						<h1 class="animated fadeInLeftBig">Bienvenido a <span>QUIZ</span></h1>
						<p class="animated fadeInRightBig">Juega respondiendo a las preguntas</p>
						<a data-scroll class="btn btn-start animated fadeInUpBig" href="/jugar">Jugar</a>
					</div>
				</div>
				<div class="item" style="background-image: url(images/slider/2.jpg)">
					<div class="caption">
						<h1 class="animated fadeInLeftBig">Bienvenido a <span>QUIZ</span></h1>
						<p class="animated fadeInRightBig">Registrate e inserta preguntas</p>
						<a data-scroll class="btn btn-start animated fadeInUpBig" href="/register">Comienza ahora</a>
					</div>
				</div>
				<div class="item" style="background-image: url(images/slider/3.jpg)">
					<div class="caption">
						<h1 class="animated fadeInLeftBig">Bienvenido a <span>QUIZ</span></h1>
						<p class="animated fadeInRightBig">Visualiza el ranking de jugadores</p>
						<a data-scroll class="btn btn-start animated fadeInUpBig" href="/ranking">Ranking</a>
					</div>
				</div>
			</div>
			<a class="left-control" href="#home-slider" data-slide="prev"><i class="fa fa-angle-left"></i></a>
			<a class="right-control" href="#home-slider" data-slide="next"><i class="fa fa-angle-right"></i></a>

			<a id="tohash" href="#services"><i class="fa fa-angle-down"></i></a>

		</div><!--/#home-slider-->
		<div class="main-nav">
			<div class="container">
				<div class="navbar-header">
					<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
						<span class="sr-only">Toggle navigation</span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
					</button>
					<a class="navbar-brand" href="/">
						<h1><img class="img-responsive" src="images/logo.png" alt="logo"></h1>
					</a>                    
				</div>
				<div class="collapse navbar-collapse">
					<ul class="nav navbar-nav navbar-right">                 
						<li class="scroll"><a href="#home">Home</a></li>
						<li class="scroll"><a href="#services">Servicios</a></li>                    
						<li class="scroll"><a href="#team">Grupo</a></li>
						<li class="scroll"><a href="#contact">Contacto</a></li>    
						<li class="scroll"><a href="/jugar">Jugar</a></li>  
			<li class="scroll"><a href="/ranking">Ranking</a></li>  
			<li class="scroll"><a href="/login">Login</a></li>  
			<li class="scroll"><a href="/register">Registro</a></li>  
					</ul>
				</div>
			</div>
		</div><!--/#main-nav-->
	</header><!--/#home-->
	
	<section id="services">
		<div class="container">
			<div class="heading wow fadeInUp" data-wow-duration="1000ms" data-wow-delay="300ms">
				<div class="row">
					<div class="text-center col-sm-8 col-sm-offset-2">
						<h2>Nuestros servicios</h2>
						<p> En QUIZ podrás ...</p>
					</div>
				</div> 
			</div>
			<div class="text-center our-services">
				<div class="row">
					<div class="col-sm-4 wow fadeInDown" data-wow-duration="1000ms" data-wow-delay="300ms">
						<div class="service-icon">
							<i class="fa fa-gamepad"></i>
						</div>
						<div class="service-info">
							<h3>Jugar</h3>
							<p>Responde a las preguntas que otros usuarios han introducido</p>
						</div>
					</div>
					<div class="col-sm-4 wow fadeInDown" data-wow-duration="1000ms" data-wow-delay="450ms">
						<div class="service-icon">
							<i class="fa fa-question-circle"></i>
						</div>
						<div class="service-info">
							<h3>Ampliar el juego</h3>
							<p>Registrate e introduce nuevas preguntas de los temas que desees</p>
						</div>
					</div>
					<div class="col-sm-4 wow fadeInDown" data-wow-duration="1000ms" data-wow-delay="550ms">
						<div class="service-icon">
							<i class="fa fa-trophy"></i>
						</div>
						<div class="service-info">
							<h3>Competir</h3>
							<p>Visualiza el ranking de jugadores y conviertete en el mejor</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section><!--/#services-->

	<section id="team">
		<div class="container">
			<div class="row">
				<div class="heading text-center col-sm-8 col-sm-offset-2 wow fadeInUp" data-wow-duration="1200ms" data-wow-delay="300ms">
					<h2>El Grupo</h2>
					<p>Somos dos estudiantes del grado en Ingeniería Informática, en la especialidad de Ingeniería del Software</p>
				</div>
			</div>
			<div class="team-members">
				<div class="row">
					<div class="col-sm-3">
						<div class="team-member wow flipInY" data-wow-duration="1000ms" data-wow-delay="300ms">
							<div class="member-image">
								<img class="img-responsive" src="images/team/1.jpg" alt="">
							</div>
							<div class="member-info">
								<h3>Iker Otxoa</h3>
								<h4>Estudiante</h4>
								<p>Facultad de Informatica - UPV/EHU</p>
							</div>
						</div>
					</div>
					<div class="col-sm-3">
						<div class="team-member wow flipInY" data-wow-duration="1000ms" data-wow-delay="500ms">
							<div class="member-image">
								<img class="img-responsive" src="images/team/2.jpg" alt="">
							</div>
							<div class="member-info">
								<h3>Eduardo Perez</h3>
								<h4>Estudiante</h4>
								<p>Facultad de Informatica - UPV/EHU</p>
							</div>
						</div>
					</div>
				</div>
			</div>            
		</div>
	</section><!--/#team-->

	<section id="contact">
		<div id="google-map" class="wow fadeIn" data-latitude="43.3067187" data-longitude="-2.0099619" data-wow-duration="1000ms" data-wow-delay="400ms"></div>
		<div id="contact-us" class="parallax">
			<div class="container">
				<div class="row">
					<div class="heading text-center col-sm-8 col-sm-offset-2 wow fadeInUp" data-wow-duration="1000ms" data-wow-delay="300ms">
						<h2>Contacto</h2>
						<p>Facultad de Informática de San Sebastián</p>
					</div>
				</div>
				<div class="contact-form wow fadeIn" data-wow-duration="1000ms" data-wow-delay="600ms">
					<div class="row">
						<div class="col-sm-6">
							<form id="main-contact-form" name="contact-form" method="post" action="sendemail.php">
								<div class="row  wow fadeInUp" data-wow-duration="1000ms" data-wow-delay="300ms">
									<div class="col-sm-6">
										<div class="form-group">
											<input type="text" name="name" class="form-control" placeholder="Nombre" required="required">
										</div>
									</div>
									<div class="col-sm-6">
										<div class="form-group">
											<input type="email" name="email" class="form-control" placeholder="Dirección de Correo" required="required">
										</div>
									</div>
								</div>
								<div class="form-group">
									<input type="text" name="subject" class="form-control" placeholder="Asunto..." required="required">
								</div>
								<div class="form-group">
									<textarea name="message" id="message" class="form-control" rows="4" placeholder="Introduce tu mensaje" required="required"></textarea>
								</div>                        
								<div class="form-group">
									<input type="submit" value="Enviar" class="btn-submit" />
								</div>
							</form>   
						</div>
						<div class="col-sm-6">
							<div class="contact-info wow fadeInUp" data-wow-duration="1000ms" data-wow-delay="300ms">
								<p> Puedes ponerte en contacto con nosotros a través de los siguientes medios:</p>
								<ul class="address">
									<li><i class="fa fa-map-marker"></i> <span> Dirección:</span> Manuel Lardizabal Ibilbidea, 1, 20018 Donostia, Gipuzkoa</li>
									<li><i class="fa fa-phone"></i> <span> Telefono:</span> 943 12 34 56  </li>
									<li><i class="fa fa-envelope"></i> <span> Email:</span> eduardoikerhads@gmail.com</li>
									<li><i class="fa fa-globe"></i> <span> Sitio web (QUIZ):</span> <a href="http://www.eisw.hol.es">www.eisw.hol.es</a></li>
								</ul>
							</div>                            
						</div>
					</div>
				</div>
			</div>
		</div>        
	</section><!--/#contact-->
	
	<footer id="footer">
		<div class="footer-top wow fadeInUp" data-wow-duration="1000ms" data-wow-delay="300ms">
			<div class="container text-center">
				<div class="footer-logo">
					<a href="/"><img class="img-responsive" src="images/logo.png" alt=""></a>
				</div>
			</div>
		</div>
		<div class="footer-bottom">
			<div class="container">
				<div class="row">
					<div class="col-sm-6">
						<p>&copy; Iker y Eduardo</p>
					</div>
					<div class="col-sm-6">
						<p class="pull-right"> HADS </p>
					</div>
				</div>
			</div>
		</div>
	</footer>

	<script type="text/javascript" src="js/jquery.js"></script>
	<script type="text/javascript" src="js/bootstrap.min.js"></script>
	<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=true"></script>
	<script type="text/javascript" src="js/jquery.inview.min.js"></script>
	<script type="text/javascript" src="js/wow.min.js"></script>
	<script type="text/javascript" src="js/mousescroll.js"></script>
	<script type="text/javascript" src="js/smoothscroll.js"></script>
	<script type="text/javascript" src="js/jquery.countTo.js"></script>
	<script type="text/javascript" src="js/lightbox.min.js"></script>
	<script type="text/javascript" src="js/main.js"></script>

</body>
</html>
"""

REGISTER_PAGE_HTML= """\
<!DOCTYPE html>
<html>
	 <body>
			<head>
				 <meta charset="utf-8">
				 <link href="/stylesheets/estilo_registro.css" rel="stylesheet" />
				 <title>Registro</title>
		 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
		 <script>
							 function archivo(evt) {
									 var files = evt.target.files; // FileList object
									 // Obtenemos la imagen del campo "file".
									 for (var i = 0, f; f = files[i]; i++) {
										 //Solo admitimos imagenes.
										 if (!f.type.match('image.*')) {
												 continue;
										 }
							 
										 var reader = new FileReader();
							 
										 reader.onload = (function(theFile) {
												 return function(e) {
													 // Insertamos la imagen
													document.getElementById("list").innerHTML = ['<img class="thumb" src="', e.target.result,'" title="', escape(theFile.name), '"/>'].join('');
												 };
										 })(f);
							 
										 reader.readAsDataURL(f);
									 }
							 }
							 
							 document.getElementById('files').addEventListener('change', archivo, false);
				 
				 function passwordIguales(){
					var pass1=document.getElementById("pass1").value;
					var pass2=document.getElementById("pass2").value;
					if(pass1!=pass2){
						alert("Las contrasenas introducidas deben de coincidir");
						return false;
					}
					return true;
				 }
				 
				 function validarCorreo(email){
					$("#erroremail").html('Procesando...');
					$.ajax("/comprobar",{
						"type": "post",
						"data":{"email":email},
						"success": function(result) {
							$("#erroremail").html(result);
							if(result=="Este correo ya esta registrado"){
							$(':input[type="submit"]').hide();}else{$(':input[type="submit"]').show();}},
							"error": function(result){ console.error("Se ha producido un error:", result);}, "async": true })}
				 
						</script>
			</head>
			<body>
		<!-- Barra navegacion superior-->
		<ul class="top">
			<li><img src="/images/logo.png" alt="Logo de la aplicacion Quiz" height="80" width="150"/></li>
			<li><a href="/">Inicio</a></li>
		</ul>
		
		<!-- Formulario de registro -->
				 <form action="/register" method="post" onSubmit="return passwordIguales();" oninput="range_control_value.value = range_control.valueAsNumber" enctype="multipart/form-data">
						<p>
						<h2>Registro en Quiz </h2>
						<br />
						Nombre y Apellidos(*): <input type="text" name="nombreyapellidos" value="%(nombreyapellidos)s" placeholder="p. ej. Inaki Urrutia Garcia" autofocus /> <p class="error">%(n_a_error)s</p>
						<br />
						Direccion de Correo (*): <input type="email" name="correo" onBlur="validarCorreo(this.value)" value="%(correo)s" placeholder="p. ej. inakiurrutia@correo.es" > <p name="erroremail" id="erroremail" class="error">%(c_error)s</p>
						<br />
						Password (*): <input type="password" name="password" value="%(password)s" id="pass1"   Title="La contrasena debe tener al menos 1 minuscula, 1 mayuscula, 1 digito y entre 6-8 caracteres"  /> <p class="error">%(p_error)s</p>
						<br />
						Repite Password (*): <input type="password" name="rpassword" value="%(rpassword)s" id="pass2"  Title="La contrasena debe tener al menos 1 minuscula, 1 mayuscula, 1 digito y entre 6-8 caracteres"  /> <p class="error">%(rp_error)s</p>
						<br />
						Seleccione una imagen de perfil (opcional) <br>
						<input type="file" id="files" name="fotoperfil" />
						<br />
						<output id="list"></output>
						<br />
			<script>
							function archivo(evt) {
									var files = evt.target.files; // FileList object
						 
									// Obtenemos la imagen del campo "file".
									for (var i = 0, f; f = files[i]; i++) {
										//Solo admitimos imagenes.
										if (!f.type.match('image.*')) {
												continue;
										}
						 
										var reader = new FileReader();
						 
										reader.onload = (function(theFile) {
												return function(e) {
													// Insertamos la imagen
												 document.getElementById("list").innerHTML = ['<img class="thumb" src="', e.target.result,'" title="', escape(theFile.name), '"/>'].join('');
												};
										})(f);
						 
										reader.readAsDataURL(f);
									}
							}
						 
							document.getElementById('files').addEventListener('change', archivo, false);
			</script>
						<center>
							 <input type="submit" class="button1" value="Enviar Datos" />
							 <br /><br />
						</center>
						</p>
				 </form>
	 </body>
</html>
"""

LOGIN_PAGE_HTML="""\
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<title>Login</title>
		<meta http-equiv="content-type" content="text/html;charset=UTF-8" />
		<link href="/stylesheets/estilo_login.css" rel="stylesheet" />
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
		<script src="https://apis.google.com/js/platform.js" async defer></script>
		<meta name="google-signin-client_id" content="685346234752-v1rptjskapa58cm0ro1178hc4cjc0luj.apps.googleusercontent.com">
		<script type="text/javascript">
			function validarCamposLogin(){
				var correo=document.getElementById("correo").value;
				var password=document.getElementById("password").value;
				
				if(correo==""){
					alert("Introduce un correo electronico");
					return false;
				}
				if(!(/^[0-z]+@[0-z]+\.[a-z]+$/.test(correo))){
						alert("Introduce un correo valido");
						return false;
				}
				
				if(password==""){
					alert("Introduce una contrasena");
					return false;
				}
				
				return true;
			}
			
			function onSignIn(googleUser) {
				var profile = googleUser.getBasicProfile();
				//alert('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
				//alert('Name: ' + profile.getName());
				//alert('Image URL: ' + profile.getImageUrl());
				//alert('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
				//$("gsi").click(function(){
				$.ajax("/loginGoogle",{
						"type": "post",
						"data":{"email": profile.getEmail(), "imageurl": profile.getImageUrl(), "name": profile.getName()},
						"success": function(result) {alert("Google Login correcto"); window.location.href="/perfil"},
						"error": function(result){ alert("Ha ocurrido un error. Intentalo de nuevo."); window.location.href="/"}, "async": true })
				//});
			}
			
			function signOut() {
				var auth2 = gapi.auth2.getAuthInstance();
				auth2.signOut().then(function () {
				console.log('User signed out.');
				});
				window.location.href="/"
			}
		</script>
	</head>
	<body>
		<!-- Barra navegacion superior-->
		<ul class="top">
				<li><img src="/images/logo.png" alt="Logo de la aplicacion Quiz" height="80" width="150"/></li>
				<li><a href=" /login">Login</a></li>
				<li><a href="/register">Registro</a></li>
				<li><a href="/">Inicio</a></li>
			</ul>
	
		<!-- Formulario para login-->
		<form method="post" action="/login" onsubmit="return validarCamposLogin();" >
			<div>
				<h1> Login </h1>
				<span>Correo electronico: </span>
				<input type="text" name="correo" id="correo" value="%(correo)s"/> <p class="error">%(correo_error)s</p>
				<br/>
				<span>Contrasena: </span>
				<input type="password" name="password" id="password" value="%(password)s"/> <p class="error">%(password_error)s</p>
				<br/>
				<input type="submit" name="submit" id="submit" value="Entrar" />
			</div>
			<hr/>
			<div name="gsi" id="gsi" class="g-signin2" data-onsuccess="onSignIn" data-theme="dark"  data-width="200" data-longtitle="true"></div>
		</form>
	</body>
</html>
"""

PROFILE_PAGE_HTML="""\
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8"/>
		<meta name="google-signin-client_id" content="685346234752-v1rptjskapa58cm0ro1178hc4cjc0luj.apps.googleusercontent.com">
		<title>Perfil</title>
		<link rel="stylesheet" type="text/css" href="/stylesheets/estilo_perfil.css"/>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
		<script src="https://apis.google.com/js/platform.js" async defer></script>
		<script>
			function signOut() {
				var auth2 = gapi.auth2.getAuthInstance();
				auth2.signOut().then(function () {
				console.log('User signed out.');
				});
				window.location.href="/"
			}
			
			 function onLoad() {
				gapi.load('auth2', function() {
				gapi.auth2.init();
				});
			}
			
			function mostrarModificarContrasena(){
				document.getElementById("cambioContraForm").style="display:inline";
				document.getElementById("botonMostrarModificarContrasena").style="display:none";
			}
			
			function modificarContrasena(){
				var passActual = document.getElementById("passActual").value;
				var passNuevo = document.getElementById("passNuevo").value; 
				var rPassNuevo = document.getElementById("rPassNuevo").value; 
					//Comprobaciones
					if(passActual.length==0 || passNuevo.length==0 || rPassNuevo==0){
						 alert("Por favor, completa todos los campos");
						 return false;
					}
					if(!(/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,8}$/.test(passNuevo))){
						 alert("El password debe tener al menos 1 minuscula, 1 mayuscula, 1 digito y entre 6-8 caracteres");
						 return false;
					}
					
					if(passNuevo!=rPassNuevo){
						alert("Los password deben de coincidir");
						 return false;
					}
				// AJAX                                                
				 $.ajax("/cambioPassword",{
						"type": "post",
						"data":{"passact": passActual, "passnuev": passNuevo, "rpassnuev": rPassNuevo},
						"success": function(result) {alert(result); window.location.href="/perfil"},
						"error": function(result){ alert("Ha ocurrido un error. Intentalo de nuevo.");}, "async": true })
			}
		</script>
	</head>
	<body onload="onLoad()"> 
			<!-- Barra navegacion superior-->
		<ul class="top">
			<li><img src="/images/logo.png" alt="Logo de la aplicacion Quiz" height="80" width="150"/></li>
			<li><a class="logout" href="/logout" onclick="signOut();">Logout</a></li>
			<li><a href="/misPreguntas">Mis preguntas</a></li>
			<li><a href="/preguntas">Ver preguntas</a></li>
			<li><a href="/anadirPregunta">Insertar pregunta</a></li>
			<li><a href="/perfil">Mi perfil</a></li>
			<li><p> Te has identificado como: %(user_email)s</p></li>
		</ul>
		<div id="perfil">
					<h1>Mi Perfil</h1>
			<img src="%(s)s"/>
			<span class="nombre">%(n)s</span>
"""

ADD_QUESTION_PAGE_HTML= """\
<!DOCTYPE html>
<html>
	 <body>
			<head>
				 <meta charset="utf-8">
		 <meta name="google-signin-client_id" content="685346234752-v1rptjskapa58cm0ro1178hc4cjc0luj.apps.googleusercontent.com">
				 <link href="/stylesheets/estilo_anadirpregunta.css" rel="stylesheet" />
				 <title>Anadir pregunta</title>
		 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
		 <script src="https://apis.google.com/js/platform.js" async defer></script>
		 <script>
				function signOut() {
					var auth2 = gapi.auth2.getAuthInstance();
					auth2.signOut().then(function () {
					console.log('User signed out.');
					});
					window.location.href="/"
				}
				
				 function onLoad() {
					gapi.load('auth2', function() {
					gapi.auth2.init();
					});
				}
							 function archivo(evt) {
									 var files = evt.target.files; // FileList object
									 // Obtenemos la imagen del campo "file".
									 for (var i = 0, f; f = files[i]; i++) {
										 //Solo admitimos imagenes.
										 if (!f.type.match('image.*')) {
												 continue;
										 }
										 var reader = new FileReader();
										 reader.onload = (function(theFile) {
												 return function(e) {
													 // Insertamos la imagen
													document.getElementById("list").innerHTML = ['<img class="thumb" src="', e.target.result,'" title="', escape(theFile.name), '"/>'].join('');
												 };
										 })(f);
										 reader.readAsDataURL(f);
									 }
							 }
							 document.getElementById('files').addEventListener('change', archivo, false);			   
						</script>
			</head>
			<body onload="onLoad()">
		<!-- Barra navegacion superior-->
		<ul class="top">
			<li><img src="/images/logo.png" alt="Logo de la aplicacion Quiz" height="80" width="150"/></li>
			<li><a class="logout" href="/logout" onclick="signOut();">Logout</a></li>
			<li><a href="/misPreguntas">Mis preguntas</a></li>
			<li><a href="/preguntas">Ver preguntas</a></li>
			<li><a href="/anadirPregunta">Insertar pregunta</a></li>
			<li><a href="/perfil">Mi perfil</a></li>
			<li><p> Te has identificado como: %(user_email)s</p></li>
		</ul>
		
		<!-- Formulario para insertar una pregunta -->
				 <form action="/anadirPregunta" method="post" oninput="range_control_value.value = range_control.valueAsNumber" enctype="multipart/form-data">
						<p>
						<h2>Insertar Pregunta </h2>
						<br />
						Pregunta (*): <input type="text" name="pregunta" value="%(pregunta)s" placeholder="Protocolo para la transferencia de hipertexto" autofocus /> <p class="error">%(pregunta_error)s</p>
						<br />
						Respuesta 1 (*): <input type="text" name="res_uno" value="%(res_uno)s" placeholder="FTP" > <p class="error">%(res_uno_error)s</p>
						<br />
			Respuesta 2 (*): <input type="text" name="res_dos" value="%(res_dos)s" placeholder="HTTP" > <p class="error">%(res_dos_error)s</p>
						<br />
			Respuesta 3 (*): <input type="text" name="res_tres" value="%(res_tres)s" placeholder="TELNET" > <p class="error">%(res_tres_error)s</p>
						<br />
			Tema (*): <input type="text" name="tema" value="%(tema)s" placeholder="Protocolos" autofocus /> <p class="error">%(tema_error)s</p>
			<br />
			Respuesta correcta (*): <select name="res_correcta"> <option value="1">Primera respuesta</option> <option value="2">Segunda respuesta</option> <option value="3">Tercera respuesta</option> </select>
			<br />
						Seleccione una imagen para la pregunta (opcional) <br>
						<input type="file" id="files" name="fotopreg" />
						<br />
						<output id="list"></output>
						<br />
			<script>
							function archivo(evt) {
									var files = evt.target.files; // FileList object
						 
									// Obtenemos la imagen del campo "file".
									for (var i = 0, f; f = files[i]; i++) {
										//Solo admitimos imagenes.
										if (!f.type.match('image.*')) {
												continue;
										}
						 
										var reader = new FileReader();
						 
										reader.onload = (function(theFile) {
												return function(e) {
													// Insertamos la imagen
												 document.getElementById("list").innerHTML = ['<img class="thumb" src="', e.target.result,'" title="', escape(theFile.name), '"/>'].join('');
												};
										})(f);
						 
										reader.readAsDataURL(f);
									}
							}
						 
							document.getElementById('files').addEventListener('change', archivo, false);
			</script>
						<center>
							 <input type="submit" class="button1" value="Guardar Pregunta" />
							 <br /><br />
						</center>
						</p>
				 </form>
	 </body>
</html>
"""

SHOW_QUESTION_PAGE_HTML= """\
<!DOCTYPE html>
<html>
			<head>
				 <meta charset="utf-8">
		 <meta name="google-signin-client_id" content="685346234752-v1rptjskapa58cm0ro1178hc4cjc0luj.apps.googleusercontent.com">
				 <link href="/stylesheets/estilo_verpreguntas.css" rel="stylesheet" />
				 <title>Ver preguntas</title>
		 <script src="https://apis.google.com/js/platform.js" async defer></script>
		 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
		 <script>
						function obtenerPreguntas(tema){
				if(tema!="none"){
					$("#tabla_preguntas").html('Procesando...');
					$.ajax("/tablaPreguntas",{
						"type": "post",
						"data":{"tema":tema},
						"success": function(result) {
							$("#tabla_preguntas").html(result);},
						"error": function(result){ alert(result);},
						"async": true })
				}else{
					$("#tabla_preguntas").html('Selecciona un tema');
				}
			}
			
			function signOut() {
				var auth2 = gapi.auth2.getAuthInstance();
				auth2.signOut().then(function () {
				console.log('User signed out.');
				});
				window.location.href="/"
			}
			
			 function onLoad() {
				gapi.load('auth2', function() {
				gapi.auth2.init();
				});
			}
				 </script>
			</head>
			<body onload="obtenerPreguntas('none'); onLoad();">
		<!-- Barra navegacion superior-->
		<ul class="top">
			<li><img src="/images/logo.png" alt="Logo de la aplicacion Quiz" height="80" width="150"/></li>
			<li><a class="logout" href="/logout" onclick="signOut();">Logout</a></li>
			<li><a href="/misPreguntas">Mis preguntas</a></li>
			<li><a href="/preguntas">Ver preguntas</a></li>
			<li><a href="/anadirPregunta">Insertar pregunta</a></li>
			<li><a href="/perfil">Mi perfil</a></li>
			<li><p> Te has identificado como: %(user_email)s</p></li>
		</ul>
		<div id="ver_preguntas" class="preguntas">
			<h2>Ver Preguntas</h2>
			<select name="tema" id="tema" onChange="obtenerPreguntas(this.value)">
				<option value="none" selected="selected">--Selecciona un tema--</option>"""

MY_QUESTIONS_PAGE_HTML="""\
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8"/>
		<title>Temas</title>
		<link rel="stylesheet" type="text/css" href="/stylesheets/estilo_misPreguntas.css"/>
	</head>
	<body> 
			<!-- Barra navegacion superior-->
		<ul class="top">
				<li><img src="/images/logo.png" alt="Logo de la aplicacion Quiz" height="80" width="150"/></li>
				<li><a class="logout" href="/logout" onclick="signOut();">Logout</a></li>
				<li><a href="/misPreguntas">Mis preguntas</a></li>
				<li><a href="/preguntas">Ver preguntas</a></li>
				<li><a href="/anadirPregunta">Insertar pregunta</a></li>
				<li><a href="/perfil">Mi perfil</a></li>
				<li><p> Te has identificado como: %(user_email)s</p></li>
			</ul>  
	</body>
</html>
"""


ANONYMOUS_PLAY_PAGE_HTML="""\
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8"/>
		<title>Jugar</title>
		<link rel="stylesheet" type="text/css" href="/stylesheets/estilo_anonymous_play.css"/>
		<script type="text/javascript">
			function validarCampos(){
				var nick=document.getElementById("nick").value;	
				if(nick==""){
					alert("Introduce un nick");
					return false;
				}
				return true;
			}
		</script>
	</head>
	<body> 
			<!-- Barra navegacion superior-->
		<ul class="top">
				<li><img src="/images/logo.png" alt="Logo de la aplicacion Quiz" height="80" width="150"/></li>
				<li><a href=" /login">Login</a></li>
				<li><a href="/register">Registro</a></li>
				<li><a href="/ranking">Ranking</a></li>
				<li><a href="/jugar">Jugar</a></li>
				<li><a href="/">Inicio</a></li>
			</ul>
		<div id="nickDiv">
					<h1>Jugar</h1>
					<form id="nickForm" method="post" action="/jugar" onsubmit="return validarCampos();" >
				Nick: <input type="text" name="nick" id="nick" value="%(nick)s"/>  <p class="error">%(n_error)s</p><br/>
				<input type="submit" name="botonNick" id="botonNick" value="Aceptar"/>
			</form>
			</br>
				</div>		 
	</body>
</html>
"""

THEME_PAGE_HTML="""\
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8"/>
		<title>Temas</title>
		<link rel="stylesheet" type="text/css" href="/stylesheets/estilo_temas.css"/>
	</head>
	<body> 
			<!-- Barra navegacion superior-->
		<ul class="top">
				<li><img src="/images/logo.png" alt="Logo de la aplicacion Quiz" height="80" width="150"/></li>
				<li><a href=" /login">Login</a></li>
				<li><a href="/register">Registro</a></li>
				<li><a href="/ranking">Ranking</a></li>
				<li><a href="/jugar">Jugar</a></li>
				<li><a href="/">Inicio</a></li>
			</ul>	 
	</body>
</html>
"""

GAME_PAGE_HTML="""\
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8"/>
		<title>Juego</title>
		<link rel="stylesheet" type="text/css" href="/stylesheets/estilo_juego.css"/>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
		<script>

			function TodasLasPreguntasRespondidas(numPreguntas) {
						return ($('input[type=radio]:checked').length == numPreguntas);
			}

			function recuento(){
				var nick= document.getElementById("nick").value;
				var numeroPreguntas= document.getElementById("numeroPreguntas").value;
				var tema= document.getElementById("tema").value;
				var resultados=[];
				if (TodasLasPreguntasRespondidas(numeroPreguntas)){
					for (i=1; i<=numeroPreguntas;i++){
						respuestas= document.getElementsByName("pregunta"+i);
						for (j=0; j<respuestas.length;j++){
							if (respuestas[j].checked)
								resultados[i-1]=j+1;
						}
					}
					resultadosString=resultados.toString();
					resultado(nick,tema,resultadosString);
				}else{
					alert("Por favor, responda a todas las preguntas");
				}
			} 

				function resultado(nick,tema, resultados){
				$("#preguntas").html('Procesando...');
				$.ajax("/resultado",{
					"type": "post",
					"data":{"nick":nick,"tema":tema,"resultados":resultados},
					"success": function(result) {
						$("#preguntas").html(result);},
					"error": function(result){ alert(result);},
					"async": true })
			} 
	</script>
	</head>
	<body> 
			<!-- Barra navegacion superior-->
		<ul class="top">
				<li><img src="/images/logo.png" alt="Logo de la aplicacion Quiz" height="80" width="150"/></li>
				<li><a href=" /login">Login</a></li>
				<li><a href="/register">Registro</a></li>
				<li><a href="/ranking">Ranking</a></li>
				<li><a href="/jugar">Jugar</a></li>
				<li><a href="/">Inicio</a></li>
			</ul>	 
	</body>
</html>
"""

RANKING_PAGE_HTML="""\
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8"/>
		<title>Ranking</title>
		<link rel="stylesheet" type="text/css" href="/stylesheets/estilo_ranking.css"/>
	</head>
	<body> 
			<!-- Barra navegacion superior-->
		<ul class="top">
				<li><img src="/images/logo.png" alt="Logo de la aplicacion Quiz" height="80" width="150"/></li>
				<li><a href=" /login">Login</a></li>
				<li><a href="/register">Registro</a></li>
				<li><a href="/ranking">Ranking</a></li>
				<li><a href="/jugar">Jugar</a></li>
				<li><a href="/">Inicio</a></li>
			</ul>	 
	</body>
</html>
"""


import webapp2
from webapp2_extras import sessions
import re
import session_module
import urllib
from google.appengine.ext import ndb
import hashlib
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
from suds.client import Client
import cgi
from google.appengine.api import users

class MainPage(webapp2.RequestHandler):
		def get(self):
				self.response.write(MAIN_PAGE_HTML)

class User(ndb.Model):
	created = ndb.DateTimeProperty(auto_now_add=True)
	nombre = ndb.StringProperty(required=True)
	email = ndb.StringProperty(required=True)
	password = ndb.StringProperty(required=True)
	isAvatar = ndb.BooleanProperty(default=False)
	avatar = ndb.BlobProperty()

class Question(ndb.Model):
	pregunta = ndb.StringProperty(required=True)
	res_uno = ndb.StringProperty(required=True)
	res_dos= ndb.StringProperty(required=True)
	res_tres = ndb.StringProperty(required=True)
	respuesta_correcta = ndb.IntegerProperty(required=True)
	tema = ndb.StringProperty(required=True)
	user = ndb.StringProperty(required=True)
	isImagen = ndb.BooleanProperty(default=False)
	imagen = ndb.BlobProperty()

class Jugador(ndb.Model):
	nick = ndb.StringProperty(required=True)
	aciertos = ndb.IntegerProperty(required=True)
	fallos = ndb.IntegerProperty(required=True)
	
def escape_html(s):
	return cgi.escape(s, quote=True)	

USER_RE = re.compile(r"^[A-z]+([ ][A-z]+)+$")
PASSWORD_RE = re.compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,8}$")
CORREO_RE = re.compile(r"^[0-z]+@[0-z]+\.[a-z]+$")
	
class Registro(webapp2.RequestHandler):
	def write_form(self, nombreyapellidos="", password="", rpassword="", correo="", n_a_error="", c_error="", p_error="", rp_error=""):
		self.response.out.write(REGISTER_PAGE_HTML % {"nombreyapellidos":nombreyapellidos, "password":password, "rpassword":rpassword, "correo":correo, "n_a_error":n_a_error, "c_error":c_error, "p_error":p_error, "rp_error":rp_error})
	
	def get(self):
		self.write_form()
	
	def valid_name(self, user_name):
		return USER_RE.match(user_name)
	def valid_correo(self, user_correo):
		return CORREO_RE.match(user_correo)
	def valid_password(self, user_password):
		return PASSWORD_RE.match(user_password)		
	def equal_password(self, user_password, user_repeat_password):
		return (user_password == user_repeat_password)
	def exist_correo(self, user_correo): #Servicio web para comprobar si existe este correo o no
		url="http://ws.cdyne.com/emailverify/Emailvernotestemail.asmx?WSDL"
		client=Client(url)
		respuesta=client.service.VerifyEmail(user_correo,0)
		valido=respuesta.GoodEmail
		return valido
	
	def post(self):
		user_name= escape_html(self.request.get('nombreyapellidos'))
		user_password= escape_html(self.request.get('password'))
		user_repeat_password= escape_html(self.request.get('rpassword'))
		user_correo= escape_html(self.request.get('correo'))
		n_a_error= ""
		c_error= ""
		p_error= ""
		rp_error= ""
		error= False
		if not self.valid_name(user_name):
			n_a_error= "Introduce al menos un nombre y un apellido"
			error= True
		if not self.valid_correo(user_correo): #Comprobar que el correo es sintacticamente correcto
			c_error= "Introduce un correo valido"
			error= True
		elif not self.exist_correo(user_correo): #Si es sintacticamente correcto, comprobar si existe un correo con ese nombre
			c_error="El correo introducido no existe"
			error= True
		if not self.valid_password(user_password):
			p_error= "La contrasena debe tener al menos 1 minuscula, 1 mayuscula, 1 digito y entre 6 y 8 caracteres"
			error= True
		if not self.equal_password(user_password, user_repeat_password):
			rp_error="Las contrasenas deben de coincidir"
			error= True
		if error:
			self.write_form(user_name, user_password, user_repeat_password, user_correo, n_a_error, c_error, p_error, rp_error)
		else:
			u= User()
			u.nombre= user_name
			u.email= user_correo
			u.password= hashlib.md5(user_password).hexdigest()
			if len(self.request.get('fotoperfil')) != 0:
				u.isAvatar= True
				u.avatar= self.request.get('fotoperfil')
			u.put()
			self.response.out.write('<script type=text/javascript>alert("Te has registrado correctamente")</script>')
			self.write_form()

class ComprobarEmail(webapp2.RequestHandler):
	def post(self):
		user = User.query(User.email==self.request.get('email')).count()
		if user==0:
			self.response.out.write('<span style="color:green">Email no registrado</span>')
		else:
			self.response.out.write('Este correo ya esta registrado')
	
			
class Login(session_module.BaseSessionHandler):
	def write_form(self, correo="", correo_error="", password="", password_error=""):
		self.response.write(LOGIN_PAGE_HTML % {"correo": correo, "correo_error": correo_error, "password": password, "password_error": password_error})
	
	def get(self):
		self.write_form()

	def valid_correo(self, user_correo):
		return CORREO_RE.match(user_correo)
		
	def valid_password(self, user_password):
		return PASSWORD_RE.match(user_password)
	
	def post(self):
		correo = self.request.get('correo')
		password = self.request.get('password')
		sani_correo = escape_html(correo)
		sani_password = escape_html(password)
		password_error = ""
		correo_error = ""
		
		error = False
		if not self.valid_password(sani_password):
			password_error = "Introduce una contrasena valida"
			error = True
		if not self.valid_correo(sani_correo):
			correo_error = "Introduce un email valido"
			error = True
		if error:
			self.write_form(correo, correo_error, password, password_error)
		else:
			enc_password=hashlib.md5(sani_password).hexdigest()
			user = User.query(User.email == sani_correo, User.password == enc_password).get()
			if not user is None:
				self.session['correo']= sani_correo
				self.session['metodo']= 'default'
				self.session['nombre']= user.nombre
				self.response.out.write('<script type=text/javascript>alert("Login correcto")</script>')
				self.redirect('/perfil')
			else:
				self.response.out.write('<script type=text/javascript>alert("Credenciales de acceso incorrectos")</script>')
				self.write_form()
				
class LoginGoogle(session_module.BaseSessionHandler):
	def post(self):
		self.session['correo']= self.request.get('email')
		self.session['metodo']= 'google'
		self.session['imageurl']= self.request.get('imageurl')
		self.session['nombre']= self.request.get('name')
				
class Logout(session_module.BaseSessionHandler):
	def get(self):
		for sesion in self.session.keys():
			del self.session[sesion]
			self.redirect('/')
		
class Perfil(session_module.BaseSessionHandler):
	def get(self):
		try:
			self.session['correo']
		except KeyError:
			self.redirect('/')
			return
		if self.session['metodo']== 'default':
			user = User.query(User.email==self.session['correo']).get()
			if user.isAvatar:
				self.response.write(PROFILE_PAGE_HTML % {"user_email":self.session['correo'], "s": '/img?img_id='+user.key.urlsafe(), "n": self.session['nombre']})
			else:
				user = User.query(User.email=='admin@admin.es').get()
				self.response.write(PROFILE_PAGE_HTML % {"user_email":self.session['correo'], "s": '/images/avatar.jpg', "n": self.session['nombre']})
			self.response.write('<input type="button" name="botonMostrarModificarContrasena" id="botonMostrarModificarContrasena" value="Modificar Contrasena" onclick="mostrarModificarContrasena()"/>')
			self.response.write('<form id="cambioContraForm" style="display:none">')
			self.response.write('Password Actual : <input type="password" name="passActual" id="passActual" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,8}"/> <br/>')
			self.response.write('Nuevo Password: <input type="password" name="passNuevo" id="passNuevo" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,8}"/> <br/>')
			self.response.write('Repetir Password: <input type="password" name="rPassNuevo" id="rPassNuevo" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,8}"/> <br/>')
			self.response.write('<input type="button" name="botonModificarContrasena" id="botonModificarContrasena" value="Modificar Password" onclick="modificarContrasena()"/>')
			self.response.write('</form>')
		else:
			self.response.write(PROFILE_PAGE_HTML % {"user_email":self.session['correo'], "s": self.session['imageurl'], "n": self.session['nombre']})
			self.response.write('<span class="googleacount">La cuenta pertenece a Google y no se pueden realizar modificaciones</span>')
		self.response.write('</br></div></body></html>')

class Image(webapp2.RequestHandler):
		def get(self):
				user_key = ndb.Key(urlsafe=self.request.get('img_id'))
				user = user_key.get()
				if user.isAvatar:
						self.response.headers['Content-Type'] = 'image/png'
						self.response.out.write(user.avatar)
				else:
						self.response.out.write('No image')
			
class CambiarPassword(session_module.BaseSessionHandler):
	def post(self):
		user = User.query(User.email==self.session['correo']).get()
		if not user.password== hashlib.md5(self.request.get('passact')).hexdigest():
			self.response.write('La contrasena actual no coincide')
		else:
			if not self.request.get('passnuev')==self.request.get('rpassnuev'):
				self.response.out.write('Los nuevos password no coinciden')
			else:
				user.password= hashlib.md5(self.request.get('passnuev')).hexdigest()
				user.put()
				self.response.write('Password actualizado correctamente')

			
QUESTION_RE = re.compile(r"^[A-z][A-z 0-9]+$")
TEXT_RE = re.compile(r"^[A-z][A-z 0-9]+$")

class AnadirPregunta(session_module.BaseSessionHandler):
	def write_form(self, pregunta="", pregunta_error="", res_uno="", res_uno_error="", res_dos="", res_dos_error="", res_tres="", res_tres_error="", tema="", tema_error=""):
		self.response.out.write(ADD_QUESTION_PAGE_HTML % {"user_email":self.session['correo'], "pregunta":pregunta, "pregunta_error":pregunta_error, "res_uno":res_uno, "res_uno_error":res_uno_error, "res_dos":res_dos, "res_dos_error":res_dos_error, "res_tres":res_tres, "res_tres_error":res_tres_error, "tema":tema, "tema_error": tema_error})
	
	def get(self):
		try:
			self.session['correo']
		except KeyError:
			self.redirect('/')
			return
		self.write_form()
	
	def valid_question(self, question):
		return QUESTION_RE.match(question)
		
	def valid_text(self, text):
		return TEXT_RE.match(text)
	
	def post(self):
		pregunta= escape_html(self.request.get('pregunta'))
		res_uno= escape_html(self.request.get('res_uno'))
		res_dos= escape_html(self.request.get('res_dos'))
		res_tres= escape_html(self.request.get('res_tres'))
		tema= escape_html(self.request.get('tema'))
		respuesta_correcta= escape_html(self.request.get('res_correcta'))
		pregunta_error=""
		res_uno_error=""
		res_dos_error=""
		res_tres_error=""
		tema_error=""
		error= False
		if not self.valid_question(pregunta):
			pregunta_error= "Introduce una pregunta valida (sin simbolos de interrogacion)"
			error= True
		if not self.valid_text(res_uno):
			res_uno_error= "Introduce una respuesta valida"
			error= True
		if not self.valid_text(res_dos):
			res_dos_error= "Introduce una respuesta valida"
			error= True
		if not self.valid_text(res_tres):
			res_tres_error= "Introduce una respuesta valida"
			error= True
		if not self.valid_text(tema):
			tema_error= "Introduce un tema valido"
			error= True
		if error:
			self.write_form(pregunta, pregunta_error, res_uno, res_uno_error, res_dos, res_dos_error, res_tres, res_tres_error, tema, tema_error)
		else:
			q= Question()
			q.pregunta= pregunta
			q.res_uno= res_uno
			q.res_dos= res_dos
			q.res_tres= res_tres
			q.respuesta_correcta= int(respuesta_correcta)
			q.tema= tema
			q.user= self.session['correo']
			if len(self.request.get('fotopreg')) != 0:
				q.isImagen= True
				q.imagen= self.request.get('fotopreg')
			q.put()
			self.response.out.write('<script type=text/javascript>alert("La pregunta se ha registrado correctamente")</script>')
			self.write_form()	

class VerPreguntas(session_module.BaseSessionHandler):
	def get(self):
		try:
			self.session['correo']
		except KeyError:
			self.redirect('/')
			return
		self.response.out.write(SHOW_QUESTION_PAGE_HTML % {"user_email":self.session['correo']})
		preguntas = ndb.gql("SELECT DISTINCT tema FROM Question")
		for pregunta in preguntas:
			self.response.out.write('<option value="'+ pregunta.tema +'">'+ pregunta.tema +'</option>')
		self.response.out.write('</select></div><br/><div id="tabla_preguntas" class="tabla_preguntas" name="tabla_preguntas"></div></body></html>')
			
class TablaPreguntas(webapp2.RequestHandler):
	def post(self):
		preguntas = Question.query(Question.tema==self.request.get('tema'))
		self.response.out.write('<table border="1">')
		self.response.out.write('<tr><th>Imagen</th><th>Pregunta</th><th>Respuesta 1</th><th>Respuesta 2</th><th>Respuesta 3</th><th>Correcta</th><th>Autor</th></tr>')
		for pregunta in preguntas:
			#self.response.out.write('<tr><td>'+pregunta.pregunta+'</td><td>Pregunta</td><td>Respuesta 1</td><th>Respuesta 2</th><th>Respuesta 3</th><th>Correcta</th><th>Autor</th></tr>')
			if pregunta.isImagen:
				self.response.out.write('<tr><td><img src="/imgp?img_id='+pregunta.key.urlsafe()+'" width="96px" height="88px"/></td><td>'+pregunta.pregunta+'</td><td>'+pregunta.res_uno+'</td><td>'+pregunta.res_dos+'</td><td>'+pregunta.res_tres+'</td><td>'+str(pregunta.respuesta_correcta)+'</td><td>'+pregunta.user+'</td></tr>')
			else:
				self.response.out.write('<tr><td><i>Sin imagen</i></td><td>'+pregunta.pregunta+'</td><td>'+pregunta.res_uno+'</td><td>'+pregunta.res_dos+'</td><td>'+pregunta.res_tres+'</td><td>'+str(pregunta.respuesta_correcta)+'</td><td>'+pregunta.user+'</td></tr>')
		self.response.out.write('</table>')

class MisPreguntas(session_module.BaseSessionHandler):
	def get(self):
		try:
			self.session['correo']
		except KeyError:
			self.redirect('/')
			return
		self.response.out.write(MY_QUESTIONS_PAGE_HTML % {"user_email":self.session['correo']})
		preguntas = Question.query(Question.user==self.session['correo'])
		self.response.out.write('<div id="preguntas">')
		if preguntas.count()==0:
			self.response.out.write('</br>No has añadido ninguna pregunta.')
		else:
			self.response.out.write('<h2>Mis preguntas</h2>')
			self.response.out.write('<table border="1">')
			self.response.out.write('<tr><th>Imagen</th><th>Pregunta</th><th>Respuesta 1</th><th>Respuesta 2</th><th>Respuesta 3</th><th>Correcta</th><th>Eliminar</th></tr>')
			for pregunta in preguntas:
				if pregunta.isImagen:
					self.response.out.write('<tr><td><img src="/imgp?img_id='+pregunta.key.urlsafe()+'" width="96px" height="88px"/></td><td>'+pregunta.pregunta+'</td><td>'+pregunta.res_uno+'</td><td>'+pregunta.res_dos+'</td><td>'+pregunta.res_tres+'</td><td>'+str(pregunta.respuesta_correcta)+'</td><td><form method="post" action="/misPreguntas"><input type="hidden" name="preguntaId" value="'+str(pregunta.key.id())+'"/><input type="submit" class="submit" value="Eliminar pregunta" /></form></td></tr>')
				else:
					self.response.out.write('<tr><td><i>Sin imagen</i></td><td>'+pregunta.pregunta+'</td><td>'+pregunta.res_uno+'</td><td>'+pregunta.res_dos+'</td><td>'+pregunta.res_tres+'</td><td>'+str(pregunta.respuesta_correcta)+'</td><td><form method="post" action="/misPreguntas"><input type="hidden" name="preguntaId" value="'+str(pregunta.key.id())+'"/><input type="submit" class="submit" value="Eliminar pregunta" /></form></td></tr>')
			self.response.out.write('</table>')

	def post(self):
		pregunta = self.request.get('preguntaId')
		ndb.Key(Question, int(pregunta)).delete()
		self.redirect('/misPreguntas')

			
			
		
class ImageP(webapp2.RequestHandler):
		def get(self):
				question_key = ndb.Key(urlsafe=self.request.get('img_id'))
				question = question_key.get()
				if question.isImagen:
						self.response.headers['Content-Type'] = 'image/png'
						self.response.out.write(question.imagen)
				else:
						self.response.out.write('No image')

class Jugar(webapp2.RequestHandler):
	def get(self):
		self.response.write(ANONYMOUS_PLAY_PAGE_HTML % {"nick":"", "n_error": ""})
	def post(self):
		nick = self.request.get('nick')
		sani_nick = escape_html(nick)
		n_error = ""	
		error = False
		if sani_nick=="":
			n_error = "Introduce un nick"
			error = True
		if error:
			self.response.write(ANONYMOUS_PLAY_PAGE_HTML % {"nick":"sani_nick", "n_error": "n_error"})
		else:
			self.redirect('/tema?nick=%s' % sani_nick)

class Tema(webapp2.RequestHandler):
	def get(self):
		nick = self.request.get('nick')
		self.response.write(THEME_PAGE_HTML)
		temas = ndb.gql("SELECT DISTINCT tema FROM Question")
		self.response.out.write('<div id="temas">')
		if temas.count()==0:
			self.response.out.write('</br> Ahora mismo no hay ningun test disponible.')
		else:
			self.response.out.write('<h2>Temas</h2>')
			for tema in temas:
				self.response.out.write('</br> Tema: '+tema.tema+'<form method="post" action="/juego">')
				self.response.out.write('<input type="hidden" name="nick" value="'+nick+'"/>')
				self.response.out.write('<input type="hidden" name="tema" value="'+tema.tema+'"/>')
				self.response.out.write('<input type="submit" class="submit" value="Jugar" /> ')
				self.response.out.write('</form></br> ')
		self.response.out.write('</div>')

class Juego(webapp2.RequestHandler):
	def post(self):
		tema= self.request.get('tema')
		nick= self.request.get('nick')
		self.response.write(GAME_PAGE_HTML)
		preguntas= Question.query(Question.tema==tema)
		self.response.out.write('<div id="preguntas" class="preguntas" name="preguntas">')
		self.response.out.write('<a href="/tema?nick='+nick+'"><img class="back" src="images/back.png"></a>')
		self.response.out.write('</br> Preguntas sobre '+tema+'<div class="wrap"><form method="post" class="formulario">')
		self.response.out.write('<input type="hidden" name="nick" id="nick" value="'+nick+'"/>')
		self.response.out.write('<input type="hidden" name="tema" id="tema" value="'+tema+'"/>')
		self.response.out.write('<input type="hidden" name="numeroPreguntas" id="numeroPreguntas" value="'+str(preguntas.count())+'"/>')
		i=1
		for pregunta in preguntas:
			self.response.out.write('</br> Pregunta '+str(i)+': '+pregunta.pregunta)
			if pregunta.isImagen:
				self.response.out.write('</br><img src="/imgp?img_id='+pregunta.key.urlsafe()+'" width="96px" height="88px"/></br>')
			self.response.out.write('</br><div class="radio"><input type="radio" id="pregunta'+str(i+(i*10))+'" name="pregunta'+str(i)+'" value="1"><label for="pregunta'+str(i+(i*10))+'">'+pregunta.res_uno+'</label>')
			self.response.out.write('</br><input type="radio" id="pregunta'+str(i+(i*10)+1)+'" name="pregunta'+str(i)+'" value="2"><label for="pregunta'+str(i+(i*10)+1)+'">'+pregunta.res_dos+'</label>')
			self.response.out.write('</br><input type="radio" id="pregunta'+str(i+(i*10)+2)+'" name="pregunta'+str(i)+'" value="3"><label for="pregunta'+str(i+(i*10)+2)+'">'+pregunta.res_tres+'</label>')
			self.response.out.write('</div></br>')
			i=i+1
		self.response.out.write('</br><input type="button" value="Finalizar quiz" onclick="recuento()">')
		self.response.out.write('</form></div></br>')
		self.response.out.write('</div>')

class Resultado(webapp2.RequestHandler):
	def post(self):
		tema= self.request.get('tema')
		nick= self.request.get('nick')
		resultados= self.request.get('resultados').split(',')
		correctos=0
		incorrectos=0
		preguntas= Question.query(Question.tema==tema)
		i=0
		for pregunta in preguntas:
			if str(pregunta.respuesta_correcta)==resultados[i]:
				correctos=correctos+1
			else:
				incorrectos=incorrectos+1
			i=i+1
		jugador= Jugador.query(Jugador.nick==nick)
		if jugador.count()==0:
			j=Jugador()
			j.nick=nick
			j.aciertos=correctos
			j.fallos=incorrectos
			j.put()
		else:
			elJugador=jugador.get()
			elJugador.aciertos= elJugador.aciertos+correctos
			elJugador.fallos=elJugador.fallos+incorrectos
			elJugador.put()
		porcentaje=round((float(correctos)  /  float(correctos+incorrectos))*100,2)
		self.response.out.write('<a href="/tema?nick='+nick+'"><img class="back" src="images/back.png"></a>')
		self.response.out.write('</br><h3>Resultado del quiz</h3>')
		self.response.out.write('</br><table border="1">')
		self.response.out.write('<tr><th>Nick</th><th>Aciertos</th><th>Fallos</th><th>Porcentaje de aciertos</th></tr>')
		self.response.out.write('<tr><td>'+nick+'</td><td>'+str(correctos)+'</td><td>'+str(incorrectos)+'</td><td>'+str(porcentaje)+'%</td></tr>')
		self.response.out.write('</table>')


class Ranking(webapp2.RequestHandler):
	def get(self):
		self.response.write(RANKING_PAGE_HTML)
		jugadores = ndb.gql("SELECT * FROM Jugador ORDER BY aciertos DESC, fallos")
		self.response.out.write('<div id="ranking" class="ranking" name="ranking">')
		self.response.out.write('</br><h2>Ranking</h2>')
		if jugadores.count()==0:
			self.response.out.write('</br>Ahora mismo no hay ningun jugador en el ranking.')
		else:
			self.response.out.write('</br><table border="1">')
			self.response.out.write('<tr><th>Posicion</th><th>Nick</th><th>Aciertos</th><th>Fallos</th></tr>')
			i=1
			for jugador in jugadores:
				self.response.out.write('<tr><td>'+str(i)+'</td><td>'+jugador.nick+'</td><td>'+str(jugador.aciertos)+'</td><td>'+str(jugador.fallos)+'</td></tr>')
				i=i+1
			self.response.out.write('</table>')



app = webapp2.WSGIApplication([
		('/', MainPage),
	('/register', Registro),
	('/login', Login),
	('/logout', Logout),
	('/comprobar', ComprobarEmail),
	('/perfil', Perfil),
	('/img', Image),
	('/imgp', ImageP),
	('/anadirPregunta', AnadirPregunta),
	('/preguntas', VerPreguntas),
	('/tablaPreguntas', TablaPreguntas),
	('/misPreguntas', MisPreguntas),
	('/loginGoogle', LoginGoogle),
	('/cambioPassword', CambiarPassword),
	('/jugar', Jugar),
	('/tema', Tema),
	('/juego', Juego),
	('/resultado', Resultado),
	('/ranking', Ranking)
], config = session_module.myconfig_dict, debug=True)

