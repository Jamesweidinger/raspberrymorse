<html>

<head><title>Crypto, the other other superman pet</title></head>
<body>
<h3>Encrypt some stuff to be sent:</h3>

<form name="crypto" method="post" action="page1.php">
	<p>Hash what?<input type="text" name="rawtext" value="encryptmebaby"></p>
	<p><input type="submit" name="submit" value="hash this"></p>
	<p>select an encryption method:  <select name="crypto">
		<option value="md5">md5</option>
		<option value="sha1">sha1</option>
		<option value="sha256">sha256</option>
		<option value="snefru">snefru</option>
		<option value="sha384">sha384</option>
		<option value="sha512">sha512</option>
		<option value="ripemd320">ripmd320</option>
		<option value="whirlpool">whirlpool</option>
		<option value="tiger160,4">tiger160,4</option>
		<option value="gost">gost</option>
		<option value="crc326">crc326</option>
		<option value="haval224,4">haval224,4</option>
	</select></p>
</form>
</br></br></br></br>
<form name="crypto" method="post" action="page2.php">
    <p>Send what?<input type="text" name="message"></p>
	<p><input type="submit" name="submit" value="Send"></p>
</form>

<form name="crypto" action="page1.php">
	<p><input type="submit" name="submit" value="refresh"></p>
</form>

<?php

if (isset($_POST['submit'])) {
	//data to be hashed
	$message = $_POST['rawtext'];
	$hashtype = $_POST['crypto'];
	$messedup = hash($hashtype,$message);
	echo '<p>The original message = '.$message.'</p>';
	echo '<p>The hashing method = '.$hashtype.'</p>';
	echo '<p>The hashed message = '.$messedup.'</p>';

}

echo "the file currently reads   ";
$myfile = fopen("inbound.txt", "r") or die("Unable to open file!");
$content = fread($myfile,filesize("inbound.txt"));
echo fread($myfile,filesize("inbound.txt"));
echo $content;
fclose($myfile);
?>




</html>
