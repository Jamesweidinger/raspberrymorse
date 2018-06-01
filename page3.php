<html>


<form name="crypto" action="page3.php">
	<p><input type="submit" name="submit" value="refresh"></p>
</form>	
</br>
<form name="crypto" action="page4.php">
	<p><input type="submit" name="submit" value="clear chat history"></p>
</form>	

<?php
echo "the Pi is saying:   ";
$myfile = fopen("outbound.txt", "r") or die("Unable to open file!");
$content = fread($myfile,filesize("outbound.txt"));
echo fread($myfile,filesize("outbound.txt"));
echo $content;
fclose($myfile);
?>




</html>
