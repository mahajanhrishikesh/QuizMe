<html>
<head>
  <link rel="stylesheet" href="style.css">
</head>
<script src="script.js"></script>
<body style="height:100%">

<header>
	<h2>Quiz Generator</h2>
</header>
<div style="height:100%" id="form">

<div class="fish" id="fish"></div>
<div class="fish" id="fish2"></div>

<form style="margin-top:-30px" id="waterform" method="get" action="quiz.php">


<div class="formgroup" id="message-form">
    <label for="message">Drop Your Text Content Here</label>
    <textarea id="message" name="message" style="height:230px"></textarea>
</div>

	<input type="submit" value="Create Quiz" />
	<input type="hidden" name="submit" value="content" />
</form><br>
<center style="font-size:1.5em">OR</center>
<form style="margin-top:-60px" method="get" action="quiz.php">


<div class="formgroup" id="message-form">
    <label for="message">Enter Topic</label>
    <textarea id="message" name="keyword" style="height:50px"></textarea>
</div>

	<input type="submit" value="Create Quiz" />
	<input type="hidden" name="submit" value="wiki" />
</form>
</div>
</body>
