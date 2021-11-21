<?php
if($_GET['submit'] == 'content')
	$text = $_GET['message'];
else
	$text = $_GET['keyword'];


$cmd = 'python quizgen_v3.py '.'"'.$text.'"';
$results = shell_exec($cmd);
//echo json_encode($results, JSON_PRETTY_PRINT); 

?>


<html>
<head>
  <link rel="stylesheet" href="style.css">
</head>
<script src="script.js"></script>

<body style="height:100%">

<header>
	<h2 style="color:green">Quiz Generated Successfully!!</h2>
</header>
<div style="height:100%" id="form">

<div class="fish" id="fish"></div>
<div class="fish" id="fish2"></div>

<form style="margin-top:-30px" id="waterform" method="get" action="generate.php">


<div class="formgroup" id="message-form">
    <label for="message">You can edit the quiz here (json): </label>
    <textarea id="message" name="message" style="height:400px"><?php echo $results ?></textarea>
</div>

	<input type="submit" value="GENERATE" />
</form><br>
<!--
<script>
    var ugly = <?php //echo "'".substr(str_replace("'",'"',"$results"), 0, -1)."'" ?>;
    var obj = JSON.parse(ugly);
    var pretty = JSON.stringify(obj, undefined, 4);
    document.getElementById('message').value = pretty;

</script>
-->
</div>
</body>
