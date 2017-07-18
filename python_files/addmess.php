<?php
if(isset($_POST['message']))
{
   $mess=$_POST['message'];
   $reply="";

   file_put_contents("../chat.txt","\r\n".'2###'.$mess,FILE_APPEND);
   
   $reply=findreply($mess);
   $part=explode("\n",$reply);
   $joined=join("<>",$part);
   file_put_contents("../chat.txt","\r\n".'1###'.$joined,FILE_APPEND);
   $joined2=join('<br/>',$part);
   echo $joined2;
}
else
echo 'false';

function findreply($str)
{
    $result = shell_exec('C:\Python27\python.exe C:\xampp\htdocs\DinoBot\python_files\controller.py '.'"'.$str.'"');
  
    return $result;
}

?>