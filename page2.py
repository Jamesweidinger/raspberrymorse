<html>

<form name="crypto" method="post" action="page1.php">
    <p><input type="submit" name="submit" value="send something else"></p>
</form>

<?php
if (isset($_POST['submit'])) {
	//data to be hashed
	$message = $_POST['message'];

}



echo "the file PREVIOUSLY read:   ";
$myfile = fopen("inbound.txt", "r") or die("Unable to open file!");
$content = fread($myfile,filesize("inbound.txt"));
echo fread($myfile,filesize("inbound.txt"));
echo $content;
fclose($myfile);

$myfile = fopen("inbound.txt", "w") or die("Unable to open file!");
$txt = $message;
fwrite($myfile, $txt);
fclose($myfile);
?>

</br>

<?php
echo "The file NOW SHOULD read:   ";
echo $message
?>



</html>
